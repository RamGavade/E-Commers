from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),    # path('remove/', views.remove_from_cart, name='remove_from_cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('update/', views.update_cart, name='update_cart'),
    # path('success/', views.success, name='purchase_success'),
]