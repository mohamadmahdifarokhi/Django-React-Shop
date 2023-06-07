import random

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.cart.models import Cart, CartItem
from apps.coupon.models import Coupon
from apps.order.models import Order, OrderItem
from apps.product.models import Product
from apps.shipping.models import Shipping
from django.core.mail import send_mail


class GetPaymentTotalView(APIView):
    def get(self, request):
        user = self.request.user

        tax = 0

        shipping_id = request.query_params.get('shipping_id')
        shipping_id = str(shipping_id)

        coupon_name = request.query_params.get('coupon_name')
        coupon_name = str(coupon_name)

        try:
            cart = Cart.objects.get_active_list().get(user=user)


            if not CartItem.objects.get_active_list().filter(cart=cart).exists():
                return Response(
                    {'error': 'Need to have items in cart'},
                    status=status.HTTP_404_NOT_FOUND
                )

            cart_items = CartItem.objects.get_active_list().filter(cart=cart)

            for cart_item in cart_items:
                if not Product.objects.get_active_list().filter(id=cart_item.product.id).exists():
                    return Response(
                        {'error': 'A proudct with ID provided does not exist'},
                        status=status.HTTP_404_NOT_FOUND
                    )
                if int(cart_item.count) > int(cart_item.product.count):
                    return Response(
                        {'error': 'Not enough items in stock'},
                        status=status.HTTP_200_OK
                    )

                total_amount = 0.0
                total_discount_amount = 0.0

                for cart_item in cart_items:
                    total_amount += (float(cart_item.product.price)
                                     * float(cart_item.count))
                    total_discount_amount += (float(cart_item.product.discount_price)
                                              * float(cart_item.count))

                total_discount_amount = round(total_discount_amount, 2)
                original_price = round(total_amount, 2)

                # Cupones
                # if coupon_name != '':
                #     # Revisar si cupon de precio fijo es valido
                #     if FixedPriceCoupon.objects.get_active_list().filter(name__iexact=coupon_name).exists():
                #         fixed_price_coupon = FixedPriceCoupon.objects.get_active_list().get(
                #             name=coupon_name
                #         )
                #     discount_amount = float(fixed_price_coupon.discount_price)
                #     if discount_amount < total_amount:
                #         total_amount -= discount_amount
                #         total_after_coupon = total_amount
                #
                #     elif PercentageCoupon.objects.get_active_list().filter(name__iexact=coupon_name).exists():
                #         percentage_coupon = PercentageCoupon.objects.get_active_list().get(
                #             name=coupon_name
                #         )
                #         discount_percentage = float(
                #             percentage_coupon.discount_percentage)
                #
                #         if discount_percentage > 1 and discount_percentage < 100:
                #             total_amount -= (total_amount *
                #                              (discount_percentage / 100))
                #             total_after_coupon = total_amount

                # Total despues del cupon
                # total_after_coupon = round(total_after_coupon, 2)


                estimated_tax = round(total_amount * tax, 2)

                total_amount += (total_amount * tax)

                shipping_cost = 0.0
                if Shipping.objects.get_active_list().filter(id__iexact=shipping_id).exists():
                    shipping = Shipping.objects.get_active_list().get(id=shipping_id)
                    shipping_cost = shipping.price
                    total_amount += float(shipping_cost)

                total_amount = round(total_amount, 2)

                return Response({
                    'original_price': f'{original_price:.2f}',
                    # 'total_after_coupon': f'{total_after_coupon:.2f}',
                    'total_amount': f'{total_amount:.2f}',
                    'total_discount_amount': f'{total_discount_amount:.2f}',
                    'estimated_tax': f'{estimated_tax:.2f}',
                    'shipping_cost': f'{shipping_cost:.2f}'
                },
                    status=status.HTTP_200_OK
                )

        except:
            return Response(
                {'error': 'Something went wrong when retrieving payment total information'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ProcessPaymentView(APIView):
    def post(self, request):
        user = self.request.user
        data = self.request.data
        print(data)

        tax = 0.18

        # nonce = data['nonce']
        shipping_id = str(data['shipping_id'])
        coupon_name = str(data['coupon_name'])
        print('d')
        full_name = data['full_name']
        address = data['address']
        city = data['city']
        price = data['price']
        discount_price = data['discount_price']
        # coupon_name = data['coupon_name']
        # shipping_id = data['shipping_id']
        print(data['shipping_id'])
        # print(price)
        # print(discount_price)
        print('-------')
        print('1')

        if not Shipping.objects.get_active_list().filter(id__iexact=shipping_id).exists():
            print('j')
            return Response(
                {'error': 'Invalid shipping option'},
                status=status.HTTP_404_NOT_FOUND
            )

        cart = Cart.objects.get_active_list().get(user=user)
        print('2')

        if not CartItem.objects.get_active_list().filter(cart=cart).exists():
            return Response(
                {'error': 'Need to have items in cart'},
                status=status.HTTP_404_NOT_FOUND
            )

        cart_items = CartItem.objects.get_active_list().filter(cart=cart)

        for cart_item in cart_items:
            if not Product.objects.get_active_list().filter(id=cart_item.product.id).exists():
                return Response(
                    {'error': 'Transaction failed, a proudct ID does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )
            if int(cart_item.count) > int(cart_item.product.count):
                return Response(
                    {'error': 'Not enough items in stock'},
                    status=status.HTTP_200_OK
                )

        total_amount = 0.0
        print('3')
        for cart_item in cart_items:
            total_amount += (float(cart_item.product.price)
                             * float(cart_item.count))

        if coupon_name != '':
            if Coupon.objects.get_active_list().filter(name__iexact=coupon_name).exists():
                coupon = Coupon.objects.get_active_list().get(
                    name=coupon_name
                )
                if coupon.discount_price != None:
                    discount_amount = float(coupon.discount_price)
                    if discount_amount < total_amount:
                        total_amount -= discount_amount
                else:
                    discount_percentage = float(
                        coupon.discount_percentage)

                    if discount_percentage > 1 and discount_percentage < 100:
                        total_amount -= (total_amount *
                                         (discount_percentage / 100))
        else:
            coupon = None
        print('4')

        total_amount += (total_amount * tax)
        print('ffffffffff')
        print(total_amount)
        shipping = Shipping.objects.get_active_list().get(id=int(shipping_id))

        shipping_name = shipping.name
        shipping_time = shipping.time
        shipping_price = shipping.price

        total_amount += float(shipping_price)
        total_amount = round(total_amount, 2)

        # try:
        #     newTransaction = gateway.transaction.sale(
        #         {
        #             'amount': str(total_amount),
        #             'payment_method_nonce': str(nonce['nonce']),
        #             'options': {
        #                 'submit_for_settlement': True
        #             }
        #         }
        #     )
        # except:
        #     return Response(
        #         {'error': 'Error processing the transaction'},
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #     )
        print('5')

        if True:
            for cart_item in cart_items:
                update_product = Product.objects.get_active_list().get(id=cart_item.product.id)

                quantity = int(update_product.count) - int(cart_item.count)

                sold = int(update_product.sold) + int(cart_item.count)

                Product.objects.get_active_list().filter(id=cart_item.product.id).update(
                    count=quantity, sold=sold
                )

            try:
                if Coupon:
                    random_num = random.randint(100000, 999999)
                    print(Coupon)
                    print('d')
                    print(user, coupon, full_name, address, city, price, shipping_name,
                          shipping_price, shipping_time)
                    order = Order.objects.get_active_list().create(
                        user=user,
                        coupon=coupon,
                        transaction_id=str(random_num),
                        full_name=full_name,
                        address=address,
                        city=city,
                        price=total_amount,
                        discount_price=total_amount,
                        shipping_name=shipping_name,
                        shipping_price=shipping_price,
                        shipping_time=shipping_time,
                        status='not_processed'
                    )
                else:
                    order = Order.objects.get_active_list().create(
                        user=user,
                        transaction_id='45',
                        full_name=full_name,
                        address=address,
                        city=city,
                        price=total_amount,
                        discount_price=total_amount,
                        shipping_name=shipping_name,
                        shipping_price=shipping_price,
                        shipping_time=shipping_time,
                        status='not_processed'
                    )
            except Exception as e:
                print(e)
                return Response(
                    {'error': 'Transaction succeeded but failed to create the order'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            print('6')

            for cart_item in cart_items:
                try:
                    product = Product.objects.get_active_list().get(id=cart_item.product.id)
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        name=product.name,
                        price=cart_item.product.price,
                        discount_price=cart_item.product.discount_price,
                        count=cart_item.count,
                        status='not_processed'
                    )

                except Exception as e:
                    print(e)
                    return Response(
                        {'error': 'Transaction succeeded and order created, but failed to create an order item'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
            print('7')

            # try:
            #     send_mail(
            #         'Your Order Details',
            #         'Hey ' + full_name + ','
            #         + '\n\nWe recieved your order!'
            #         + '\n\nGive us some time to process your order and ship it out to you.'
            #         + '\n\nYou can go on your user dashboard to check the status of your order.'
            #         + '\n\nSincerely,'
            #         + '\nShop Time',
            #         [user.email],
            #         fail_silently=False
            #     )
            # except:
            #     return Response(
            #         {'error': 'Transaction succeeded and order created, but failed to send email'},
            #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
            #     )

            print('8')

            try:
                CartItem.objects.get_active_list().filter(cart=cart).delete()

            except Exception as e:
                print(e)
                return Response(
                    {'error': 'Transaction succeeded and order successful, but failed to clear cart'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            print('9')

            return Response(
                {'success': 'Transaction successful and order was created'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Transaction failed'},
                status=status.HTTP_400_BAD_REQUEST
            )
