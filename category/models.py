from django.db import models



class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    cart_image = models.ImageField(upload_to='categories/photos')
   