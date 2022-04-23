from django.db import models

# Create your models here.
class Product(models.Model):
    P_image=models.ImageField(default='')
    P_price=models.FloatField()
    P_name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.P_image},{self.P_price},{self.P_name}"