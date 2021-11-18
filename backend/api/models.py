from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class ProductType(models.Model):
    product_type_id     = models.AutoField(primary_key=True)
    product_type_name   = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class ProductSpecification(models.Model):
    product_specification_id    = models.AutoField(primary_key=True)
    product_specification_name  = models.CharField(max_length=50)
    product_specification_value = models.CharField(max_length=50)
    fk_product_type_id          = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        unique_together = (('product_name', 'spec1', 'spec2', 'spec3', 'product_description'), )
    product_id          = models.AutoField(primary_key=True)
    product_name        = models.CharField(max_length=50)
    price               = models.DecimalField(max_digits=15, decimal_places=2)
    product_description = models.CharField(max_length=250, default="N/A")
    fk_product_type_id  = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    spec1               = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE, related_name="spec1")
    spec2               = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE, related_name="spec2")
    spec3               = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE, related_name="spec3")
    def __str__(self):
        return self.name

class Store(models.Model):
    store_id        = models.AutoField(primary_key=True)
    address         = models.CharField(max_length=250, unique=True)
    phone_number    = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.name

class Inventory(models.Model):
    inventory_id    = models.AutoField(primary_key=True)
    fk_building     = models.OneToOneField(Store, on_delete=models.CASCADE, unique=True)
    def __str__(self):
        return self.name

class StorageRack(models.Model):
    storage_rack_id = models.AutoField(primary_key=True)
    quantity        = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
    fk_inventory    = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    fk_product_id   = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

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
    work_place      = models.ForeignKey(Store, on_delete=models.CASCADE)
    manager_id      = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class FiredEmployee(models.Model):
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
    work_place      = models.ForeignKey(Store, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class Customer(models.Model):
    customer_id     = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length=50)
    middle_name     = models.CharField(max_length=50, null=True)
    last_name       = models.CharField(max_length=50)
    date_of_birth   = models.DateField(null=True)
    gender          = models.CharField(max_length=10, choices=Gender.choices)
    email           = models.EmailField(unique=True)
    address         = models.CharField(max_length=250)
    phone_number    = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    order_id        = models.AutoField(primary_key=True)
    ordered_at      = models.DateTimeField(auto_now_add=True)
    fk_customer_id  = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    fk_store_id     = models.ForeignKey(Store, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_id  = models.AutoField(primary_key=True)
    quantity        = models.IntegerField()
    fk_product_id   = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    fk_order_id     = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name
