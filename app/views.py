from django.shortcuts import render
from .models import Product
# Create your views here.
def show(request):
    product=Product.objects.all()
    return render(request, 'apptemp/index.html',{"product":product})