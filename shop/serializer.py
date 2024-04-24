from rest_framework import serializers
from .models import (Product, MainPhoto, Category, Review, ContactForm, Manufacturer, Blog,
                     SecondaryPhoto,
                     MainBlogPhoto, SecondaryBlogPhoto, Color, Size)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'email', 'rating', 'text']

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    main_photo = serializers.SerializerMethodField()
    secondary_photo = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    sizes = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    manufacturer = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    @staticmethod
    def get_main_photo(obj):
        return [photo.image.url for photo in obj.main_photo.all()]

    @staticmethod
    def get_secondary_photo(obj):
        return [photo.image.url for photo in obj.secondary_photo.all()]

    @staticmethod
    def get_categories(obj):
        return [{'id': category.id} for category in obj.categories.all()]

    @staticmethod
    def get_colors(obj):
        return [{'id': color.id, 'name': color.name, 'hex_color': color.hex_color} for color in obj.colors.all()]

    @staticmethod
    def get_sizes(obj):
        return [size.name for size in obj.sizes.all()]

    @staticmethod
    def get_reviews(obj):
        return [{'id': review.id} for review in obj.reviews.all()]

    @staticmethod
    def get_manufacturer(obj):
        manufacturer_instance = obj.manufacturer.first()
        if manufacturer_instance:
            return manufacturer_instance.name
        return None

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

    @staticmethod
    def get_manufacturer(obj):
        manufacturer_instance = obj.manufacturer.first()
        if manufacturer_instance:
            return manufacturer_instance.name
        return None
class CategorySerializer(serializers.ModelSerializer):
    preview_photo = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    @staticmethod
    def get_preview_photo(obj):
        return obj.preview_photo.url if obj.preview_photo else None

class MainPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPhoto
        fields = '__all__'

class SecondaryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryPhoto
        fields = '__all__'

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'

class MainPhotoBlogSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = MainBlogPhoto
        fields = ['image']

    @staticmethod
    def get_image(obj):
        return obj.image.url if obj.image else None

class SecondaryPhotoBlogSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SecondaryBlogPhoto
        fields = ['image']

    @staticmethod
    def get_image(obj):
        return obj.image.url if obj.image else None

class BlogSerializer(serializers.ModelSerializer):
    main_photo = serializers.SerializerMethodField()
    secondary_photo = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Blog
        fields = ['id', 'created_at', 'name', 'title_en', 'description', 'content1', 'content2', 'main_photo', 'secondary_photo']

    @staticmethod
    def get_main_photo(obj):
        return [photo.image.url for photo in obj.main_photo.all()]

    @staticmethod
    def get_secondary_photo(obj):
        return [photo.image.url for photo in obj.secondary_photo.all()]


