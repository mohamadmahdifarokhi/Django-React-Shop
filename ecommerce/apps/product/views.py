from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from apps.product.models import Product
from apps.product.serializers import ProductSerializer
from apps.category.models import Category
from django.db.models import Q


class ProductDetailView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pid):
        try:
            product_id = int(pid)
        except:
            return Response(
                {'error': 'Product ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND)

        if Product.objects.get_active_list().filter(id=product_id).exists():
            product = Product.objects.get_active_list().get(id=product_id)

            product = ProductSerializer(product)

            return Response({'product': product.data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Product with this ID does not exist'},
                status=status.HTTP_404_NOT_FOUND)


class ListProductsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        sort_by = request.query_params.get('sort_by')

        if not (sort_by == 'created' or sort_by == 'price' or sort_by == 'sold' or sort_by == 'name'):
            sort_by = 'created'

        order = request.query_params.get('order')
        limit = request.query_params.get('limit')

        if not limit:
            limit = 6

        try:
            limit = int(limit)
        except:
            return Response(
                {'error': 'Limit must be an integer'},
                status=status.HTTP_404_NOT_FOUND)

        if limit <= 0:
            limit = 6

        if order == 'desc':
            sort_by = '-' + sort_by
            products = Product.objects.get_active_list().order_by(sort_by).all()[:int(limit)]
        elif order == 'asc':
            products = Product.objects.get_active_list().order_by(sort_by).all()[:int(limit)]
        else:
            products = Product.objects.get_active_list().order_by(sort_by).all()
        products = ProductSerializer(products, many=True)

        if products:
            return Response({'products': products.data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'No products to list'},
                status=status.HTTP_404_NOT_FOUND)


class ListSearchView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = self.request.data

        try:
            category_id = int(data['category_id'])
        except:
            return Response(
                {'error': 'Category ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND)

        search = data['search']

        if len(search) == 0:
            search_results = Product.objects.get_active_list().order_by('-created').all()
        else:
            search_results = Product.objects.get_active_list().filter(
                Q(description__icontains=search) | Q(name__icontains=search)
            )

        if category_id == 0:

            search_results = ProductSerializer(search_results, many=True)
            return Response(
                {'search_products': search_results.data},
                status=status.HTTP_200_OK)

        if not Category.objects.get_active_list().filter(id=category_id).exists():
            return Response(
                {'error': 'Category not found'},
                status=status.HTTP_404_NOT_FOUND)

        category = Category.objects.get_active_list().get(id=category_id)

        if category.parent:
            search_results = search_results.order_by(
                '-created'
            ).filter(category=category)

        else:
            if not Category.objects.get_active_list().filter(parent=category).exists():
                search_results = search_results.order_by(
                    '-created'
                ).filter(category=category)

            else:
                categories = Category.objects.get_active_list().filter(parent=category)
                filtered_categories = [category]

                for cat in categories:
                    filtered_categories.append(cat)

                filtered_categories = tuple(filtered_categories)

                search_results = search_results.order_by(
                    '-created'
                ).filter(category__in=filtered_categories)

        search_results = ProductSerializer(search_results, many=True)
        return Response({'search_products': search_results.data}, status=status.HTTP_200_OK)


class ListRelatedView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pid):
        try:
            product_id = int(pid)
        except:
            return Response(
                {'error': 'Product ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND)

        if not Product.objects.get_active_list().filter(id=product_id).exists():
            return Response(
                {'error': 'Product with this product ID does not exist'},
                status=status.HTTP_404_NOT_FOUND)

        category = Product.objects.get_active_list().get(id=product_id).category

        if Product.objects.get_active_list().filter(category=category).exists():
            if category.parent:
                related_products = Product.objects.get_active_list().order_by(
                    '-sold'
                ).filter(category=category)
            else:
                if not Category.objects.get_active_list().filter(parent=category).exists():
                    related_products = Product.objects.get_active_list().order_by(
                        '-sold'
                    ).filter(category=category)

                else:
                    categories = Category.objects.get_active_list().filter(parent=category)
                    filtered_categories = [category]

                    for cat in categories:
                        filtered_categories.append(cat)

                    filtered_categories = tuple(filtered_categories)
                    related_products = Product.objects.get_active_list().order_by(
                        '-sold'
                    ).filter(category__in=filtered_categories)

            related_products = related_products.exclude(id=product_id)
            related_products = ProductSerializer(related_products, many=True)

            if len(related_products.data) > 3:
                return Response(
                    {'related_products': related_products.data[:3]},
                    status=status.HTTP_200_OK)
            elif len(related_products.data) > 0:
                return Response(
                    {'related_products': related_products.data},
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {'error': 'No related products found'},
                    status=status.HTTP_200_OK)

        else:
            return Response(
                {'error': 'No related products found'},
                status=status.HTTP_200_OK)


class ListBySearchView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = self.request.data


        try:
            category_id = int(data['category_id'])
        except:
            return Response(
                {'error': 'Category ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND)

        price_range = data['price_range']
        sort_by = data['sort_by']

        if not (sort_by == 'created' or sort_by == 'price' or sort_by == 'sold' or sort_by == 'name'):
            sort_by = 'created'

        order = data['order']

        if category_id == 0:
            product_results = Product.objects.get_active_list().all()
        elif not Category.objects.get_active_list().filter(id=category_id).exists():
            return Response(
                {'error': 'This category does not exist'},
                status=status.HTTP_404_NOT_FOUND)
        else:
            category = Category.objects.get_active_list().get(id=category_id)
            if category.parent:
                product_results = Product.objects.get_active_list().filter(category=category)
            else:
                if not Category.objects.get_active_list().filter(parent=category).exists():
                    product_results = Product.objects.get_active_list().filter(category=category)
                else:
                    categories = Category.objects.get_active_list().filter(parent=category)
                    filtered_categories = [category]

                    for cat in categories:
                        filtered_categories.append(cat)

                    filtered_categories = tuple(filtered_categories)
                    product_results = Product.objects.get_active_list().filter(
                        category__in=filtered_categories)

        if price_range == '1 - 19':
            product_results = product_results.filter(price__gte=1)
            product_results = product_results.filter(price__lt=20)
        elif price_range == '20 - 39':
            product_results = product_results.filter(price__gte=20)
            product_results = product_results.filter(price__lt=40)
        elif price_range == '40 - 59':
            product_results = product_results.filter(price__gte=40)
            product_results = product_results.filter(price__lt=60)
        elif price_range == '60 - 79':
            product_results = product_results.filter(price__gte=60)
            product_results = product_results.filter(price__lt=80)
        elif price_range == 'More than 80':
            product_results = product_results.filter(price__gte=80)

        if order == 'desc':
            sort_by = '-' + sort_by
            product_results = product_results.order_by(sort_by)
        elif order == 'asc':
            product_results = product_results.order_by(sort_by)
        else:
            product_results = product_results.order_by(sort_by)

        product_results = ProductSerializer(product_results, many=True)

        if len(product_results.data) > 0:
            return Response(
                {'filtered_products': product_results.data},
                status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'No products found'},
                status=status.HTTP_200_OK)
