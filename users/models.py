from django.db import models

class User(models.Model):
    userId = models.CharField(max_length=50, unique=True) # Mandatory
    name = models.CharField(max_length=100)  # Mandatory
    email = models.EmailField(unique=True)   # Mandatory
    mobile = models.CharField(max_length=15)  # Mandatory
    healthInfoFilled = models.BooleanField(default=False, blank=True)
    Gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    HeightFeet = models.IntegerField(blank=True, null=True)  # Optional
    HeightInch = models.IntegerField(blank=True, null=True)  # Optional
    Weight = models.FloatField(blank=True, null=True)  # Optional
    DOB = models.CharField(max_length=30, blank=True, null=True)  # Optional
    ActivityLevel = models.CharField(max_length=50, blank=True)
    dietery_preference = models.CharField(max_length=100, blank=True)
    dietery_goal = models.CharField(max_length=100, blank=True)
    allergies = models.JSONField(default=list, blank=True)  # Optional
    health_conditions = models.JSONField(default=list, blank=True)  # Optional

    def __str__(self):
        return self.name
