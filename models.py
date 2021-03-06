# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bank(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bank'


class Book(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Supplier_id')  # Field name made lowercase.
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='Category_id')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category_0 = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'book'


class Cart(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Cartitem(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cart = models.ForeignKey(Cart, models.DO_NOTHING, db_column='Cart_id')  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_id')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cartitem'


class Category(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Clothes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Supplier_id')  # Field name made lowercase.
    fashioncategory = models.ForeignKey('Fashioncategory', models.DO_NOTHING, db_column='FashionCategory_id')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fashioncategory_name = models.CharField(db_column='FashionCategory_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clothes'


class Electro(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Supplier_id')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    width = models.CharField(db_column='Width', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=255, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electro'


class Fashioncategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fashioncategory'


class Inventory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    book = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_id')  # Field name made lowercase.
    elector = models.ForeignKey(Electro, models.DO_NOTHING, db_column='Elector_id')  # Field name made lowercase.
    clothes = models.ForeignKey(Clothes, models.DO_NOTHING, db_column='Clothes_id')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    created_time = models.CharField(db_column='Created_time', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'


class Invoice(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    order = models.ForeignKey('Order', models.DO_NOTHING, db_column='Order_id')  # Field name made lowercase.
    bank = models.ForeignKey(Bank, models.DO_NOTHING, db_column='Bank_id')  # Field name made lowercase.
    created_time = models.CharField(db_column='Created_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice'


class Order(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.
    cart = models.ForeignKey(Cart, models.DO_NOTHING, db_column='Cart_id')  # Field name made lowercase.
    payment = models.ForeignKey('Payment', models.DO_NOTHING, db_column='Payment_id')  # Field name made lowercase.
    shipment = models.ForeignKey('Shipment', models.DO_NOTHING, db_column='Shipment_id')  # Field name made lowercase.
    bank = models.ForeignKey(Bank, models.DO_NOTHING, db_column='Bank_id')  # Field name made lowercase.
    created_time = models.CharField(db_column='Created_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    method = models.IntegerField(db_column='Method')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Payment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shipment = models.ForeignKey('Shipment', models.DO_NOTHING, db_column='Shipment_id')  # Field name made lowercase.
    total = models.IntegerField(db_column='Total')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Person(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    birthday = models.CharField(db_column='Birthday', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person'


class Product(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING, db_column='Inventory_id')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    sale = models.IntegerField(db_column='Sale')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    created_time = models.CharField(db_column='Created_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Shipment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shipfee = models.IntegerField(db_column='ShipFee')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment'


class Staff(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    brithday = models.CharField(db_column='Brithday', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'


class Supplier(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.IntegerField(db_column='Name')  # Field name made lowercase.
    address = models.IntegerField(db_column='Address')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='Pass', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    role = models.CharField(db_column='Role', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
