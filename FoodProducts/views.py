from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import FoodProduct
from .serializers import FoodProductSerializer


class ScannedProductView(APIView):
    def get(self, request, barcode):
        user_health_goal = request.query_params.get("health_goal")  # Optional health goal
        try:
            scanned_product = FoodProduct.objects.get(barcode=barcode)
            serialized_scanned = FoodProductSerializer(scanned_product)

            # Fetch related products
            related_products = FoodProduct.objects.filter(
                category=scanned_product.category
            ).exclude(barcode=scanned_product.barcode)

            # Filter based on health goal if provided
            if user_health_goal:
                related_products = related_products.filter(
                    benefits__has_key=user_health_goal
                )

            serialized_related = FoodProductSerializer(related_products, many=True)

            return Response({
                "scanned_product": serialized_scanned.data,
                "health_related_products": serialized_related.data
            }, status=status.HTTP_200_OK)
        except FoodProduct.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class FoodProductViewSet(viewsets.ModelViewSet):
    queryset = FoodProduct.objects.all()
    serializer_class = FoodProductSerializer

    # Custom actions
    @action(detail=False, methods=['get'], url_path='by-barcode')
    def fetch_by_barcode(self, request):
        barcode = request.query_params.get('barcode')
        if not barcode:
            return Response({"error": "Please provide a barcode."}, status=400)
        try:
            product = FoodProduct.objects.get(barcode=barcode)
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        except FoodProduct.DoesNotExist:
            return Response({"message": "No product found with this barcode."}, status=404)

    @action(detail=False, methods=['get'], url_path='by-name')
    def fetch_by_name(self, request):
        name = request.query_params.get('name')
        if not name:
            return Response({"error": "Please provide a product name."}, status=400)
        products = FoodProduct.objects.filter(name__icontains=name)
        if products.exists():
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response({"message": "No products found with this name."}, status=404)
