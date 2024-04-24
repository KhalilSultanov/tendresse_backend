from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin

from shop.views import search_products, search_products_title_en, search_blogs_title_en, product_by_id, all_categories, \
    product_photos, \
    contact_form_view, \
    ProductList, get_blogs, blog_photos, review_list, color_list, size_list, manufacturer_list, get_blog_by_id, \
    categories_by_id
from tendresse_backend import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/search/', search_products, name='search'),
    path('api/search_products_title_en/', search_products_title_en, name='search_products_title_en'),
    path('api/search_blogs_title_en/', search_blogs_title_en, name='search_blogs_title_en'),
    path('api/product_by_id/<int:id>/', product_by_id, name='product_by_id'),
    path('api/all_categories/', all_categories, name='all_categories'),
    path('api/categories_by_id/<int:id>/', categories_by_id, name='categories_by_id'),
    path('api/product/<int:product_id>/photos/', product_photos, name='product_photos'),
    path('api/submit_contact_form/', contact_form_view, name='contact_form_view'),
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/blogs', get_blogs, name='get_blogs'),
    path('api/blog/<int:blog_id>/photos/', blog_photos, name='get_blogs'),
    path('api/reviews/', review_list, name='review_list'),
    path('api/colors/', color_list, name='color_list'),
    path('api/sizes/', size_list, name='size_list'),
    path('api/manufacturers/', manufacturer_list, name='manufacturer_list'),
    path('api/blog_by_id/<int:id>', get_blog_by_id, name='get_blog_by_id'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

