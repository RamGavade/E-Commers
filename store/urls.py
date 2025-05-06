from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),  # Home store page
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),  # Category filter
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),  # Product detail
    path('search/', views.search, name='search'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]
