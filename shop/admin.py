from django.contrib import admin
from .models import Product, Manufacturer, Color, Size, Characteristic, Review, Photo, Category, ContactForm

class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'new', 'popular', 'is_waiting')
    list_filter = ('new', 'popular', 'manufacturer', 'colors', 'sizes', 'categories')
    search_fields = ('name', 'full_name', 'description_full')
    filter_horizontal = ('colors', 'sizes', 'reviews', 'categories', 'manufacturer', 'photos')
    inlines = [CharacteristicInline]

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Characteristic)
class CharacteristicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'name', 'email', 'rating')
    search_fields = ('text', 'name', 'email')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)
    search_fields = ('image',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone_number', 'email', 'message')
    search_fields = ('fullname', 'phone_number', 'email', 'message')
