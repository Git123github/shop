# from django.contrib import admin
# from store.models import *
#
# # admin.site.register(Employee)
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']
#     list_display_links = ['name']
#     list_per_page = 1
#     search_fields = ['name']
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Category._meta.fields]
#
#     class Meta:
#         model = Category
#
#
# admin.site.register(Category, CategoryAdmin)
#
#
