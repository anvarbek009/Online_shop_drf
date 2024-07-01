from django.shortcuts import render
from .models import Categories,Product,Order
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer,CategorySerializer,ProductSerializer
from rest_framework import status
# Create your views here.
class ProductView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    

class CategoriesView(APIView):
    def get(self,request):
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)


class OrderView(APIView):
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateProductsView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateProductsView(APIView):
    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteProductView(APIView):
    def delete(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CreateCategorytView(APIView):
    def post(self, request,pk):
        category = Categories.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateCategoriesView(APIView):
    def put(self, request, pk):
        category = Categories.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCategoriesView(APIView):
    def delete(self, request, pk):
        category = Categories.objects.get(id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateOrdersView(APIView):
    def put(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteOrdersView(APIView):
    def delete(self, request, pk):
        order = Order.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SearchProductsView(APIView):
    def get(self, request):
        query = request.GET.get('query')
        products = Product.objects.filter(name__icontains=query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class SearchCategoriesView(APIView):
    def get(self, request):
        query = request.GET.get('query')
        categories = Categories.objects.filter(name__icontains=query)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class SearchOrdersView(APIView):
    def get(self, request):
        query = request.GET.get('query')
        orders = Order.objects.filter(product__name__icontains=query)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class FilterProductsView(APIView):
    def get(self, request):
        min_price = request.GET.get('min_price', 0)
        max_price = request.GET.get('max_price', float('inf'))
        products = Product.objects.filter(price__gte=min_price, price__lte=max_price)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
       

class FilterOrdersView(APIView):
    def get(self, request):
        min_price = request.GET.get('min_price', 0)
        max_price = request.GET.get('max_price', float('inf'))
        orders = Order.objects.filter(product__price__gte=min_price, product__price__lte=max_price)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class GetProductsByCategoryView(APIView):
    def get(self, request, pk):
        category = Categories.objects.get(id=pk)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    