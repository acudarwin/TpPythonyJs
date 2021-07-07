from django.urls import path
from . import views
app_name = 'ecommerce'
urlpatterns = [
    path('',views.home, name='Home'),
    path('category',views.category, name='Category'),
    path('about',views.about, name='About'),
    path('contact',views.contact, name='Contact'),
    path('newproduct',views.newproduct, name='Newproduct'),
    path('registro',views.registro, name='Registro'),
    path('products', views.products, name='products'),
]
