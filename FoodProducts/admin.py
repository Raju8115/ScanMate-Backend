from django.contrib import admin
from .models import Category, FoodProduct

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(FoodProduct)
class FoodProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'category')
    search_fields = ('name', 'barcode', 'category__name')
