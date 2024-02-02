from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Product


@csrf_exempt
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)


@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        new_product_name = request.POST.get('new_product')

        if "  " not in new_product_name:
            Product.objects.create(name=new_product_name)

    products = Product.objects.all()
    context = {"products": products}
    return redirect('/')


@csrf_exempt
def delete_product(request, id):
    Product.objects.filter(id=id).delete()
    products = Product.objects.all()
    context = {"products": products}
    return redirect('/')


@csrf_exempt
def mark_product(request, id):
    modified_product = Product.objects.get(id=id)
    if modified_product.buyed == False:
        modified_product.buyed = True  # change field
    else:
        modified_product.buyed = False  # change field
    modified_product.save()  # this will update only
    products = Product.objects.all()
    context = {"products": products}
    return redirect('/')
