from django.urls import include, path
from rest_framework import routers
from api.views import (
    View10ViewSet, 
    View11ViewSet, 
    View12ViewSet, 
    View13ViewSet, 
    View1ViewSet, 
    CustomerViewSet, 
    FiredEmployeeViewSet, 
    TransactionViewSet, 
    OrderViewSet, 
    EmployeeViewSet, 
    StoreViewSet, 
    InventoryViewSet, 
    StorageRackViewSet, 
    ProductSpecificationViewSet, 
    ProductTypeViewSet, 
    ProductViewSet, 
    View2ViewSet, 
    View3ViewSet, 
    View4ViewSet, 
    View5ViewSet, 
    View8ViewSet, 
    View9ViewSet
)

router = routers.DefaultRouter()
router.register(r'product-types', ProductTypeViewSet)
router.register(r'product-specifications', ProductSpecificationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'storage-racks', StorageRackViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'fired-employees', FiredEmployeeViewSet)
router.register(r'view1', View1ViewSet)
router.register(r'view2', View2ViewSet)
router.register(r'view3', View3ViewSet)
router.register(r'view4', View4ViewSet)
router.register(r'view5', View5ViewSet)
router.register(r'view8', View8ViewSet)
router.register(r'view9', View9ViewSet)
router.register(r'view10', View10ViewSet)
router.register(r'view11', View11ViewSet)
router.register(r'view12', View12ViewSet)
router.register(r'view13', View13ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]