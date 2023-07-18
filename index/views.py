from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product


def home(request):
    data = Product.objects.all()

    context = {
        'data': data
    }
    return render(request, 'shop/profiles/home.html', context)



def about(request, id):
    data = Product.objects.get(id=id)
    contex = {
        'data': data
    }
    return render(request, 'shop/profiles/about.html', contex)
