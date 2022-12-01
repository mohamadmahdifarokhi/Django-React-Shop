from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from apps.product.models import Product
from apps.product.serializers import ProductSerializer
from apps.category.models import Category

from django.db.models import Q


class ProductDetailView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, product_id, format=None):
        try:
            product_id = int(product_id)
        except:
            return Response({'error': 'Invalid product id'}, status=status.HTTP_400_BAD_REQUEST)

        if Product.objects.filter(id=product_id).exists():
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            return Response({'product': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class ListProductsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        sort_by = request.query_params.get('sortBy')

        if not (sort_by == 'name' or sort_by == 'quality' or sort_by == 'sold' or sort_by == 'date_created'):
            sort_by = 'date_created'

        order = request.query_params.get('order')
        limit = request.query_params.get('limit')

        if not limit:
            limit = 6

        try:
            limit = int(limit)
        except:
            return Response({'error': 'Invalid limit'}, status=status.HTTP_400_BAD_REQUEST)

        if limit <= 0:
            limit = 6

        if order == 'desc':
            sort_by = '-' + sort_by
            products = Product.objects.order_by(sort_by).all()[:limit]
        elif order == 'asc':
            products = Product.objects.order_by(sort_by).all()[:limit]

        else:
            products = Product.objects.order_by(sort_by).all()

        products = ProductSerializer(products, many=True)

        if products:
            return Response({'products': products.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No products found'}, status=status.HTTP_400_BAD_REQUEST)


class ListSearchView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        data = request.request.data

        try:
            category_id = int(data['category_id'])
        except:
            return Response({'error': 'Invalid category id'}, status=status.HTTP_400_BAD_REQUEST)

        search = data['search']

        if len(search) == 0:
            search_results = Product.objects.order_by('-date_created').all()
        else:
            search_results = Product.objects.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )

        if category_id == 0:
            search_results = ProductSerializer(search_results, many=True)
            return Response({'search_results': search_results.data}, status=status.HTTP_200_OK)

        if not Category.objects.filter(id=category_id).exists():
            return Response({'error': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)

        category = Category.objects.get(id=category_id)

        if category.parent:
            search_results = search_results.order_by('-date_created').filter(category=category)
        else:
            if not Category.objects.filter(parent=category).exists():
                search_results = search_results.order_by('-date_created').filter(category=category)
            else:
                categories = Category.objects.filter(parent=category)
                filter_categories = [category]
                for cat in categories:
                    filter_categories.append(cat)

                filter_categories = tuple(filter_categories)

                search_results = search_results.order_by('-date_created').filter(category__in=filter_categories)

        search_results = ProductSerializer(search_results, many=True)
        return Response({'search_results': search_results.data}, status=status.HTTP_200_OK)

