from django.urls import path
from .views import ProductDetailView, ListProductsView, ListSearchView, ListRelatedView, ListBySearchView

app_name = 'product'
urlpatterns = [
    path('product/<pid>', ProductDetailView.as_view()),
    path('get-products', ListProductsView.as_view()),
    path('search', ListSearchView.as_view()),
    path('related/<pid>', ListRelatedView.as_view()),
    path('by/search', ListBySearchView.as_view()),
]