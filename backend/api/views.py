# from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from api.models import Store, Employee, Inventory, StorageRack, Product, ProductType, ProductSpecification
from api.serializers import StoreSerializer, EmployeeSerializer, InventorySerializer, ProductSerializer, ProductTypeSerializer, ProductSpecificationSerializer, StorageRackSerializer

# Create your views here.

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all().order_by("product_type_name")
    serializer_class = ProductTypeSerializer

class ProductSpecificationViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecification.objects.all().order_by("product_specification_name")
    serializer_class = ProductSpecificationSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("product_name")
    serializer_class = ProductSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class StorageRackViewSet(viewsets.ModelViewSet):
    queryset = StorageRack.objects.all()
    serializer_class = StorageRackSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
