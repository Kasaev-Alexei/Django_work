from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ProductView.as_view(), name='contacts'),
]
