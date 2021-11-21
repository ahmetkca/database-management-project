from django.urls import include, path
from rest_framework import routers
from api.views import EmployeeViewSet, StoreViewSet, InventoryViewSet, StorageRackViewSet, ProductSpecificationViewSet, ProductTypeViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'product-types', ProductTypeViewSet)
router.register(r'product-specifications', ProductSpecificationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'storage-racks', StorageRackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]