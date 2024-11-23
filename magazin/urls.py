from django.urls import path
from magazin.views import *



urlpatterns = [
    path('', catalog ),
    path('product_ditail/<int:product_id>/', product_ditail),
    path('order/', order),
    path('create_order/<int:product_id>/', create_order),
]