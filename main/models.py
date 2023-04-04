from django.db import models
    
class users(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.JSONField(null=True, blank=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

class Product(models.Model):
    id = models.IntegerField(primary_key=True)



