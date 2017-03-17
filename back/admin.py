# -*- coding: utf-8 -*-
from django.contrib import admin
from back.models import Article
# Register your models here.
# 在未更改数据界面显示字段
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('ar_name','ar_desc','timestamp')
# admin.site.register(Article, ArticleAdmin)