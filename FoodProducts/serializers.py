from rest_framework import serializers
from .models import FoodProduct, Category

class FoodProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category'
    )

    class Meta:
        model = FoodProduct
        fields = '__all__'


