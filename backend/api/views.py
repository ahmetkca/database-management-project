# from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework import  viewsets
from api.models import View1, FiredEmployee, Customer, Order, Transaction, Store, Employee, Inventory, StorageRack, Product, ProductType, ProductSpecification, View10, View11, View12, View13, View2, View3, View4, View5, View8, View9
from api.serializers import View10Serializer, View11Serializer, View12Serializer, View13Serializer, View1Serializer, FiredEmployeeSerializer, CustomerSerializer, OrderSerializer, TransactionSerializer, StoreSerializer, EmployeeSerializer, InventorySerializer, ProductSerializer, ProductTypeSerializer, ProductSpecificationSerializer, StorageRackSerializer, View2Serializer, View3Serializer, View4Serializer, View5Serializer, View8Serializer, View9Serializer

# Create your views here.

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all().order_by("product_type_name")
    serializer_class = ProductTypeSerializer

class ProductSpecificationViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
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

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FiredEmployeeViewSet(viewsets.ModelViewSet):
    queryset = FiredEmployee.objects.all()
    serializer_class = FiredEmployeeSerializer

class View1ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View1.objects.all()
    serializer_class = View1Serializer

class View2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View2.objects.all()
    serializer_class = View2Serializer

class View3ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View3.objects.all()
    serializer_class = View3Serializer

class View4ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View4.objects.all()
    serializer_class = View4Serializer

class View5ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View5.objects.all()
    serializer_class = View5Serializer

class View8ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View8.objects.all()
    serializer_class = View8Serializer

class View9ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View9.objects.all()
    serializer_class = View9Serializer

class View10ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View10.objects.all()
    serializer_class = View10Serializer

class View11ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View11.objects.all()
    serializer_class = View11Serializer

class View12ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View12.objects.all()
    serializer_class = View12Serializer

class View13ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = View13.objects.all()
    serializer_class = View13Serializer