from django.urls import path
from .views import homepage, change_product_class


urlpatterns = [
    path('', homepage, name='homepage'),
    path('change-product-class/', change_product_class, name='change_product_class')
] 
