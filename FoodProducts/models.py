from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class FoodProduct(models.Model):
    barcode = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image_url = models.URLField(max_length=500, blank=True, null=True)
    ingredients = models.JSONField(help_text="List of ingredients with effects on health")
    allergies = models.JSONField(help_text="Allergies associated with this product", blank=True, null=True)
    benefits = models.JSONField(help_text="Health benefits of this product", blank=True, null=True)
    flipkart_link = models.URLField(max_length=500, blank=True, null=True)
    amazon_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
