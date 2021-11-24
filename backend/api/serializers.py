from rest_framework import serializers
from api.models import (
    FiredEmployee,
    Order, 
    Transaction, 
    Store, 
    StorageRack,
    Inventory,
    Customer,
    Employee,
    Product,
    ProductSpecification,
    ProductType,
    View1,
    View10,
    View11,
    View12,
    View13,
    View2,
    View3,
    View4,
    View5,
    View8,
    View9
    )
from django.db import IntegrityError
import logging
from django.conf import settings

fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

logging.basicConfig(format=fmt, level=lvl)


class ProductTypeSerializer(serializers.ModelSerializer):
    specifications = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProductType
        fields = ['product_type_id', 'product_type_name', 'specifications']


class ProductSpecificationSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer(read_only=True)

    class Meta:
        model = ProductSpecification
        fields = ['product_specification_id', 'product_specification_name', 'product_specification_value', 'product_type']


class ProductSerializer(serializers.ModelSerializer):
    spec1 = ProductSpecificationSerializer(read_only=True)
    spec2 = ProductSpecificationSerializer(read_only=True)
    spec3 = ProductSpecificationSerializer(read_only=True)
    product_type = ProductTypeSerializer(read_only=True)
    spec1_id = serializers.IntegerField(write_only=True)
    spec2_id = serializers.IntegerField(write_only=True)
    spec3_id = serializers.IntegerField(write_only=True)
    product_type_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'price', 'product_description', 'product_type', 'spec1', 'spec2', 'spec3', 'product_type_id', 'spec1_id', 'spec2_id', 'spec3_id']


    def create(self, validated_data):
        logging.debug(validated_data)
        product_type_id = validated_data.pop('product_type_id')
        spec1_id = validated_data.pop('spec1_id')
        spec2_id = validated_data.pop('spec2_id')
        spec3_id = validated_data.pop('spec3_id')
        product_type = None
        spec1 = None
        spec2 = None
        spec3 = None
        try:
            product_type = ProductType.objects.get(product_type_id=int(product_type_id))
        except ProductType.DoesNotExist:
            error = {'message': f"Product Type with given id {int(product_type_id)} does not exists."}
            raise serializers.ValidationError(error)
        try:
            spec1 = ProductSpecification.objects.get(product_specification_id=int(spec1_id))
            spec2 = ProductSpecification.objects.get(product_specification_id=int(spec2_id))
            spec3 = ProductSpecification.objects.get(product_specification_id=int(spec3_id))
        except ProductSpecification.DoesNotExist:
            error = {'message': f"One of the given specification ids ({int(spec1_id)}, {int(spec2_id)} or {int(spec3_id)}) does not exists."}
            raise serializers.ValidationError(error)
        if product_type is None or spec1 is None or spec2 is None or spec3 is None:
            error = {'message': f"Unknown error occured while trying to create the product."}
            raise serializers.ValidationError(error)
        try:
            product = Product.objects.create(**validated_data, product_type=product_type, spec1=spec1, spec2=spec2, spec3=spec3)
            product.save()
            return product
        except IntegrityError:
            error = {'message': f"There is already product with the same type and specifications BUDDY."}
            raise serializers.ValidationError(error)
        




class StoreSerializer(serializers.ModelSerializer):
    employees = serializers.StringRelatedField(many=True, read_only=True)
    fired_employees = None
    inventory = None

    class Meta:
        model = Store
        fields = ('store_id', 'address', 'phone_number', 'employees', 'inventory', 'fired_employees')
        read_only_fields = ['fired_employees']


class StorageRackSerializer(serializers.ModelSerializer):
    fk_product = ProductSerializer(read_only=True)    
    fk_inventory  = None

    class Meta:
        model = StorageRack
        fields = ('storage_rack_id', 'quantity', 'fk_inventory', 'fk_product')


class InventorySerializer(serializers.ModelSerializer):
    fk_building = StoreSerializer()
    storage_racks = StorageRackSerializer(many=True)

    class Meta:
        model = Inventory
        fields = ('inventory_id', 'fk_building', 'storage_racks')

StoreSerializer.inventory = InventorySerializer()
StorageRackSerializer.fk_inventory = InventorySerializer()

class EmployeeSerializer(serializers.ModelSerializer):
    work_place = StoreSerializer(read_only=True)
    manager = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = (
            'employee_id',
            'ssn',
            'email',
            'gender',
            'date_of_birth',
            'first_name',
            'middle_name',
            'last_name',
            'address',
            'phone_number',
            'work_place',
            'manager')

class CustomerSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'email', 'shipping_address', 'phone_number', 'orders')
        # read_only_fields = ('orders')

class TransactionSerializer(serializers.ModelSerializer):
    fk_product = ProductSerializer(read_only=True)
    fk_order = None
    class Meta:
        model = Transaction  
        fields = '__all__'  

class OrderSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    fk_customer = CustomerSerializer(read_only=True)
    fk_store = StoreSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
TransactionSerializer.fk_order = OrderSerializer(read_only=True)

class FiredEmployeeSerializer(serializers.ModelSerializer):
    work_place = StoreSerializer(read_only=True)
    class Meta:
        model = FiredEmployee
        fields = '__all__'
StoreSerializer.fired_employees = FiredEmployeeSerializer(many=True, read_only=True)

class View1Serializer(serializers.ModelSerializer):
    class Meta:
        model = View1
        fields = '__all__'
        read_only_fields = [f.name for f in View1._meta.get_fields()]

class View2Serializer(serializers.ModelSerializer):
    class Meta:
        model = View2
        fields = '__all__'
        read_only_fields = [f.name for f in View2._meta.get_fields()]

class View3Serializer(serializers.ModelSerializer):
    class Meta:
        model = View3
        fields = '__all__'
        read_only_fields = [f.name for f in View3._meta.get_fields()]

class View4Serializer(serializers.ModelSerializer):
    class Meta:
        model = View4
        fields = '__all__'
        read_only_fields = [f.name for f in View4._meta.get_fields()]

class View5Serializer(serializers.ModelSerializer):
    class Meta:
        model = View5
        fields = '__all__'
        read_only_fields = [f.name for f in View5._meta.get_fields()]

class View8Serializer(serializers.ModelSerializer):
    class Meta:
        model = View8
        fields = '__all__'
        read_only_fields = [f.name for f in View8._meta.get_fields()]

class View9Serializer(serializers.ModelSerializer):
    class Meta:
        model = View9
        fields = '__all__'
        read_only_fields = [f.name for f in View9._meta.get_fields()]

class View10Serializer(serializers.ModelSerializer):
    class Meta:
        model = View10
        fields = '__all__'
        read_only_fields = [f.name for f in View10._meta.get_fields()]

class View11Serializer(serializers.ModelSerializer):
    class Meta:
        model = View11
        fields = '__all__'
        read_only_fields = [f.name for f in View11._meta.get_fields()]

class View12Serializer(serializers.ModelSerializer):
    class Meta:
        model = View12
        fields = '__all__'
        read_only_fields = [f.name for f in View12._meta.get_fields()]

class View13Serializer(serializers.ModelSerializer):
    class Meta:
        model = View13
        fields = '__all__'
        read_only_fields = [f.name for f in View13._meta.get_fields()]
