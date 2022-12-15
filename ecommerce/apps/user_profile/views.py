from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile, Address
from .serializers import UserProfileSerializer


class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            user_profile = UserProfile.objects.get(user=user)
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


class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
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
