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
from django.urls import path
from django.contrib import admin

from shop.views import search_products, product_by_id, all_categories, product_photos, contact_form_view, \
    ProductList, get_blogs, blog_photos, review_list, color_list, size_list, manufacturer_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_products, name='search'),
    path('product_by_id/<int:id>/', product_by_id, name='product_by_id'),
    path('all_categories/', all_categories, name='all_categories'),
    path('product/<int:product_id>/photos/', product_photos, name='product_photos'),
    path('submit_contact_form/', contact_form_view, name='contact_form_view'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('blogs', get_blogs, name='get_blogs'),
    path('blog/<int:blog_id>/photos/', blog_photos, name='get_blogs'),
    path('reviews/', review_list, name='review_list'),
    path('colors/', color_list, name='color_list'),
    path('sizes/', size_list, name='size_list'),
    path('manufacturers/', manufacturer_list, name='manufacturer_list'),



]

