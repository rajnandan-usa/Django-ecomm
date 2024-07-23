from django.contrib import admin
from .models import *

# Register your models here.

class Product_Images(admin.TabularInline):
    model = Product_Image

class Additional_informations(admin.TabularInline):
    model = Additional_information

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images,Additional_informations)
    list_display = ('product_name','price','Categories','color','section')
    list_editable = ('Categories','section','color')

admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(main_category)
admin.site.register(category)
admin.site.register(subcategory)

admin.site.register(section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_information)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Coupon_Code)