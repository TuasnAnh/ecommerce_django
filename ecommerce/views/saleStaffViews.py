from datetime import date, datetime
from ecommerce.views.views import login
from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from ..models import Cart, Cartitem, Inventory, Order, Person, Product, User
from ..currentAuthen import authen


def sale_homepage(request):
    if request.method == "GET":

        order = Order.objects.filter(status=1)

        for item in order:
            cart = Cart.objects.get(id=item.cart_id.id)
            cartItem = Cartitem.objects.filter(cart_id=cart.id)
            for item2 in cartItem:
                product = item2.product_id
                price = product.price
                sale = product.sale
                salePrice = price * sale / 100
                item2.product_id.salePrice = round(salePrice)
            item.cartItem = cartItem

        res = {"order": order}

        return render(request, "sale/sale-homepage.html", res)


def delivering(request):
    if request.method == "GET":

        order = Order.objects.filter(status=2)

        for item in order:
            cart = Cart.objects.get(id=item.cart_id.id)
            cartItem = Cartitem.objects.filter(cart_id=cart.id)
            for item2 in cartItem:
                product = item2.product_id
                price = product.price
                sale = product.sale
                salePrice = price * sale / 100
                item2.product_id.salePrice = round(salePrice)
            item.cartItem = cartItem

        res = {"order": order}

        return render(request, "sale/sale-delivering.html", res)


def success(request):
    if request.method == "GET":

        order = Order.objects.filter(status=3)

        for item in order:
            cart = Cart.objects.get(id=item.cart_id.id)
            cartItem = Cartitem.objects.filter(cart_id=cart.id)
            for item2 in cartItem:
                product = item2.product_id
                price = product.price
                sale = product.sale
                salePrice = price * sale / 100
                item2.product_id.salePrice = round(salePrice)
            item.cartItem = cartItem

        res = {"order": order}

        return render(request, "sale/sale-done.html", res)


def confirmOrder(request):
    if request.method == "GET":
        id = request.GET.get("id")
        order = Order.objects.get(id=id)
        order.status = 2
        order.created_time = datetime.now()
        order.save()

        # update quantity of product and inventory
        carItem = Cartitem.objects.filter(cart_id=Cart.objects.get(id=order.cart_id.id).id)
        print(len(carItem))
        for item in carItem:
            print(item.product_id.inventory_id.id)
            inventory_id = item.product_id.inventory_id.id
            product = Product.objects.get(inventory_id=inventory_id)
            product.quantity = product.quantity - item.quantity
            product.save()

            inventory = Inventory.objects.get(id=inventory_id)
            inventory.quantity = inventory.quantity - item.quantity
            inventory.save()

        return redirect("order/waiting")


def rejectOrder(request):
    if request.method == "GET":
        id = request.GET.get("id")
        order = Order.objects.get(id=id)
        order.status = 0
        order.created_time = datetime.now()
        order.save()

        return redirect("order/waiting")


def customerRejectOrder(request):
    if request.method == "GET":
        id = request.GET.get("id")
        order = Order.objects.get(id=id)
        order.status = 0
        order.created_time = datetime.now()
        order.save()

        # reverse quantity of product and inventory
        carItem = Cartitem.objects.filter(cart_id=Cart.objects.get(id=order.cart_id.id).id)
        print(len(carItem))
        for item in carItem:
            print(item.product_id.inventory_id.id)
            inventory_id = item.product_id.inventory_id.id
            product = Product.objects.get(inventory_id=inventory_id)
            product.quantity = product.quantity + item.quantity
            product.save()

            inventory = Inventory.objects.get(id=inventory_id)
            inventory.quantity = inventory.quantity + item.quantity
            inventory.save()

        return redirect("order/delivering")


def markAsDelivered(request):
    if request.method == "GET":
        id = request.GET.get("id")
        order = Order.objects.get(id=id)
        order.status = 3
        order.created_time = datetime.now()
        order.save()

        return redirect("order/waiting")
