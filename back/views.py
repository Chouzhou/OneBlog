# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
#主页显示
def home(request):
    return render(request, 'index.html')

