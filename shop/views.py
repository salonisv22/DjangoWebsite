from django.shortcuts import render
from .models import Product,Order,Contact
from math import ceil
import logging
# Create your views here.
from django.http import HttpResponse


def index(request):

    all_products = []
    category_of_products = Product.objects.values('category','id')
    category_list = {item['category'] for item in category_of_products}
    for each_category in category_list:
        product_of_category = Product.objects.filter(category=each_category)
        n = len(product_of_category)
        n_slides = ceil(n / 4)
        all_products.append([product_of_category,range(1,n_slides),n_slides])

    params = {'product_list':all_products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    sent = False
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        msg = Contact(name=name,email=email,phone=phone,desc=desc)
        msg.save()
        sent = True
    return render(request, 'shop/contact.html',{'sent':sent})


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/productView.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_JSON = request.POST.get('itemsJSON','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('add1','')+request.POST.get('add2','')
        phone = request.POST.get('phone','')
        city= request.POST.get('city', '')
        state= request.POST.get('state', '')
        pin_code = request.POST.get('pin_code','')

        order = Order(name=name,email=email,address=address,phone=phone,state=state,city=city,pin_code=pin_code,
                      items_JSON=items_JSON)
        order.save()
        o_id = order.order_id
        thank = True
        return render(request, 'shop/checkout.html',{'thank':thank,'id':o_id})
    return render(request, 'shop/checkout.html')
