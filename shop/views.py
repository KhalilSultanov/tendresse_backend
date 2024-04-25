import os

from django.db.models import Q, Func
from django.db.models.functions import Lower
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .filter import ProductFilter
from .models import Product, Category, Blog, Review, Color, Size, Manufacturer
from .serializer import ProductSerializer, CategorySerializer, ContactFormSerializer, BlogSerializer, \
    MainPhotoBlogSerializer, SecondaryPhotoBlogSerializer, ReviewSerializer, ColorSerializer, ManufacturerSerializer, \
    SizeSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@api_view(['GET'])
def search_products(request):
    query = request.query_params.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__iregex=query)
        ).distinct()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response([])

@api_view(['GET'])
def search_products_title_en(request):
    query = request.query_params.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(title_en__icontains=query) |
            Q(title_en__contains=query)
        ).distinct()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response([])


@api_view(['GET'])
def categories_by_id(request, id):
    try:
        category = Category.objects.get(pk=id)
        products = category.product_set.all()
        data = [{'id': product.id, 'name': product.name} for product in products]
        return Response(data)
    except Category.DoesNotExist:
        return Response({'message': 'Категория не найдена'}, status=404)


@api_view(['GET'])
def search_blogs_title_en(request):
    query = request.query_params.get('q', '')
    if query:
        blogs = Blog.objects.filter(
            Q(title_en__icontains=query) |
            Q(title_en__contains=query)
        ).distinct()
        serializer = BlogSerializer(blogs, many=True)
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
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.query_params.get('category_name')

        if category_name:
            queryset = queryset.filter(categories__name__icontains=category_name)

        return queryset

@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_blog_by_id(request, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        return Response(status=404)

    serializer = BlogSerializer(blog)
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

@api_view(['GET'])
def size_list(request):
    sizes = Size.objects.all()
    serializer = SizeSerializer(sizes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def manufacturer_list(request):
    manufacturer = Manufacturer.objects.all()
    serializer = ManufacturerSerializer(manufacturer, many=True)
    return Response(serializer.data)