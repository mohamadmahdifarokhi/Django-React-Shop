from django.urls import path
from .views import CategoryListView

app_name = 'category'
urlpatterns = [
    path('categories', CategoryListView.as_view(), name='list'),
]

