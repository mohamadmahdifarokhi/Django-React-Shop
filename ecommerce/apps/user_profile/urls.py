from django.urls import path
from .views import GetUserProfileView, UpdateUserProfileView, GetUserAddressView

urlpatterns = [
    path('user', GetUserProfileView.as_view()),
    path('update', UpdateUserProfileView.as_view()),
    path('address', GetUserAddressView.as_view()),
]
