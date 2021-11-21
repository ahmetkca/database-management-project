from re import L
from rest_framework import fields, serializers
from api.models import (
    Order, 
    Transaction, 
    Store, 
    StorageRack,
    Inventory,
    Customer,
    Employee,
    Product,
    ProductSpecification,
    ProductType
    )





class ProductTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductType
        fields = ['product_type_id', 'product_type_name']


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

    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'price', 'product_description', 'product_type', 'spec1', 'spec2', 'spec3']





class StoreSerializer(serializers.ModelSerializer):
    employees = serializers.StringRelatedField(many=True, read_only=True)
    inventory = None

    class Meta:
        model = Store
        fields = ('store_id', 'address', 'phone_number', 'employees', 'inventory')


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
