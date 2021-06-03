# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bank(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)
    account = models.CharField(db_column="Account", max_length=255, blank=True, null=True)
    number = models.CharField(db_column="Number", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "bank"


class Book(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    supplier_id = models.ForeignKey("Supplier", models.DO_NOTHING, db_column="Supplier_id")
    category_id = models.ForeignKey("Category", models.DO_NOTHING, db_column="Category_id")
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)
    author = models.CharField(db_column="Author", max_length=255, blank=True, null=True)
    publisher = models.CharField(db_column="Publisher", max_length=255, blank=True, null=True)
    category = models.CharField(db_column="Category", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "book"


class Cart(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    person_id = models.ForeignKey("Person", models.DO_NOTHING, db_column="Person_id")

    class Meta:
        db_table = "cart"


class Cartitem(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    cart_id = models.ForeignKey(Cart, models.DO_NOTHING, db_column="Cart_id")
    product_id = models.ForeignKey("Product", models.DO_NOTHING, db_column="Product_id")
    quantity = models.IntegerField(db_column="Quantity")

    class Meta:
        db_table = "cartitem"


class Category(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "category"


class Clothes(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    supplier_id = models.ForeignKey("Supplier", models.DO_NOTHING, db_column="Supplier_id")
    fashioncategory_id = models.ForeignKey("Fashioncategory", models.DO_NOTHING, db_column="FashionCategory_id")
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)
    size = models.CharField(db_column="Size", max_length=255, blank=True, null=True)
    fashioncategory_name = models.CharField(db_column="FashionCategory_name", max_length=255, blank=True, null=True)
    branch = models.CharField(db_column="Branch", max_length=255, blank=True, null=True)
    color = models.CharField(db_column="Color", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "clothes"


class Electro(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    supplier_id = models.ForeignKey("Supplier", models.DO_NOTHING, db_column="Supplier_id")
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)
    width = models.CharField(db_column="Width", max_length=255, blank=True, null=True)
    height = models.CharField(db_column="Height", max_length=255, blank=True, null=True)
    weight = models.CharField(db_column="Weight", max_length=255, blank=True, null=True)
    branch = models.CharField(db_column="Branch", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "electro"


class Fashioncategory(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "fashioncategory"


class Inventory(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    book_id = models.ForeignKey(Book, models.DO_NOTHING, db_column="Book_id")
    electro_id = models.ForeignKey(Electro, models.DO_NOTHING, db_column="Elector_id")
    clothes_id = models.ForeignKey(Clothes, models.DO_NOTHING, db_column="Clothes_id")
    type = models.IntegerField(db_column="Type")
    price = models.IntegerField(db_column="Price")
    quantity = models.IntegerField(db_column="Quantity")
    created_time = models.CharField(db_column="Created_time", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "inventory"


class Invoice(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    order_id = models.ForeignKey("Order", models.DO_NOTHING, db_column="Order_id")
    bank_id = models.ForeignKey(Bank, models.DO_NOTHING, db_column="Bank_id")
    created_time = models.CharField(db_column="Created_time", max_length=255, blank=True, null=True)
    price = models.IntegerField(db_column="Price")
    status = models.IntegerField(db_column="Status")

    class Meta:
        db_table = "invoice"


class Order(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    person_id = models.ForeignKey("Person", models.DO_NOTHING, db_column="Person_id")
    cart_id = models.ForeignKey(Cart, models.DO_NOTHING, db_column="Cart_id")
    payment_id = models.ForeignKey("Payment", models.DO_NOTHING, db_column="Payment_id")
    shipment_id = models.ForeignKey("Shipment", models.DO_NOTHING, db_column="Shipment_id")
    bank_id = models.ForeignKey(Bank, models.DO_NOTHING, db_column="Bank_id")
    created_time = models.CharField(db_column="Created_time", max_length=255, blank=True, null=True)
    status = models.IntegerField(db_column="Status")
    method = models.IntegerField(db_column="Method")

    class Meta:
        db_table = "order"


class Payment(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    shipment_id = models.ForeignKey("Shipment", models.DO_NOTHING, db_column="Shipment_id")
    total = models.IntegerField(db_column="Total")

    class Meta:
        db_table = "payment"


class Person(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    user_id = models.ForeignKey("User", models.DO_NOTHING, db_column="User_id")
    gender = models.IntegerField(db_column="Gender")
    birthday = models.CharField(db_column="Birthday", max_length=255, blank=True, null=True)
    address = models.CharField(db_column="Address", max_length=255, blank=True, null=True)
    phone = models.CharField(db_column="Phone", max_length=255, blank=True, null=True)
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)
    email = models.CharField(db_column="Email", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "person"


class Product(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    inventory_id = models.ForeignKey(Inventory, models.DO_NOTHING, db_column="Inventory_id")
    type = models.IntegerField(db_column="Type")
    sale = models.IntegerField(db_column="Sale")
    price = models.IntegerField(db_column="Price")
    quantity = models.IntegerField(db_column="Quantity")
    created_time = models.CharField(db_column="Created_time", max_length=255, blank=True, null=True)
    description = models.CharField(db_column="Description", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "product"


class Shipment(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    shipfee = models.IntegerField(db_column="ShipFee")
    address = models.CharField(db_column="Address", max_length=255, blank=True, null=True)
    phone = models.CharField(db_column="Phone", max_length=255, blank=True, null=True)
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "shipment"


class Staff(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    user_id = models.ForeignKey("User", models.DO_NOTHING, db_column="User_id")
    gender = models.IntegerField(db_column="Gender")
    brithday = models.CharField(db_column="Brithday", max_length=255, blank=True, null=True)
    address = models.CharField(db_column="Address", max_length=255, blank=True, null=True)
    phone = models.CharField(db_column="Phone", max_length=255, blank=True, null=True)
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)
    salary = models.IntegerField(db_column="Salary")
    email = models.CharField(db_column="Email", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "staff"


class Supplier(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    name = models.CharField(db_column="Name", max_length=255, blank=True, null=True)
    address = models.CharField(db_column="Address", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "supplier"


class User(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    username = models.CharField(db_column="Username", max_length=255, blank=True, null=True)
    pass_field = models.CharField(db_column="Pass", max_length=255, blank=True, null=True)
    role = models.CharField(db_column="Role", max_length=255, blank=True, null=True)

    class Meta:
        db_table = "user"
