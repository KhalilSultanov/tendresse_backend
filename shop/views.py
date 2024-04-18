import os

from django.db.models import Q, Func
from django.db.models.functions import Lower
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filter import ProductFilter
from .models import Product, Category, Blog, Review, Color
from .serializer import ProductSerializer, CategorySerializer, ContactFormSerializer, BlogSerializer, \
    MainPhotoBlogSerializer, SecondaryPhotoBlogSerializer, ReviewSerializer, ColorSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@api_view(['GET'])
def search_products(request):
    query = request.query_params.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(full_name__icontains=query) |
            Q(article__icontains=query) |
            Q(content1__icontains=query) |
            Q(content2__icontains=query)
        ).distinct()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response([])



@api_view(['GET'])
def product_by_id(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_photos(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'message': 'Товар не найден'}, status=404)

    main_photos = product.main_photo.all()
    secondary_photos = product.secondary_photo.all()

    main_photo_data = [{'id': photo.id, 'image': os.path.basename(photo.image.url)} for photo in main_photos]
    secondary_photo_data = [{'id': photo.id, 'image': os.path.basename(photo.image.url)} for photo in secondary_photos]

    response_data = {
        'main_photo': main_photo_data,
        'secondary_photos': secondary_photo_data
    }

    return Response(response_data)


@csrf_exempt
def contact_form_view(request):
    print(request.body)
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        serializer = ContactFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'Contact form submitted successfully.'}, status=201)
        else:
            return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed.'}, status=405)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset()

        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        manufacturer_id = self.request.query_params.get('manufacturer_id')
        color_id = self.request.query_params.get('color_id')
        size_id = self.request.query_params.get('size_id')

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        if manufacturer_id is not None:
            queryset = queryset.filter(manufacturer__id=manufacturer_id)
        if color_id is not None:
            queryset = queryset.filter(colors__id=color_id)
        if size_id is not None:
            queryset = queryset.filter(sizes__id=size_id)

        return queryset


@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def blog_photos(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response({'message': 'Блог не найден'}, status=404)

    main_photo = blog.main_photo.all()
    secondary_photos = blog.secondary_photo.all()

    main_serializer = MainPhotoBlogSerializer(main_photo, many=True, context={'request': request})
    secondary_serializer = SecondaryPhotoBlogSerializer(secondary_photos, many=True, context={'request': request})

    return Response({'main_photo': main_serializer.data, 'secondary_photos': secondary_serializer.data})


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def color_list(request):
    colors = Color.objects.all()
    serializer = ColorSerializer(colors, many=True)
    return Response(serializer.data)
