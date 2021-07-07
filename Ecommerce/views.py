from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import *
from .models import Category, Product, Cart
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'ecommerce/home.html')

def products(request):
    if "ultimosProductos" not in request.session:
        request.session["ultimosProductos"] = []
    return render(request,"ecommerce/home.html", {
        "lista_productos": Product.objects.all(),
        "ultimosProductos": request.session["ultimosProductos"],
    })

def categories(request, category_id):
    un_category = get_object_or_404(Category, id=category_id)
    return render(request, "ecommerce/category.html", {
        "category": un_category
    })

def category(request):
    return render(request, 'ecommerce/category.html')

def about(request):
    return render(request, 'ecommerce/about.html')

def contact(request):
    return render(request, 'ecommerce/contact.html')

def newproduct(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormProduct(request.POST, request.FILES, instance=Product(imagen=request.FILES['imagen'], publicador=user))       
        if form.is_valid():
            form.save()
            return redirect("ecommerce:home")          
    else:
        form = FormProduct(initial={'category'})
        return render(request, "ecommerce/newproduct.html", {
            "form": form
        })    

def registro(request):
    return render(request, 'ecommerce/registro.html')

@login_required
def ultimosProductos(request, product_id):
    un_product = get_object_or_404(Product, id=product_id)
    for id in request.session["leer_mas_tarde"]:
        if id == product_id:
            #existe el producto
            return HttpResponseRedirect(reverse("ecommerce:producto", args=(un_product.id,)))            
    request.session["ultimosProductos"] += [product_id]
    return HttpResponseRedirect(reverse("ecommerce:producto", args=(un_product.id,)))  