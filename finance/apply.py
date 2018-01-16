from django.db import transaction
from django.shortcuts import  HttpResponse,render,redirect

from finance import models


import datetime,time
#
# def activityapply(request):
#     uid=request.session.get('user_info').get('nid')
#     userinfo=models.UserInfo.objects.filter(user_id=uid).first()
#     companys=models.Company.objects.all()
#     return render(request,'apply/actapply.html',{"userinfo":userinfo,'companys':companys})



def activity_apply(request):
    """
    活动推广表相关页面展示，以及数据的提交处理。
    :param request:
    :return:
    """
    user_id=request.session["user_info"].get("nid")#通过session中已经登录的user信息获取到user_id
    User_obj=models.User.objects.filter(pk=user_id).first()#查找到user对象
    user_obj=models.UserInfo.objects.filter(user_id=user_id).first()#通过user对象查找到userinfo对象。
    company_list=models.Company.objects.all()#获取所有的公司列表
    context={
        "user_obj":user_obj,
        "company_list":company_list,
    }
    now_datetime = datetime.datetime.utcnow().strftime("%Y%m%d")#获取当前日期20171110格式
    itme_id = str(int(time.time() * 1000)) + str(int(time.clock() * 10000))#生成唯一的随机数字。
    form_id=itme_id[-4:]+now_datetime#截取前4位与当前日期拼接。
    if request.method=="POST":
        """
        利用form表单POST请求提交过来的表格数据写入到ActivityApply表。
        """
        # print("____|",request.POST)
        apply_id=int(form_id)
        indent_id=models.ActivityApply.objects.filter(apply_id=apply_id).first()
        # 判断流水单号是否存在如果存在将前面4位数字加个1后与当前日期拼接。
        if not indent_id:
            apply_id=apply_id
        else:
            apply_id=int(itme_id[-4:])+1+int(now_datetime)
        form=request.POST.get("form")
        product_name=request.POST.get("product_name")
        product_version=request.POST.get("product_version")
        advocate_platform=request.POST.get("advocate_platform")
        advocate_des=request.POST.get("advocate_des")
        apply_cause=request.POST.get("apply_cause")#列表多选菜单。修改为单选框。
        if request.POST.get("apply_cause")==4:
            apply_cause=request.POST.get("apply_other")
            # print("其他____",apply_cause)
        anticipate=request.POST.get("anticipate")
        fg=request.POST.get("fg")
        before_result=request.POST.get("before_result")
        bg=request.POST.get("bg")
        payer=request.POST.get("payer")
        budget=request.POST.get("budget")
        exigence=request.POST.get("exigence")
        currency_type=request.POST.get("currency_type")
        note=request.POST.get("remarks")
        write_model={
            "apply_id":apply_id,
            "depart":user_obj.department,
            "user":User_obj,
            "form":form,
            "payer_id":payer,
            "budget":budget,
            "exigence":exigence,
            "apply_type_id":1,
            "product_name":product_name,
            "product_version":product_version,
            "advocate_platform":advocate_platform,
            "advocate_des":advocate_des,
            "apply_cause":apply_cause,
            "anticipate":anticipate,
            "first_generalize":fg,
            "before_result":before_result,
            "buy_goods":bg,
            "currency_type":currency_type,
            "attachment":None,#上传文件我暂时先弄成None做测试的
            "note":note,
        }
        print(write_model)
        with transaction.atomic():
            models.ActivityApply.objects.create(**write_model)
            base_obj=models.BaseApply.objects.filter(apply_id=apply_id).first()
            record_dic={
                "operate_id":user_obj.pk,
                "apply_for_id":base_obj.pk,
                "status":1,#(刚提交的表单状态默认为1已提交)
                "note":note,
                "apply_type_id":1
            }
            models.Record.objects.create(**record_dic)#记录表记录数据
            return HttpResponse("表单提交成功")
    return render(request, "apply/actapply.html", context)



# def adminapply(request):
#     user_id = request.session["user_info"].get("nid")  # 通过session中已经登录的user信息获取到user_id
#     User_obj = models.User.objects.filter(pk=user_id).first()  # 查找到user对象
#     user_obj = models.UserInfo.objects.filter(user_id=user_id).first()  # 通过user对象查找到userinfo对象。
#     company_list = models.Company.objects.all()  # 获取所有的公司列表
#     context = {
#         "user_obj": user_obj,
#         "company_list": company_list,
#     }
#     now_datetime = datetime.datetime.utcnow().strftime("%Y%m%d")  # 获取当前日期20171110格式
#     itme_id = str(int(time.time() * 1000)) + str(int(time.clock() * 10000))  # 生成唯一的随机数字。
#     form_id = itme_id[-4:] + now_datetime  # 截取前4位与当前日期拼接。
#
#
#     if request.method=='POST':
#         apply_id = int(form_id)
#         indent_id = models.ActivityApply.objects.filter(apply_id=apply_id).first()
#         # 判断流水单号是否存在如果存在将前面4位数字加个1后与当前日期拼接。
#         if not indent_id:
#             apply_id = apply_id
#         else:
#             apply_id = int(itme_id[-4:]) + 1 + int(now_datetime)
#         form = request.POST.get("form")
#         goodtype=None
#         if goodtype==6:
#             goodtype= request.POST.get('good_type_other')
#         else:
#             goodtype=request.POST.get('goodtype')
#         good_use=request.POST.get('good_use')
#         goodname=request.POST.get('goodname')
#         goodtype=request.POST.get('goodtype')
#         godnum=request.POST.get('godnum')
#         godnote=request.POST.get('godnote')
#         goodprice=request.POST.get('godprice')
#         goodmodel=request.POST.get('goodmodel')
#         payer = request.POST.get("payer")
#         budget = request.POST.get("budget")
#         exigence = request.POST.get("exigence")
#         currency_type = request.POST.get("currency_type")
#         note = request.POST.get("remarks")
#         good_model={
#             'godmdoel':goodmodel,
#             'caption':goodname,
#             'num':godnum,
#             'price':goodprice,
#             'note':godnote
#         }
#         with transaction.atomic():
#             good=models.Goods.objects.create(**good_model)
#             write_model = {
#                 "apply_id": apply_id,
#                 "depart": user_obj.department,
#                 "user": User_obj,
#                 "form": form,
#                 "payer_id": payer,
#                 "budget": budget,
#                 "exigence": exigence,
#                 "currency_type": currency_type,
#                 "attachment": None,  # 上传文件我暂时先弄成None做测试的
#                 "note": note,
#                 "apply_type_id": 2,
#                 "purchase_type": goodtype,
#                 'gooduse': good_use,
#                 'attachment':None
#             }
#             print()
#             adminapply=models.AdminApply.objects.create(**write_model)
#             adminapply.good.add(good)
#             base_obj = models.BaseApply.objects.filter(apply_id=apply_id).first()
#             record_dic = {
#                 "operate_id": user_obj.pk,
#                 "apply_for_id": base_obj.pk,
#                 "status": 1,  # (刚提交的表单状态默认为1已提交)
#                 "note": note,
#                 "apply_type_id": 2
#             }
#             models.Record.objects.create(**record_dic)  # 记录表记录数据
#             return HttpResponse("表单提交成功")
#
#     return render(request, 'apply/adminapply.html', context)

def apply(request,apply_url):
    if  apply_url=='activityapply':
        return activity_apply(request)
    # elif apply_url=='adminapply':
    #     return  adminapply(request)
