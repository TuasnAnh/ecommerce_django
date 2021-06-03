from django.urls import path
from .views import views, wareHouseStaffViews, saleStaffViews, businessStaffViews, customerViews

urlpatterns = [
    path("", views.login, name="login"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    # customer urls
    path("homepage", customerViews.homepage, name="homepage"),
    path("register", customerViews.register, name="register"),
    # warehouse urls
    path("warehouse-homepage", wareHouseStaffViews.warehouse_homepage, name="warehouse-homepage"),
    path("inventory/search", wareHouseStaffViews.searchInventory, name="inventory/search"),
    path("inventory/add", wareHouseStaffViews.addInventory, name="inventory/add"),
    path("inventory/book", wareHouseStaffViews.inventoryBook, name="inventory/book"),
    path("inventory/book/add", wareHouseStaffViews.inventoryAddBook, name="inventory/book/add"),
    path("inventory/book/edit/<int:id>", wareHouseStaffViews.inventoryEditBook, name="inventory/book/edit"),
    path("inventory/book/edit-form", wareHouseStaffViews.inventoryEditBookF, name="inventory/book/edit-form"),
    path("inventory/electro", wareHouseStaffViews.inventoryElectro, name="inventory/electro"),
    path("inventory/electro/add", wareHouseStaffViews.inventoryAddElectro, name="inventory/electro/add"),
    path("inventory/electro/edit/<int:id>", wareHouseStaffViews.inventoryEditElectro, name="inventory/electro/edit"),
    path("inventory/electro/edit-form", wareHouseStaffViews.inventoryEditElectroF, name="inventory/electro/edit-form"),
    path("inventory/clothes", wareHouseStaffViews.inventoryClothes, name="inventory/clothes"),
    path("inventory/clothes/add", wareHouseStaffViews.inventoryAddClothes, name="inventory/clothes/add"),
    path("inventory/clothes/edit/<int:id>", wareHouseStaffViews.inventoryEditClothes, name="inventory/clothes/edit"),
    path("inventory/clothes/edit-form", wareHouseStaffViews.inventoryEditClothesF, name="inventory/clothes/edit-form"),
    path("supplier", wareHouseStaffViews.supplier, name="supplier"),
    path("supplier/add", wareHouseStaffViews.addSupplier, name="supplier/add"),
    path("category", wareHouseStaffViews.category, name="category"),
    path("category/add", wareHouseStaffViews.addCategory, name="category/add"),
    path("fashionCategory/add", wareHouseStaffViews.addFashionCategory, name="fashionCategory/add"),
    path("statistical", wareHouseStaffViews.statistical, name="statistical"),
    # business urls
    path("business-homepage", businessStaffViews.business_homepage, name="business-homepage"),
    # sale urls
    path("sale-homepage", saleStaffViews.sale_homepage, name="sale-homepage"),
]
