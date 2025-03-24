from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),  # Home store page
    path('store/<slug:category_slug>/', views.store, name='products_by_category'),  # Category filter
    path('store/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),  # Product detail
]
