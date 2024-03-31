from rest_framework import serializers
from .models import Product, Photo, Category, Review, Characteristic, ContactForm, Manufacturer


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'text']

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['name', 'value']

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    sizes = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    characteristics = serializers.SerializerMethodField()
    manufacturer = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = '__all__'

    @staticmethod
    def get_photos(obj):
        return [photo.image.url for photo in obj.photos.all()]

    @staticmethod
    def get_categories(obj):
        return [category.name for category in obj.categories.all()]

    @staticmethod
    def get_colors(obj):
        return [color.name for color in obj.colors.all()]

    @staticmethod
    def get_sizes(obj):
        return [size.name for size in obj.sizes.all()]

    @staticmethod
    def get_reviews(obj):
        return ReviewSerializer(obj.reviews.all(), many=True).data

    @staticmethod
    def get_characteristics(obj):
        return CharacteristicSerializer(obj.characteristics.all(), many=True).data

    @staticmethod
    def get_manufacturer(obj):
        manufacturer_instance = obj.manufacturer.first()
        if manufacturer_instance:
            return manufacturer_instance.name
        return None

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'

