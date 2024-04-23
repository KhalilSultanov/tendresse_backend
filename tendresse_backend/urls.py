"""
URL configuration for tendresse_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin

from shop.views import search_products,search_products_title_en, product_by_id, all_categories, product_photos, contact_form_view, \
    ProductList, get_blogs, blog_photos, review_list, color_list, size_list, manufacturer_list
from tendresse_backend import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/search/', search_products, name='search'),
    path('api/search_title_en/', search_products_title_en, name='search_title_en'),
    path('api/product_by_id/<int:id>/', product_by_id, name='product_by_id'),
    path('api/all_categories/', all_categories, name='all_categories'),
    path('api/product/<int:product_id>/photos/', product_photos, name='product_photos'),
    path('api/submit_contact_form/', contact_form_view, name='contact_form_view'),
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/blogs', get_blogs, name='get_blogs'),
    path('api/blog/<int:blog_id>/photos/', blog_photos, name='get_blogs'),
    path('api/reviews/', review_list, name='review_list'),
    path('api/colors/', color_list, name='color_list'),
    path('api/sizes/', size_list, name='size_list'),
    path('api/manufacturers/', manufacturer_list, name='manufacturer_list'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

