# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from rango.models import Category, Page

# Add in this class to customise the AdminInterface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    # To display individual fields
    list_display = ('title', 'category', 'url')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Page, PageAdmin)
