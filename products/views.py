from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .form.form import ProductForm
# Create your views here.


def index(req):
    if req.method == "POST":
        form = ProductForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("products:index")
        return render(req, "products/add.html", {"form": form})
    products = Product.objects.order_by("-id")
    return render(req, "products/index.html", {"products": products})


def add(req):
    form = ProductForm()
    return render(req, "products/add.html", {"form": form})


def each(req, id):
    product = get_object_or_404(Product, id=id)
    if req.method == "POST":
        form = ProductForm(req.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:each", id=id)
        return render(req, "products/edit.html", {"product": product, "form": form})
    return render(req, "products/each.html", {"product": product})


def edit(req, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    return render(req, "products/edit.html", {"product": product, "form": form})


def delete(req, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("products:index")
