from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

app_name = 'mainapp'
urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('categories/', views.product_list, name='product_list'),
    path('search/', views.post_search, name='post_search'),
    path('about/', views.about, name='about'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)