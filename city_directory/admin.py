from django.contrib import admin

from .models import Catalog, Category, Contact

@admin.register(Catalog)

class CatalogAdmin(admin.ModelAdmin):
    list_display=['name', 'description', 'category', 'address', 'city', 'contact']
    list_filter=['name', 'category', 'city', 'address']
    search_fields=['name', 'category', 'city', 'address']


@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    list_filter=['name']
    search_fields=['name']


@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display=['phone', 'second_phone', 'mail']
    list_filter=['phone', 'second_phone', 'mail']
    search_fields=['phone', 'mail']

