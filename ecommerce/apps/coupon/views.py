from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coupon
from .serializers import CouponSerializer


class CheckCouponView(APIView):
    def get(self, request):
        try:
            coupon_name = request.query_params.get('coupon_name')
            print(coupon_name)

            if Coupon.objects.get_active_list().filter(name=coupon_name).exists():
                coupon = Coupon.objects.get_active_list().get(name=coupon_name)
                coupon = CouponSerializer(coupon)

                return Response(
                    {'coupon': coupon.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'Coupon code not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except:
            return Response(
                {'error': 'Something went wrong when checking coupon'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
