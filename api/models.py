from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    code = models.TextField()
    product_type = models.TextField()
    status = models.TextField()
