from django.urls import path
from .views import *

urlpatterns = [
    path('products/',ProductView.as_view()),
    path('categories/',CategoriesView.as_view()),
    path('orders/', OrderView.as_view()),
    path('products/create/', CreateProductsView.as_view()),
    path('products/<int:pk>/update/', UpdateProductsView.as_view()),
    path('products/<int:pk>/delete/', DeleteProductView.as_view()),
    path('categories/<int:pk>/create/', CreateCategorytView.as_view()),
    path('categories/<int:pk>/update/', UpdateCategoriesView.as_view()),
    path('categories/<int:pk>/delete/', DeleteCategoriesView.as_view()),
    path('orders/<int:pk>/update/', UpdateOrdersView.as_view()),
    path('orders/<int:pk>/delete/', DeleteOrdersView.as_view()),
    path('search/products/', SearchProductsView.as_view()),
    path('search/categories/', SearchCategoriesView.as_view()),
    path('search/orders/', SearchOrdersView.as_view()),
    path('filter/products/', FilterProductsView.as_view()),
    path('filter/orders/', FilterOrdersView.as_view()),
    path('products/category/<int:pk>/', GetProductsByCategoryView.as_view()),
]