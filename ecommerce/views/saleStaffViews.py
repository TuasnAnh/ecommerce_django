from ecommerce.views.views import login
from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from ..models import Inventory, Order, Person, User
from ..currentAuthen import authen


def sale_homepage(request):
    if request.method == "GET":
        print(authen.username)
        if not authen.checkAuthen():
            return redirect("login")

        order = Order.objects.all()
        res = {"order": order}

        return render(request, "sale/sale-homepage.html", res)
