from logging import getLogger

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import ProductForm, RawProductForm
from .models import *

logger = getLogger(__name__)


# Create your views here.

def product_details_view(request, *args, **kwargs):
    obj = Product.objects.all()
    context = {"products": obj}
    return render(request, "product_details.html", context)


def product_create_view(request, *args, **kwargs):
    initial_data = {'title': 'P_123', 'description': '123', 'price': 123.94,
                    'summary': 'Default Summary !!!123', 'featured': False}
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        logger.info({
            "data": form.cleaned_data
        })
        obj = Product.objects.filter(title=form.cleaned_data.get("title")).first()
        if obj:
            form.instance.id = obj.id
        form.save()
    context = {"form": form}
    return render(request, "product_create.html", context)


def product_create_raw_view(request, *args, **kwargs):
    p_form = RawProductForm()
    if request.method == "POST":
        p_form = RawProductForm(request.POST)
        if p_form.is_valid():
            logger.info({
                "data": p_form.cleaned_data
            })
            p1 = Product.objects.create(**p_form.cleaned_data)
            logger.info(f"Created Product with Title {p1.title} and Description {p1.description} for price {p1.price}")
        else:
            logger.critical({
                "errors": p_form.errors
            })

    context = {"form": p_form}
    return render(request, "product_create.html", context)


def product_dynamic_lookup_view(request, pid, *args, **kwargs):
    obj = get_object_or_404(Product, id=pid)
    # try:
    #     obj = Product.objects.get(id=pid)
    # except Product.DoesNotExist:
    #     raise Http404("Product does not exist.")
    # obj = Product.objects.filter(id=pid).first()
    context = {"products": (obj,)}
    return render(request, "product_details.html", context)


def product_delete_view(request, pid, *args, **kwargs):

    obj = get_object_or_404(Product, id=pid)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse("prd_det_view"))
    # try:
    #     obj = Product.objects.get(id=pid)
    # except Product.DoesNotExist:
    #     raise Http404("Product does not exist.")
    # obj = Product.objects.filter(id=pid).first()
    context = {"product": obj}
    return render(request, "product_delete.html", context)
