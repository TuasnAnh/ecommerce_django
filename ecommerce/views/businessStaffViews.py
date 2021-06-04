from datetime import datetime
from ecommerce.views.views import login
from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from ..models import (
    Book,
    Category,
    Clothes,
    Electro,
    Fashioncategory,
    Inventory,
    Order,
    Person,
    Product,
    Supplier,
    User,
)
from ..currentAuthen import authen


def business_homepage(request):
    if request.method == "GET":
        print(authen.username)
        # if not authen.checkAuthen():
        #     return redirect("login")

        product = Product.objects.all()
        for item in product:
            price = item.price
            sale = item.sale
            salePrice = price * sale / 100
            item.salePrice = round(salePrice)

        res = {"product": product}

        return render(request, "business/business-homepage.html", res)


def productSearch(request):
    if request.method == "POST":
        search = request.POST.get("product-search")
        print(search)

        inventory = []
        book = Book.objects.filter(name__icontains=search)
        electro = Electro.objects.filter(name__icontains=search)
        clothes = Clothes.objects.filter(name__icontains=search)

        for item in book:
            inventory.append(Inventory.objects.get(book_id=item))

        for item in electro:
            inventory.append(Inventory.objects.get(electro_id=item))

        for item in clothes:
            inventory.append(Inventory.objects.get(clothes_id=item))

        product = []
        for item in inventory:
            p = Product.objects.filter(inventory_id=item)
            print(len(p))
            if len(p) > 0:
                product.append(p[0])
        res = {"product": product}
        return render(request, "business/business-homepage.html", res)


def addProductView(request):
    if request.method == "GET":
        print(authen.username)
        # if not authen.checkAuthen():
        #     return redirect("login")

        inventory = Inventory.objects.all()
        display = []
        for item in inventory:
            isOnLive = Product.objects.filter(inventory_id=item).exists()
            item.onLive = isOnLive
            display.append(item)

        res = {"inventory": display}
        return render(request, "business/product-add.html", res)


def searchInventory(request):
    if request.method == "POST":
        search = request.POST.get("inventory-search")
        print(search)

        inventory = []
        book = Book.objects.filter(name__icontains=search)
        electro = Electro.objects.filter(name__icontains=search)
        clothes = Clothes.objects.filter(name__icontains=search)

        for item in book:
            inventory.append(Inventory.objects.get(book_id=item))

        for item in electro:
            inventory.append(Inventory.objects.get(electro_id=item))

        for item in clothes:
            inventory.append(Inventory.objects.get(clothes_id=item))

        # inventory = Inventory.objects.filter(name__icontains=search)
        res = {"inventory": inventory}
        return render(request, "business/product-add.html", res)


def showBookAddform(request):
    if request.method == "GET":
        inventory_id = request.GET.get("id")
        inventory = Inventory.objects.get(id=inventory_id)
        category = Category.objects.all()
        supplier = Supplier.objects.all()
        res = {"inventory": inventory, "category": category, "supplier": supplier}
        return render(request, "business/book-add-form.html", res)


def showElectroAddForm(request):
    if request.method == "GET":
        inventory_id = request.GET.get("id")
        inventory = Inventory.objects.get(id=inventory_id)
        supplier = Supplier.objects.all()
        res = {"inventory": inventory, "supplier": supplier}
        return render(request, "business/electro-add-form.html", res)


def showClothesAddForm(request):
    if request.method == "GET":
        inventory_id = request.GET.get("id")
        inventory = Inventory.objects.get(id=inventory_id)
        supplier = Supplier.objects.all()
        fashionCategory = Fashioncategory.objects.all()
        res = {"inventory": inventory, "supplier": supplier, "fashionCategory": fashionCategory}
        return render(request, "business/clothes-add-form.html", res)


def addBook(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        author = request.POST.get("author")
        publisher = request.POST.get("publisher")
        category_id = request.POST.get("category")
        supplier_id = request.POST.get("supplier")
        sale = request.POST.get("sale")
        description = request.POST.get("description")

        print(name, quantity, price, author, publisher, category_id, supplier_id, sale, description)

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(author) <= 0
            or len(publisher) <= 0
            or len(category_id) <= 0
            or len(supplier_id) <= 0
            or len(sale) <= 0
            or len(description) <= 0
        ):
            messages.info(request, "Vui lòng nhập đủ dữ liệu!")
            return redirect("/product/book/add-form?id=" + str(id))

        inventory = Inventory.objects.get(id=id)
        isExist = Product.objects.filter(inventory_id=inventory).exists()

        if isExist:
            messages.info(request, "Đã có mặt hàng này!")
            return redirect("/product/book/add-form?id=" + str(id))

        if int(inventory.quantity) < int(quantity):
            messages.info(request, "Không đủ hàng trong kho!")
            return redirect("/product/book/add-form?id=" + str(id))

        created_time = datetime.now()
        product = Product(
            inventory_id=inventory,
            type=1,
            sale=sale,
            price=price,
            quantity=quantity,
            created_time=created_time,
            description=description,
        )
        product.save()
        return redirect("/product/add")


def addElectro(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        width = request.POST.get("width")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        branch = request.POST.get("branch")
        supplier_id = request.POST.get("supplier")
        sale = request.POST.get("sale")
        description = request.POST.get("description")

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(width) <= 0
            or len(height) <= 0
            or len(weight) <= 0
            or len(branch) <= 0
            or len(supplier_id) <= 0
            or len(sale) <= 0
            or len(description) <= 0
        ):
            messages.info(request, "Vui lòng nhập đủ dữ liệu!")
            return redirect("/product/electro/add-form?id=" + str(id))

        inventory = Inventory.objects.get(id=id)
        isExist = Product.objects.filter(inventory_id=inventory).exists()

        if isExist:
            messages.info(request, "Đã có mặt hàng này!")
            return redirect("/product/electro/add-form?id=" + str(id))

        if int(inventory.quantity) < int(quantity):
            messages.info(request, "Không đủ hàng trong kho!")
            return redirect("/product/electro/add-form?id=" + str(id))

        created_time = datetime.now()
        product = Product(
            inventory_id=inventory,
            type=2,
            sale=sale,
            price=price,
            quantity=quantity,
            created_time=created_time,
            description=description,
        )
        product.save()
        return redirect("/product/add")


def addClothes(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        size = request.POST.get("size")
        branch = request.POST.get("branch")
        color = request.POST.get("color")
        fashionCategory_id = request.POST.get("fashionCategory")
        supplier_id = request.POST.get("supplier")
        sale = request.POST.get("sale")
        description = request.POST.get("description")

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(size) <= 0
            or len(branch) <= 0
            or len(color) <= 0
            or len(fashionCategory_id) <= 0
            or len(supplier_id) <= 0
            or len(sale) <= 0
            or len(description) <= 0
        ):
            messages.info(request, "Vui lòng nhập đủ dữ liệu!")
            return redirect("/product/clothes/add-form?id=" + str(id))

        inventory = Inventory.objects.get(id=id)
        isExist = Product.objects.filter(inventory_id=inventory).exists()

        if isExist:
            messages.info(request, "Đã có mặt hàng này!")
            return redirect("/product/clothes/add-form?id=" + str(id))

        if int(inventory.quantity) < int(quantity):
            messages.info(request, "Không đủ hàng trong kho!")
            return redirect("/product/clothes/add-form?id=" + str(id))

        created_time = datetime.now()
        product = Product(
            inventory_id=inventory,
            type=3,
            sale=sale,
            price=price,
            quantity=quantity,
            created_time=created_time,
            description=description,
        )
        product.save()
        return redirect("/product/add")


def showBookEdit(request):
    product_id = request.GET.get("id")
    product = Product.objects.get(id=product_id)
    category = Category.objects.all()
    supplier = Supplier.objects.all()
    res = {"product": product, "category": category, "supplier": supplier}
    return render(request, "business/book-edit-form.html", res)


def showElectroEdit(request):
    product_id = request.GET.get("id")
    product = Product.objects.get(id=product_id)
    category = Category.objects.all()
    supplier = Supplier.objects.all()
    res = {"product": product, "category": category, "supplier": supplier}
    return render(request, "business/electro-edit-form.html", res)


def showClothesEdit(request):
    product_id = request.GET.get("id")
    product = Product.objects.get(id=product_id)
    category = Category.objects.all()
    supplier = Supplier.objects.all()
    res = {"product": product, "category": category, "supplier": supplier}
    return render(request, "business/clothes-edit-form.html", res)


def editProduct(request, id):
    if request.method == "POST":
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        sale = request.POST.get("sale")
        description = request.POST.get("description")
        product = Product.objects.get(id=id)

        type = ""
        if product.type == 1:
            type = "book"
        elif product.type == 2:
            type = "electro"
        elif product.type == 3:
            type = "clothes"

        if len(quantity) <= 0 or len(price) <= 0 or len(sale) <= 0 or len(description) <= 0:
            messages.info(request, "Vui lòng nhập đủ dữ liệu!")
            return redirect("/product/" + type + "/edit?id=" + str(id))

        if int(product.inventory_id.quantity) < int(quantity):
            messages.info(request, "Không đủ hàng trong kho!")
            return redirect("/product/" + type + "/edit?id=" + str(id))

        product.price = price
        product.quantity = quantity
        product.sale = sale
        product.description = description
        product.save()

        return redirect("business-homepage")
