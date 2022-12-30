from django.db import models

# Create your models here.
class Vegitables(models.Model):
    Item=models.CharField(max_length=50,unique=True)
    Price=models.FloatField()
    Status=models.CharField(max_length=12)
    Veg_image=models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.Item