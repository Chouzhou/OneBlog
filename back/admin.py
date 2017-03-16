from django.contrib import admin
from back.models import Article, ArticleAdmin
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('ar_name','timestamp')
admin.site.register(Article, ArticleAdmin)