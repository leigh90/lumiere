from django.forms import ModelForm
from .models import Image
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_name','image_location', 'image_category']