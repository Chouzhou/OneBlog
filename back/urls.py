# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from .views import *
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'articles', ArticleViewSet)

urlpatterns = [
    # url(r'^$', include('router.urls')),
    url(r'articles/$', ArticleViewSet.as_view(), name='article_list'),
    url(r'articles/(?P<ar_type>.+)', ArticleViewSetFilter.as_view()),
]