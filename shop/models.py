from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=512, null=True, blank=True)
    article = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.ManyToManyField('Manufacturer', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    colors = models.ManyToManyField('Color', blank=True)
    sizes = models.ManyToManyField('Size', blank=True)
    quantity = models.PositiveIntegerField(default=0)
    description_full = models.TextField(null=True, blank=True)
    reviews = models.ManyToManyField('Review', blank=True)
    photos = models.ManyToManyField('Photo', blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    sale = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    new = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    is_waiting = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Characteristic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')
    name = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.value}"

class Review(models.Model):
    name = models.CharField(max_length=255, default="Anonymous")
    email = models.EmailField(default='Anon')
    rating = models.PositiveSmallIntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
    text = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.text[:50]}"

class Photo(models.Model):
    image = models.ImageField(upload_to='static')

    def __str__(self):
        return self.image.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    fullname = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=1000, blank=True, null=True)
    message = models.CharField(max_length=2000)
