from django.db import models
from ckeditor.fields import RichTextField


class Product(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=512, null=True, blank=True)
    article = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.ManyToManyField('Manufacturer', blank=True)
    details = models.TextField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    colors = models.ManyToManyField('Color', blank=True)
    sizes = models.ManyToManyField('Size', blank=True)
    quantity = models.PositiveIntegerField(default=0)
    description_full = RichTextField(default='')
    reviews = models.ManyToManyField('Review', blank=True)
    main_photo = models.ManyToManyField('MainPhoto', blank=True)
    secondary_photo = models.ManyToManyField('SecondaryPhoto', blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    sale = models.FloatField(default=0.0, null=True, blank=True)
    new = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_color = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=255, default="Anonymous")
    email = models.EmailField(default='Anon')
    rating = models.PositiveSmallIntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
    text = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.text[:50]}"

class MainPhoto(models.Model):
    image = models.ImageField(upload_to='/products_photos/main_photo', blank=True, null=True)

    def __str__(self):
        return self.image.name

class SecondaryPhoto(models.Model):
    image = models.ImageField(upload_to='/products_photos/secondary_photos', blank=True, null=True)

    def __str__(self):
        return self.image.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    preview_photo = models.ImageField(upload_to='/category_photos', blank=True, null=True)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    fullname = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=1000, blank=True, null=True)
    message = models.CharField(max_length=2000)


class MainBlogPhoto(models.Model):
    image = models.ImageField(upload_to='/blog_photos/main_photo/', blank=True, null=True)

    def __str__(self):
        return self.image.name

class SecondaryBlogPhoto(models.Model):
    image = models.ImageField(upload_to='/blog_photos/secondary_photos/', blank=True, null=True)

    def __str__(self):
        return self.image.name


class Blog(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=100)
    content1 = RichTextField(default='')
    content2 = RichTextField(default='')
    main_photo = models.ManyToManyField('MainBlogPhoto')
    secondary_photo = models.ManyToManyField('SecondaryBlogPhoto')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
