from django.shortcuts import render,HttpResponse
from . import models

def test(request):
    name= "番禺"
    pwd= "123"
    # 获取当前用户对象
    user = models.User.objects.filter(username=name,password=pwd).first()
    # 获取当前用户所有的角色
    # role_list = user.roles.all()
    # 获取当前用户所有权限（去重）
    permission_list = user.roles.values('permissions__title','permissions__url','permissions__is_menu').distinct()

    return HttpResponse('...')
