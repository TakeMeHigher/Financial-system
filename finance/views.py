from django.shortcuts import render,redirect,HttpResponse
from rbac import models as rbac_models
from rbac.service.init_permission import init_permission
# Create your views here.


def index(request):
    # url = "{}?{}".format(request.path_info,request.GET.urlencode())
    # print(url)
    # print(request.path_info)
    # print(request.GET)
    # print(request.GET.urlencode())
    return render(request,"index.html")



def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method=="POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        # print("___cookie",request.COOKIES)
        obj = rbac_models.User.objects.filter(username=username,password=pwd).first()
        if obj:
            #初始化权限
            request.session["user_info"]={"nid":obj.id}

            print(request.session["user_info"])
            init_permission(obj,request)

            return redirect('/index/')
        else:
            return render(request, "login.html")

def logout(request):
    request.session["user_info"] = None
    return redirect("/login/")