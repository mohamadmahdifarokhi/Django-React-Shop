from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem


class ListOrdersView(APIView):
    def get(self, request):
        user = self.request.user
        print('d')
        try:
            orders = Order.objects.get_active_list().order_by('-created').filter(user=user)
            result = []

            for order in orders:
                item = {}
                item['user'] = order.user.first_name
                item['coupon'] = order.coupon
                item['transaction_id'] = str(order.transaction_id)
                item['full_name'] = order.full_name
                item['address'] = order.address
                item['city'] = order.city
                item['price'] = order.price
                item['discount_price'] = order.discount_price
                item['shipping_name'] = order.shipping_name
                item['shipping_price'] = order.shipping_price
                item['shipping_time'] = order.shipping_time
                item['status'] = order.status
                statuss = ['not_processed', 'processed', 'shipped', 'delivered', 'cancelled']
                count = -1
                for i in statuss:
                    count += 1
                    if order.status == i:
                        item['step'] = count

                result.append(item)
            print(result)
            return Response(
                {'orders': result},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong when retrieving orders'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ListOrderDetailView(APIView):
    def get(self, request, transactionId):
        user = self.request.user
        print('------------')
        try:
            if Order.objects.get_active_list().filter(user=user, transaction_id=transactionId).exists():
                order = Order.objects.get_active_list().get(user=user, transaction_id=transactionId)
                result = {}
                result['coupon'] = order.coupon
                result['transaction_id'] = str(order.transaction_id)
                result['full_name'] = order.full_name
                result['address'] = order.address
                result['city'] = order.city
                result['price'] = order.price
                result['discount_price'] = order.discount_price
                result['shipping_name'] = order.shipping_name
                result['shipping_price'] = order.shipping_price
                result['shipping_time'] = order.shipping_time
                result['status'] = order.status


                order_items = OrderItem.objects.get_active_list().order_by('-created').filter(order=order)
                result['order_items'] = []

                for order_item in order_items:
                    sub_item = {}

                    sub_item['name'] = order_item.name
                    sub_item['price'] = order_item.price
                    sub_item['count'] = order_item.count
                    print(order_item.product.photo.url)
                    sub_item['photo'] = order_item.product.photo.url
                    statuss = ['not_processed', 'processed', 'shipped', 'delivered', 'cancelled']
                    count = -1
                    for i in statuss:
                        count += 1
                        if order.status == i:
                            sub_item['step'] = count

                    result['order_items'].append(sub_item)
                print(result)
                return Response(
                    {'order': result},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'Order with this transaction ID does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving order detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
