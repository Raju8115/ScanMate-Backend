from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodProductViewSet, ScannedProductView

router = DefaultRouter()
router.register(r'products', FoodProductViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Handles CRUD and custom actions
    path('scanned/<str:barcode>/', ScannedProductView.as_view(), name='scanned_product'),  # For scanning and related logic
]
