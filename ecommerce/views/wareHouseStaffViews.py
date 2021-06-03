from ecommerce.views.views import login
from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from ..models import Book, Category, Clothes, Electro, Fashioncategory, Inventory, Person, Supplier, User
from ..currentAuthen import authen
from datetime import date, datetime


# INVENTORY CONTROLLER
def warehouse_homepage(request):
    if request.method == "GET":
        print(authen.username)
        # if not authen.checkAuthen():
        #     return redirect("login")

        inventory = Inventory.objects.all()
        res = {"inventory": inventory}
        return render(request, "warehouse/warehouse-homepage.html", res)


def addInventory(request):
    return render(request, "warehouse/inventory-add.html")


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
        return render(request, "warehouse/warehouse-homepage.html", res)


def inventoryBook(request):
    if request.method == "GET":
        category = Category.objects.all()
        supplier = Supplier.objects.all()
        res = {"category": category, "supplier": supplier}

        return render(request, "warehouse/add-book.html", res)


def inventoryEditBookF(request):
    if request.method == "GET":
        inventory_id = request.GET.get("id")
        inventory = Inventory.objects.get(id=inventory_id)
        category = Category.objects.all()
        supplier = Supplier.objects.all()
        res = {"inventory": inventory, "category": category, "supplier": supplier}
        return render(request, "warehouse/edit-book.html", res)


def inventoryEditBook(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        author = request.POST.get("author")
        publisher = request.POST.get("publisher")
        category_id = request.POST.get("category")
        supplier_id = request.POST.get("supplier")

        print(name, quantity, price, author, publisher, category_id, supplier_id)

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(author) <= 0
            or len(publisher) <= 0
            or len(category_id) <= 0
            or len(supplier_id) <= 0
        ):
            return redirect("/inventory/book/edit-form?id=" + str(id))

        inventory = Inventory.objects.get(id=int(id))
        inventory.quantity = quantity
        inventory.price = price
        inventory.save()

        book = Book.objects.get(id=inventory.book_id.id)
        book.name = name
        book.author = author
        book.publisher = publisher
        book.category_id = Category.objects.get(id=int(category_id))
        book.supplier_id = Supplier.objects.get(id=int(supplier_id))
        book.save()

        return redirect("warehouse-homepage")


def inventoryAddBook(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        author = request.POST.get("author")
        publisher = request.POST.get("publisher")
        category_id = request.POST.get("category")
        supplier_id = request.POST.get("supplier")

        print(name, quantity, price, author, publisher, category_id, supplier_id)

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(author) <= 0
            or len(publisher) <= 0
            or len(category_id) <= 0
            or len(supplier_id) <= 0
        ):
            return redirect("/inventory/book")

        category = Category.objects.get(id=category_id)
        book = Book(
            name=name,
            supplier_id=Supplier.objects.get(id=int(supplier_id)),
            category_id=Category.objects.get(id=int(category_id)),
            author=author,
            publisher=publisher,
            category=category.name,
        )
        book.save()
        boom_id = Book.objects.latest("id")
        created_time = datetime.now()
        print(created_time)

        inventory = Inventory(
            book_id=boom_id, type=1, price=int(price), quantity=int(quantity), created_time=str(created_time)
        )
        inventory.save()

        return redirect("inventory/add")


def inventoryElectro(request):
    if request.method == "GET":
        supplier = Supplier.objects.all()
        res = {"supplier": supplier}

        return render(request, "warehouse/add-electro.html", res)


def inventoryEditElectro(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        width = request.POST.get("width")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        branch = request.POST.get("branch")
        supplier_id = request.POST.get("supplier")

        print(name, quantity, price, width, height, weight, branch, supplier_id)

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(width) <= 0
            or len(height) <= 0
            or len(weight) <= 0
            or len(branch) <= 0
            or len(supplier_id) <= 0
        ):
            return redirect("/inventory/electro/edit-form?id=" + str(id))

        inventory = Inventory.objects.get(id=int(id))
        inventory.quantity = quantity
        inventory.price = price
        inventory.save()

        electro = Electro.objects.get(id=inventory.electro_id.id)
        electro.name = name
        electro.width = width
        electro.height = height
        electro.weight = weight
        electro.branch = branch
        electro.supplier_id = Supplier.objects.get(id=int(supplier_id))
        electro.save()

        return redirect("warehouse-homepage")


def inventoryEditElectroF(request):
    if request.method == "GET":
        inventory_id = request.GET.get("id")
        inventory = Inventory.objects.get(id=inventory_id)
        supplier = Supplier.objects.all()
        res = {"inventory": inventory, "supplier": supplier}
        return render(request, "warehouse/edit-electro.html", res)


def inventoryAddElectro(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        width = request.POST.get("width")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        branch = request.POST.get("branch")
        supplier_id = request.POST.get("supplier")

        print(name, quantity, price, width, height, weight, branch, supplier_id)

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(width) <= 0
            or len(height) <= 0
            or len(weight) <= 0
            or len(branch) <= 0
            or len(supplier_id) <= 0
        ):
            return redirect("/inventory/electro")

        electro = Electro(
            name=name,
            supplier_id=Supplier.objects.get(id=int(supplier_id)),
            width=width,
            height=height,
            weight=weight,
            branch=branch,
        )
        electro.save()

        electro_id = Electro.objects.latest("id")
        created_time = datetime.now()
        print(created_time)

        inventory = Inventory(
            electro_id=electro_id, type=2, price=int(price), quantity=int(quantity), created_time=str(created_time)
        )
        inventory.save()

        return redirect("inventory/add")


def inventoryClothes(request):
    if request.method == "GET":
        supplier = Supplier.objects.all()
        fashionCategory = Fashioncategory.objects.all()
        res = {"supplier": supplier, "fashionCategory": fashionCategory}
        return render(request, "warehouse/add-clothes.html", res)


def inventoryEditClothes(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        size = request.POST.get("size")
        branch = request.POST.get("branch")
        color = request.POST.get("color")
        fashionCategory_id = request.POST.get("fashionCategory")
        supplier_id = request.POST.get("supplier")

        print(name, quantity, price, size, color, fashionCategory_id, branch, supplier_id)

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(size) <= 0
            or len(color) <= 0
            or len(fashionCategory_id) <= 0
            or len(branch) <= 0
            or len(supplier_id) <= 0
        ):
            return redirect("/inventory/clothes/edit-form?id=" + str(id))

        inventory = Inventory.objects.get(id=int(id))
        inventory.quantity = quantity
        inventory.price = price
        inventory.save()

        clothes = Clothes.objects.get(id=inventory.clothes_id.id)
        clothes.name = name
        clothes.supplier_id = Supplier.objects.get(id=int(supplier_id))
        clothes.fashioncategory_id = Fashioncategory.objects.get(id=int(fashionCategory_id))
        clothes.size = size
        clothes.branch = branch
        clothes.color = color
        clothes.save()

        return redirect("/warehouse-homepage")


def inventoryEditClothesF(request):
    if request.method == "GET":
        inventory_id = request.GET.get("id")
        inventory = Inventory.objects.get(id=inventory_id)
        supplier = Supplier.objects.all()
        fashionCategory = Fashioncategory.objects.all()
        res = {"inventory": inventory, "supplier": supplier, "fashionCategory": fashionCategory}
        return render(request, "warehouse/edit-clothes.html", res)


def inventoryAddClothes(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        size = request.POST.get("size")
        branch = request.POST.get("branch")
        color = request.POST.get("color")
        fashionCategory_id = request.POST.get("fashionCategory")
        supplier_id = request.POST.get("supplier")

        print(name, quantity, price, size, color, fashionCategory_id, branch, supplier_id)

        if (
            len(name) <= 0
            or len(quantity) <= 0
            or len(price) <= 0
            or len(size) <= 0
            or len(color) <= 0
            or len(fashionCategory_id) <= 0
            or len(branch) <= 0
            or len(supplier_id) <= 0
        ):
            return redirect("/inventory/clothes")

        clothes = Clothes(
            name=name,
            supplier_id=Supplier.objects.get(id=int(supplier_id)),
            fashioncategory_id=Fashioncategory.objects.get(id=int(fashionCategory_id)),
            branch=branch,
            size=size,
            color=color,
        )
        clothes.save()

        clothes_id = Clothes.objects.latest("id")
        created_time = datetime.now()
        print(created_time)

        inventory = Inventory(
            clothes_id=clothes_id, type=3, price=int(price), quantity=int(quantity), created_time=str(created_time)
        )
        inventory.save()

        return redirect("inventory/add")


# SUPPLIER CONTROLLER
def supplier(request):
    if request.method == "GET":
        supplier = Supplier.objects.all()
        res = {"supplier": supplier}
        return render(request, "warehouse/supplier.html", res)


def addSupplier(request):
    if request.method == "POST":
        name = request.POST.get("supplierName")
        address = request.POST.get("supplierAddress")
        if len(name) <= 0 or len(address) <= 0:
            return redirect("supplier")

        supplier = Supplier(name=name, address=address)
        supplier.save()

        return redirect("supplier")


# CATEGORY CONTROLLER
def category(request):
    if request.method == "GET":
        categorys = Category.objects.all()
        fashioncategorys = Fashioncategory.objects.all()
        res = {"fashionCategory": fashioncategorys, "bookCategory": categorys}

        return render(request, "warehouse/category.html", res)


def addCategory(request):
    if request.method == "POST":
        name = request.POST.get("newBookCategory")
        if len(name) <= 0:
            return redirect("category")

        category = Category(name=name)
        category.save()

        return redirect("category")


def addFashionCategory(request):
    if request.method == "POST":
        name = request.POST.get("newFashionCategory")
        if len(name) <= 0:
            return redirect("category")

        fashionCategory = Fashioncategory(name=name)
        fashionCategory.save()

        return redirect("category")


# STATISTICAL CONTROLLER
def statistical(request):
    if request.method == "GET":
        return render(request, "warehouse/statistical.html", {})
