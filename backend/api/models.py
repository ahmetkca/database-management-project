from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class ProductType(models.Model):
    product_type_id     = models.AutoField(primary_key=True)
    product_type_name   = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.product_type_name

class ProductSpecification(models.Model):
    product_specification_id    = models.AutoField(primary_key=True)
    product_specification_name  = models.CharField(max_length=50)
    product_specification_value = models.CharField(max_length=50)
    product_type                = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="specifications")
    def __str__(self):
        return f"{self.product_specification_id},{self.product_specification_name},{self.product_specification_value}"

class Product(models.Model):
    class Meta:
        
        unique_together = (('product_name', 'spec1', 'spec2', 'spec3', 'product_description'), )
        verbose_name_plural = "Products"
    product_id          = models.AutoField(primary_key=True)
    product_type        = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products', null=True)
    product_name        = models.CharField(max_length=50)
    spec1               = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE, related_name="primary_products")
    spec2               = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE, related_name="secondary_products")
    spec3               = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE, related_name="tertiary_products")
    price               = models.DecimalField(max_digits=15, decimal_places=2)
    product_description = models.CharField(max_length=250, default="N/A")
    
    def __str__(self):
        return self.product_name

class Store(models.Model):
    store_id        = models.AutoField(primary_key=True)
    # store_name      = models.CharField(max_length=50, unique=True)
    address         = models.CharField(max_length=250, unique=True)
    phone_number    = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return f"{self.store_id}"

class Inventory(models.Model):
    inventory_id    = models.AutoField(primary_key=True)
    fk_building     = models.OneToOneField(Store, on_delete=models.CASCADE, unique=True, related_name='inventory')
    def __str__(self):
        return f"{self.inventory_id}"

class StorageRack(models.Model):
    storage_rack_id = models.AutoField(primary_key=True)
    fk_product   = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="storage_racks")
    # location_name   = models.CharField(max_length=10)
    quantity        = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
    fk_inventory    = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="storage_racks")
    
    def __str__(self):
        return f"{self.storage_rack_id}"

class Gender(models.TextChoices):
    MALE    = "Male"
    FEMALE  = "Female"
    OTHER   = "Other"

class Employee(models.Model):
    employee_id     = models.AutoField(primary_key=True)
    ssn             = models.IntegerField(unique=True)
    email           = models.EmailField(unique=True)
    gender          = models.CharField(max_length=10, choices=Gender.choices)
    date_of_birth   = models.DateField(null=True)
    first_name      = models.CharField(max_length=50)
    middle_name     = models.CharField(max_length=50, null=True)
    last_name       = models.CharField(max_length=50)
    address         = models.CharField(max_length=250)
    phone_number    = models.CharField(max_length=15, unique=True)
    work_place      = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="employees")
    manager         = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name="employees")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FiredEmployee(models.Model):
    employee_id     = models.AutoField(primary_key=True)
    ssn             = models.IntegerField(unique=True)
    email           = models.EmailField(unique=True)
    gender          = models.CharField(max_length=10, choices=Gender.choices)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    work_place      = models.ForeignKey(Store, on_delete=models.DO_NOTHING, related_name="fired_employees")
    address         = models.CharField(max_length=250)
    phone_number    = models.CharField(max_length=15, unique=True)
    date_of_birth   = models.DateField(null=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    customer_id     = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length=50)
    middle_name     = models.CharField(max_length=50, null=True)
    last_name       = models.CharField(max_length=50)
    date_of_birth   = models.DateField(null=True)
    gender          = models.CharField(max_length=10, choices=Gender.choices)
    email                    = models.EmailField(unique=True)
    shipping_address         = models.CharField(max_length=250)
    phone_number    = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    order_id        = models.AutoField(primary_key=True)
    ordered_at      = models.DateTimeField(auto_now_add=True)
    fk_customer  = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    fk_store     = models.ForeignKey(Store, on_delete=models.DO_NOTHING, related_name='orders')
    def __str__(self):
        return f"{self.order_id}"

class Transaction(models.Model):
    transaction_id  = models.AutoField(primary_key=True)
    quantity        = models.IntegerField()
    fk_product   = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='transactionbs')
    fk_order     = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    def __str__(self):
        return f"{self.transaction_id}"

class View1(models.Model):
    product_id = models.IntegerField(primary_key=True, db_column='Product ID')
    product_name = models.CharField(max_length=50, db_column="Product Name")
    product_description = models.CharField(max_length=250, db_column='Product Description')
    price = models.DecimalField(max_digits=15, decimal_places=2, db_column='Price')
    spec1_name = models.CharField(max_length=50, db_column='Specification 1')
    spec1_value = models.CharField(max_length=50, db_column='Specification 1 Value')
    spec2_name = models.CharField(max_length=50, db_column='Specification 2')
    spec2_value = models.CharField(max_length=50, db_column='Specification 2 Value')
    spec3_name = models.CharField(max_length=50, db_column='Specification 3')
    spec3_value = models.CharField(max_length=50, db_column='Specification 3 Value')
    product_type = models.CharField(max_length=50, db_column='Product Type')

    class Meta:
        managed = False
        db_table = "view1"

class View2(models.Model):
    product_type = models.CharField(max_length=50, primary_key=True, db_column='Product Type')
    number_of_products = models.BigIntegerField(db_column='Number of Products')

    class Meta:
        managed = False
        db_table = 'view2'

class View3(models.Model):
    employee_id = models.IntegerField(primary_key=True, db_column='Employee ID')
    first_name = models.CharField(max_length=50, db_column='First Name')
    last_name = models.CharField(max_length=50, db_column='Last Name')
    date_of_birth = models.DateField(db_column='Date of Birth')
    work_place = models.IntegerField(db_column='Works in Store with id:')

    class Meta:
        managed = False
        db_table = 'view3'

class View4(models.Model):
    order_id = models.IntegerField(primary_key=True, db_column='Order ID')
    first_name = models.CharField(max_length=50, db_column='First Name')
    last_name = models.CharField(max_length=50, db_column='Last Name')
    class Meta:
        managed = False
        db_table = "view4"

class View5(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    ssn = models.IntegerField()
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    work_place_id = models.IntegerField()
    address = models.CharField(max_length=250)
    date_of_birth = models.DateField()

    class Meta:
        managed = False
        db_table = "view5"


class BaseAllProductsByTypeModel(models.Model):
    product_id = models.IntegerField(primary_key=True, db_column="Product id")
    product_name = models.CharField(max_length=50, db_column="Product Name")
    product_description = models.CharField(max_length=250, db_column='Product Description')
    price = models.DecimalField(max_digits=15, decimal_places=2, db_column='Price')
    spec1_name = models.CharField(max_length=50, db_column='Specification 1')
    spec1_value = models.CharField(max_length=50, db_column='Specification 1 Value')
    spec2_name = models.CharField(max_length=50, db_column='Specification 2')
    spec2_value = models.CharField(max_length=50, db_column='Specification 2 Value')
    spec3_name = models.CharField(max_length=50, db_column='Specification 3')
    spec3_value = models.CharField(max_length=50, db_column='Specification 3 Value')

    class Meta:
        abstract = True
        managed = False

class View8(BaseAllProductsByTypeModel):
    class Meta:
        managed = False
        db_table = "view8"

class View9(BaseAllProductsByTypeModel):
    class Meta:
        managed = False
        db_table = "view9"

class View10(BaseAllProductsByTypeModel):
    class Meta:
        managed = False
        db_table = "view10"

class View11(BaseAllProductsByTypeModel):
    class Meta:
        managed = False
        db_table = "view11"

class View12(BaseAllProductsByTypeModel):
    class Meta:
        managed = False
        db_table = "view12"

class View13(BaseAllProductsByTypeModel):
    class Meta:
        managed = False
        db_table = "view13"