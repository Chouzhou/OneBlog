# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
#主页显示
def home(request):
    return render(request, 'index.html')



from django.contrib.auth.models import User, Group
from back.models import Article
from rest_framework import viewsets
from back.serializers import UserSerializer, GroupSerializer, ArticleSerializer
# 解决出现‘身份认证信息未提供’
from rest_framework.authentication import SessionAuthentication, BasicAuthentication  
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly  


class UserViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑用户
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # 解决出现‘身份认证信息未提供’
    #注意这里我将BasicAuthentication放在了SessionAuthentication前面，否则  
    #会先用SessionAuthentication认证，而这会造成C#的NetworkCredentials认证失败  
    authentication_classes = (BasicAuthentication, SessionAuthentication, )  
    permission_classes = (IsAuthenticatedOrReadOnly,) 

