from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('authors/', views.all_authors, name='authors'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_category/', views.add_category, name='add_category'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]