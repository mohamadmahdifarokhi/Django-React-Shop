from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('auth/', include('djoser.urls')),
                  path('auth/', include('djoser.urls.jwt')),
                  path('auth/', include('djoser.social.urls')),

                  path('api/category/', include('apps.category.urls', namespace='category')),
                  path('api/product/', include('apps.product.urls', namespace='product')),
                  path('api/cart/', include('apps.cart.urls', namespace='cart')),
                  path('api/shipping/', include('apps.shipping.urls', namespace='shipping')),
                  path('api/order/', include('apps.order.urls', namespace='order')),
                  path('api/payment/', include('apps.payment.urls')),
                  path('api/coupon/', include('apps.coupon.urls')),
                  path('api/profile/', include('apps.user_profile.urls')),
                  path('api/wishlist/', include('apps.wishlist.urls')),
                  path('api/review/', include('apps.review.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
