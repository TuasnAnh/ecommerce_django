from datetime import datetime
from ecommerce.views.views import login
from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from ..models import Bank, Cart, Cartitem, Inventory, Order, Person, Product, User
from ..currentAuthen import authen


def homepage(request):
    if request.method == "GET":
        # print(authen.username)
        # if not authen.checkAuthen():
        #     return redirect("login")

        product = Product.objects.all()
        for item in product:
            price = item.price
            sale = item.sale
            salePrice = price * (100 - sale) / 100
            item.salePrice = round(salePrice)

        res = {"product": product}

        return render(request, "customer/homepage.html", res)


def register(request):
    if request.method == "GET":
        return render(request, "customer/register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        phone = request.POST.get("Phone")
        email = request.POST.get("Email")
        birth = request.POST.get("birth")
        address = request.POST.get("address")

        if (
            len(username) <= 0
            or len(password) <= 0
            or len(repassword) <= 0
            or len(name) <= 0
            or len(gender) <= 0
            or len(phone) <= 0
            or len(email) <= 0
            or len(birth) <= 0
            or len(address) <= 0
        ):
            messages.info(request, "Bạn chưa nhập đủ thông tin")
            return redirect("register")

        print(username, password, repassword, name, gender, phone, email, birth, address)

        existEmail = User.objects.filter(username=username).exists()
        if existEmail:
            messages.info(request, "Đã tồn tại tài khoản này")
            return redirect("register")

        if password != repassword:
            messages.info(request, "Không trùng mật khẩu")
            return redirect("register")

        user = User(username=username, pass_field=password, role="Customer")
        user.save()

        # get lastest id
        userId = User.objects.latest("id")
        person = Person(
            user_id=userId, gender=gender, birthday=birth, address=address, phone=phone, name=name, email=email
        )
        person.save()

        # get lastest person id
        lastestPerson = Person.objects.latest("id")
        cart = Cart(person_id=lastestPerson, is_used="false")
        cart.save()

        return redirect("login")


def addToCart(request, id):
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        print(id, quantity)

        if len(quantity) <= 0 or (len(quantity) > 0 and int(quantity) == 0):
            messages.info(request, "Bạn chưa nhập số lượng")
            return redirect("homepage")

        personId = request.session.get("personId")
        product = Product.objects.get(id=id)
        cart = Cart.objects.filter(person_id=personId).filter(is_used="false")[0]
        cartItem = Cartitem.objects.filter(cart_id=cart.id).filter(product_id=id)
        totalQuantity = int(quantity)

        alreadyInCart = cartItem.exists()
        # nếu hàng đó đã trong giỏ hàng
        if alreadyInCart:
            totalQuantity += cartItem[0].quantity

        if product.quantity < totalQuantity:
            messages.info(request, "Không đủ hàng")
            return redirect("homepage")

        if alreadyInCart:
            crrCartItem = Cartitem.objects.get(id=cartItem[0].id)
            crrCartItem.quantity = totalQuantity
            crrCartItem.save()
        else:
            newCartItem = Cartitem(cart_id=cart, product_id=product, quantity=totalQuantity)
            newCartItem.save()

        return redirect("homepage")


def getCart(request):
    if request.method == "GET":
        personId = request.session.get("personId")

        cart = Cart.objects.filter(person_id=personId).filter(is_used="false")[0]
        cartItem = Cartitem.objects.filter(cart_id=cart)

        # calculate total
        total = 0
        for item in cartItem:
            product = item.product_id
            price = product.price
            sale = product.sale
            salePrice = price * (100 - sale) / 100
            total += salePrice * item.quantity
            item.product_id.salePrice = round(salePrice)

        person = Person.objects.get(id=personId)

        res = {"cartItem": cartItem, "person": person, "total": round(total)}
        return render(request, "customer/cart.html", res)


def removeFromCart(request):
    if request.method == "GET":
        cartitem_id = request.GET.get("id")

        Cartitem.objects.filter(id=cartitem_id).delete()
        return redirect("cart")


def createOrder(request):
    if request.method == "POST":
        method = request.POST.get("method")

        personId = request.session.get("personId")
        person = Person.objects.get(id=personId)
        cart = Cart.objects.filter(person_id=personId).filter(is_used="false")[0]
        cartItem = Cartitem.objects.filter(cart_id=cart.id)

        if not cartItem.exists():
            return redirect("/cart")

        # cal total
        total = 0
        for item in cartItem:
            product = item.product_id
            price = product.price
            sale = product.sale
            salePrice = price * (100 - sale) / 100
            total += salePrice * item.quantity

        created_time = datetime.now()
        order = Order(
            person_id=person, cart_id=cart, created_time=created_time, status=1, method=int(method), total=round(total)
        )
        order.save()

        # disable old cart
        cart.is_used = "true"
        cart.save()

        # create new cart
        newCart = Cart(person_id=person, is_used="false")
        newCart.save()

        if int(method) == 1:
            return render(request, "customer/created-order-offline.html")
        else:
            bank = Bank.objects.all()
            res = {"bank": bank[0], "total": round(total)}
            return render(request, "customer/created-order-online.html", res)
        # return redirect("/homepage")


def showOnlineSuccess(request):
    if request.method == "GET":
        bank = Bank.objects.all()
        res = {"bank": bank[0], "total": round(1000)}
        return render(request, "customer/created-order-online.html", res)


def showOfflineSuccess(request):
    if request.method == "GET":
        return render(request, "customer/created-order-offline.html")
