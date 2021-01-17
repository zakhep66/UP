from django.contrib import admin
from mainPage.models import Customer, Product, Cart, CartProduct, Order, ProductOrder, ImgProduct, Login, TableOrders, Rating
from django.forms import ModelForm


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'price', 'img') # какие поля будут видны в списке
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description', 'category', 'price', 'img') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('title', 'description', 'category', 'price', ) # по каким параметрам можем фильтровать

admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serName', 'tel', 'email') # какие поля будут видны в списке
    list_display_links = ('id', 'serName')
    search_fields = ('id', 'serName', 'name', 'email', 'tel') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('serName', 'name', 'email', 'tel', ) # по каким параметрам можем фильтровать

admin.site.register(Customer, CustomerAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer') # какие поля будут видны в списке
    list_display_links = ('id', 'customer')
    search_fields = ('id', 'customer') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('customer', ) # по каким параметрам можем фильтровать

admin.site.register(Cart, CartAdmin)


class CartProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'qty', 'final_price') # какие поля будут видны в списке
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('user', ) # по каким параметрам можем фильтровать

admin.site.register(CartProduct, CartProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'owner', 'data') # какие поля будут видны в списке
    list_display_links = ('id', 'owner')
    search_fields = ('id', 'cart', 'owner', 'data') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('cart', 'owner', 'data') # по каким параметрам можем фильтровать

admin.site.register(Order, OrderAdmin)


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order') # какие поля будут видны в списке
    list_display_links = ('id', 'product', 'order')
    search_fields = ('id', 'product', 'order') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('product', 'order') # по каким параметрам можем фильтровать

admin.site.register(ProductOrder, ProductOrderAdmin)


class ImgProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'url') # какие поля будут видны в списке
    list_display_links = ('id', 'product')
    search_fields = ('id', 'product') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('product', 'url') # по каким параметрам можем фильтровать

admin.site.register(ImgProduct, ImgProductAdmin)


class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'password', 'Avatar', 'customer') # какие поля будут видны в списке
    list_display_links = ('id', 'login')
    search_fields = ('id', 'login', 'password', 'Avatar', 'customer') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('login', 'password', 'Avatar', 'customer') # по каким параметрам можем фильтровать

admin.site.register(Login, LoginAdmin)


class TableOrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer') # какие поля будут видны в списке
    list_display_links = ('id', 'customer')
    search_fields = ('id', 'customer') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = () # по каким параметрам можем фильтровать

admin.site.register(TableOrders, TableOrdersAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'rating') # какие поля будут видны в списке
    list_display_links = ('id', 'product', 'customer', 'rating')
    search_fields = ('id', 'product', 'customer', 'rating') # по каким полям будет производиться поиск
    list_editable = () # что мы можем изменять не входя, стоит ничего, это картеж
    list_filter = ('product', 'customer', 'rating') # по каким параметрам можем фильтровать

admin.site.register(Rating, RatingAdmin)



# from import_export.admin import ImportExportModelAdmin
