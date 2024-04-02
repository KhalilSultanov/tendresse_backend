from django.contrib import admin
from .models import Product, Manufacturer, Color, Size, Characteristic, Review, MainPhoto, Category, ContactForm, Blog, \
    SecondaryPhoto, BlogCharacteristic, MainBlogPhoto, SecondaryBlogPhoto
from decimal import Decimal


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1

class BlogCharacteristicInline(admin.TabularInline):
    model = BlogCharacteristic
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'new', 'popular', 'is_waiting')
    list_filter = ('new', 'popular', 'manufacturer', 'colors', 'sizes', 'categories')
    search_fields = ('name', 'full_name', 'description_full')
    filter_horizontal = ('colors', 'sizes', 'reviews', 'categories', 'manufacturer', 'main_photo', 'secondary_photo')
    inlines = [CharacteristicInline]

    def save_model(self, request, obj, form, change):
        if obj.price is not None:
            obj.price = obj.price - (obj.price * Decimal(obj.sale) / Decimal(100.0))
        super().save_model(request, obj, form, change)


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

@admin.register(MainPhoto)
class MainPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)
    search_fields = ('image',)

@admin.register(SecondaryPhoto)
class SecondaryPhotoAdmin(admin.ModelAdmin):
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

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at_display')
    search_fields = ('name', 'description', 'created_at')
    filter_horizontal = ('main_photo', 'secondary_photo')

    inlines = [BlogCharacteristicInline]

    @staticmethod
    def created_at_display(obj):
        return obj.created_at.strftime('%d.%m.%Y')

@admin.register(SecondaryBlogPhoto)
class SecondaryBlogPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)
    search_fields = ('image',)

@admin.register(MainBlogPhoto)
class MainBlogPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)
    search_fields = ('image',)

