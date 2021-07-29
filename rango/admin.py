from django.contrib import admin
from rango.models import Category, Page, PageAdmin, CategoryAdmin

# Register your models here.

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)