from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile, Address
from .serializers import UserProfileSerializer, AddressSerializer


class GetUserProfileView(APIView):

    def get(self, request):
        try:
            user = self.request.user
            user_profile = UserProfile.objects.get(user=user)
            address = user_profile.address.address
            city = user_profile.address.city
            user_profile = UserProfileSerializer(user_profile)

            return Response(
                {'profile': user_profile.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving profile'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetUserAddressView(APIView):

    def post(self, request):
        try:
            print('xxxxxxxx')
            user = self.request.user
            user_profile = UserProfile.objects.get(user=user)
            address = user_profile.address
            print(address)
            address = AddressSerializer(address)

            return Response(
                {'address': address.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving address'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdateUserProfileView(APIView):
    def put(self, request):
        try:
            user = self.request.user
            data = self.request.data

            body = data['body_2']
            city = data['city']
            phone = data['phone']
            image = data['image']
            print(body)
            print(city)
            print(phone)
            print(image)

            user_profile = UserProfile.objects.get(user=user)
            address = Address.objects.get(id=user_profile.address.id)

            if body == '':
                body = address.body

            if city == '':
                city = address.city

            if phone == '':
                phone = user_profile.phone

            if image == '':
                image = user_profile.image

            address = Address.objects.create(
                body=body,
                city=city,
            )

            UserProfile.objects.filter(user=user).update(
                address=address,
                phone=phone,
                image=image
            )

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response(
                {'profile': user_profile.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when updating profile'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
