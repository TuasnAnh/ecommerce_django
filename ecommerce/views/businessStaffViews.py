from ecommerce.views.views import login
from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from ..models import Inventory, Order, Person, Product, User
from ..currentAuthen import authen


def business_homepage(request):
    if request.method == "GET":
        print(authen.username)
        if not authen.checkAuthen():
            return redirect("login")

        product = Product.objects.all()
        res = {"product": product}

        return render(request, "business/business-homepage.html", res)
