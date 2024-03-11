from django.urls import path

from catalog.views import contacts, product_detail, product_list, index

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts),
    path('<int:pk>/', product_detail, name="product_detail"),
    path('product_list/', product_list, name='product_list'),
]
