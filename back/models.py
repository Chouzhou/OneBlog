# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
# 文章
class Article(models.Model):
    # 文章名
    ar_name = models.CharField(max_length=30,verbose_name='文章名')
    # 文章描述
    ar_desc = models.CharField(max_length=255,verbose_name='文章描述')
    # 文章主要内容
    ar_body = models.TextField(verbose_name='文章主要内容')
    # 文章建立时间
    timestamp = models.DateTimeField(verbose_name='文章建立时间')
    def __str__(self):
        return self.ar_name
        
