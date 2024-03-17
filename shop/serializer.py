from rest_framework import serializers
from .models import Product, Photo, Category, Color, Size, Review, Characteristic


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'text']

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['name', 'value']

class ProductSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    sizes = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    characteristics = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_photos(self, obj):
        return [photo.image.url for photo in obj.photos.all()]

    def get_categories(self, obj):
        return [category.name for category in obj.categories.all()]

    def get_colors(self, obj):
        return [color.name for color in obj.colors.all()]

    def get_sizes(self, obj):
        return [size.name for size in obj.sizes.all()]

    def get_reviews(self, obj):
        return ReviewSerializer(obj.reviews.all(), many=True).data

    def get_characteristics(self, obj):
        return CharacteristicSerializer(obj.characteristics.all(), many=True).data
