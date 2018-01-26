# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    # To display individual fields
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
