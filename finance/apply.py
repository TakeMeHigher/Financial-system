from django.shortcuts import  HttpResponse,render,redirect

from finance import models

def activityapply(request):
    uid=request.session.get('user_info').get('nid')
    userinfo=models.UserInfo.objects.filter(user_id=uid).first()
    companys=models.Company.objects.all()
    return render(request,'apply/activity.html',{"userinfo":userinfo,'companys':companys})

def apply(request,apply_url):
    if  apply_url=='activityapply':
        return apply_url(request)
