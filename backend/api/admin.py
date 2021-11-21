from django.contrib import admin
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

admin.site.register(Order)
admin.site.register(Transaction)
admin.site.register(Store)
admin.site.register(StorageRack)
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(ProductSpecification)
admin.site.register(ProductType)
