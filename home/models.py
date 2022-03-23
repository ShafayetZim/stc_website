from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider')

    def __str__(self):
        return self.title


class ProductSlider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product-slider')

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.title


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Rotary Nickel Screen', 'Rotary Nickel Screen'),
        ('Flat Bed Screen', 'Flat Bed Screen'),
        ('Reactive Dyes', 'Reactive Dyes'),
        ('Auxiliaries', 'Auxiliaries'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,)
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
