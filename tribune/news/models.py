from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.uploader
# Create your models here.

class Location(models.Model):
    LOCATION_CHOICES = (
        ('Nairobi','Kenya'),
        ('Kuala Lumpur', 'Malaysia'),
        ('Cape Town', 'South Africa'),
    )
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)

class Category(models.Model):
    CATEGORY_CHOICES =(
        ('Food', 'Food'),
        ('People','People'),
        ('Travel','Travel'),
        ('Architecture','Architecture'),
    )
    category_name = models.CharField(max_length=30,choices=CATEGORY_CHOICES)



class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=100)
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE,)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE,)
