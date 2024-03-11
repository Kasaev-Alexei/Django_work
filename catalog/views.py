from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, Phone: {phone}, Message: {message}')
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    context = {'object': Product.objects.get(pk=pk)}

    return render(request, 'catalog/product_detail.html', context=context)


def product_list(request):
    context_data = {'object_list': Product.objects.all()}

    return render(request, 'catalog/product_list.html', context=context_data)
