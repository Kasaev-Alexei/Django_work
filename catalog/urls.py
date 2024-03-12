from django.urls import path

from catalog.views import contacts, product_detail, product_list, index

app_name = 'catalog'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name="product_detail"),
    path('contacts/', contacts),
]
