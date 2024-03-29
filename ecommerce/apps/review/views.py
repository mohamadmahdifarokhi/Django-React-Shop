from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from apps.product.models import Product
from .models import Review


class GetProductReviewsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, productId):
        try:
            product_id = int(productId)
        except:
            return Response(
                {'error': 'Product ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            if not Product.objects.get_active_list().filter(id=product_id).exists():
                return Response(
                    {'error': 'This product does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            product = Product.objects.get_active_list().get(id=product_id)

            results = []

            if Review.objects.get_active_list().filter(product=product).exists():
                reviews = Review.objects.get_active_list().order_by(
                    '-created'
                ).filter(product=product)

                for review in reviews:
                    item = {}

                    item['id'] = review.id
                    item['rating'] = review.rating
                    item['head'] = review.head
                    item['body'] = review.body
                    item['created'] = review.created
                    item['user'] = review.user.first_name

                    results.append(item)

            return Response(
                {'reviews': results},
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                {'error': 'Something went wrong when retrieving reviews'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetProductReviewView(APIView):
    def get(self, request, productId):
        user = self.request.user

        try:
            product_id = int(productId)
        except:
            return Response(
                {'error': 'Product ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            if not Product.objects.get_active_list().filter(id=product_id).exists():
                return Response(
                    {'error': 'This product does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            product = Product.objects.get_active_list().get(id=product_id)

            result = {}

            if Review.objects.get_active_list().filter(user=user, product=product).exists():
                review = Review.objects.get_active_list().get(user=user, product=product)

                result['id'] = review.id
                result['rating'] = review.rating
                result['head'] = review.head
                result['body'] = review.body
                result['created'] = review.created
                result['user'] = review.user.first_name

            if len(result) == 0:
                return Response(
                    {'review': None},
                    status=status.HTTP_200_OK
                )

            return Response(
                {'review': result},
                status=status.HTTP_200_OK
            )


        except:
            return Response(
                {'error': 'Something went wrong when retrieving review'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CreateProductReviewView(APIView):
    def post(self, request, productId):
        user = self.request.user
        data = self.request.data

        try:
            rating = float(data['rating'])
        except:
            return Response(
                {'error': 'Rating must be a decimal value'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            head = str(data['head'])
            body = str(data['body_2'])
        except:
            return Response(
                {'error': 'Must pass a comment when creating review'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            if not Product.objects.get_active_list().filter(id=productId).exists():
                return Response(
                    {'error': 'This Product does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            product = Product.objects.get_active_list().get(id=productId)

            result = {}
            results = []

            if Review.objects.get_active_list().filter(user=user, product=product).exists():
                return Response(
                    {'error': 'Review for this course already created'},
                    status=status.HTTP_409_CONFLICT
                )

            review = Review.objects.get_active_list().create(
                user=user,
                product=product,
                rating=rating,
                head=head,
                body=body
            )

            if Review.objects.get_active_list().filter(user=user, product=product).exists():
                result['id'] = review.id
                result['rating'] = review.rating
                result['head'] = review.head
                result['body'] = review.body
                result['created'] = review.created
                result['user'] = review.user.first_name

                reviews = Review.objects.get_active_list().order_by('-created').filter(
                    product=product
                )

                for review in reviews:
                    item = {}

                    item['id'] = review.id
                    item['rating'] = review.rating
                    item['head'] = review.head
                    item['body'] = review.body
                    item['created'] = review.created
                    item['user'] = review.user.first_name

                    results.append(item)

            return Response(
                {'review': result, 'reviews': results},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {'error': 'Something went wrong when creating review'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdateProductReviewView(APIView):
    def put(self, request, productId):
        user = self.request.user
        data = self.request.data

        try:
            product_id = int(productId)
        except:
            return Response(
                {'error': 'Product ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            rating = float(data['rating'])
        except:
            return Response(
                {'error': 'Rating must be a decimal value'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            head = str(data['head'])
            body = str(data['body_2'])
        except:
            return Response(
                {'error': 'Must pass a comment when creating review'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            if not Product.objects.get_active_list().filter(id=product_id).exists():
                return Response(
                    {'error': 'This product does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            product = Product.objects.get_active_list().get(id=product_id)

            result = {}
            results = []

            if not Review.objects.get_active_list().filter(user=user, product=product).exists():
                return Response(
                    {'error': 'Review for this product does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            if Review.objects.get_active_list().filter(user=user, product=product).exists():
                Review.objects.get_active_list().filter(user=user, product=product).update(
                    rating=rating,
                    head=head,
                    body=body
                )

                review = Review.objects.get_active_list().get(user=user, product=product)

                result['id'] = review.id
                result['rating'] = review.rating
                result['head'] = review.head
                result['body'] = review.body
                result['created'] = review.created
                result['user'] = review.user.first_name

                reviews = Review.objects.get_active_list().order_by('-created').filter(
                    product=product
                )

                for review in reviews:
                    item = {}

                    item['id'] = review.id
                    item['rating'] = review.rating
                    item['head'] = review.head
                    item['body'] = review.body
                    item['created'] = review.created
                    item['user'] = review.user.first_name

                    results.append(item)

            return Response(
                {'review': result, 'reviews': results},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when updating review'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DeleteProductReviewView(APIView):
    def delete(self, request, productId):
        user = self.request.user

        try:
            product_id = int(productId)
        except:
            return Response(
                {'error': 'Product ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            if not Product.objects.get_active_list().filter(id=product_id).exists():
                return Response(
                    {'error': 'This product does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            product = Product.objects.get_active_list().get(id=product_id)

            results = []

            if Review.objects.get_active_list().filter(user=user, product=product).exists():
                Review.objects.get_active_list().filter(user=user, product=product).delete()

                reviews = Review.objects.get_active_list().order_by('-created').filter(
                    product=product
                )

                for review in reviews:
                    item = {}

                    item['id'] = review.id
                    item['rating'] = review.rating
                    item['head'] = review.head
                    item['body'] = review.body
                    item['created'] = review.created
                    item['user'] = review.user.first_name

                    results.append(item)

                return Response(
                    {'reviews': results},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'Review for this product does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except:
            return Response(
                {'error': 'Something went wrong when deleting product review'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FilterProductReviewsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, productId):
        try:
            product_id = int(productId)
        except:
            return Response(
                {'error': 'Product ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND
            )

        if not Product.objects.get_active_list().filter(id=product_id).exists():
            return Response(
                {'error': 'This product does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )

        product = Product.objects.get_active_list().get(id=product_id)

        rating = request.query_params.get('rating')

        try:
            rating = float(rating)
        except:
            return Response(
                {'error': 'Rating must be a decimal value'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            if not rating:
                rating = 5.0
            elif rating > 5.0:
                rating = 5.0
            elif rating < 0.5:
                rating = 0.5

            results = []

            if Review.objects.get_active_list().filter(product=product).exists():
                if rating == 0.5:
                    reviews = Review.objects.get_active_list().order_by('-created').filter(
                        rating=rating, product=product
                    )
                else:
                    reviews = Review.objects.get_active_list().order_by('-created').filter(
                        rating__lte=rating,
                        product=product
                    ).filter(
                        rating__gte=(rating - 0.5),
                        product=product
                    )

                for review in reviews:
                    item = {}

                    item['id'] = review.id
                    item['rating'] = review.rating
                    item['head'] = review.head
                    item['body'] = review.body
                    item['created'] = review.created
                    item['user'] = review.user.first_name

                    results.append(item)

            return Response(
                {'reviews': results},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when filtering reviews for product'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
