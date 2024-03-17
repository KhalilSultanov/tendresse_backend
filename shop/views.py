from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer

@api_view(['GET'])
def search_products(request):
    query = request.query_params.get('q', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(full_name__icontains=query) |
            Q(article__icontains=query) |
            Q(description_full__icontains=query) |
            Q(name__contains=query) |
            Q(full_name__contains=query) |
            Q(article__contains=query) |
            Q(description_full__contains=query)
        ).distinct()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response([])
