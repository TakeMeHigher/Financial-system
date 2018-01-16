from django.conf.urls import url
from django.shortcuts import render, HttpResponse, redirect
from stark.service import v1
from . import models

#用户
class UserInfoConfig(v1.StarkConfig):
    list_display = ["user", "name", "department"]

    show_search_form = True

    search_fileds = ['user','name','department']

v1.site.register(models.UserInfo, UserInfoConfig)


#部门
class DepartmentConfig(v1.StarkConfig):
    list_display = ["name", ]
    show_search_form = True

    search_fileds = ['name']

v1.site.register(models.Department, DepartmentConfig)


#公司
class CompanyConfig(v1.StarkConfig):
    list_display = ["name", "bank", "card_num"]
    show_search_form = True

    search_fileds = ['name']

v1.site.register(models.Company, CompanyConfig)

#申请记录表
class RecordConfig(v1.StarkConfig):
    list_display = ["apply_for", "status", "operate", "operate_time"]


v1.site.register(models.Record, RecordConfig)


# 推广活动申请表
class ActivityApplyConfig(v1.StarkConfig):
    list_display = ["apply_id", "depart", "user"]


v1.site.register(models.ActivityApply, ActivityApplyConfig)


#申请表类类型
class ApplyTypeConfig(v1.StarkConfig):
    list_display = ["name", ]


v1.site.register(models.ApplyType, ApplyTypeConfig)

#申请表具体类型
class SecondTypeConfig(v1.StarkConfig):
    list_display = ["name","url","base_type"]

v1.site.register(models.SecondType, SecondTypeConfig)



# -----------申请管理---------
class BaseApplyConfig(v1.StarkConfig):

    def put_apply(self,request, *args, **kwargs):
        """填写申请-主页面"""
        apply_types = models.ApplyType.objects.all()
        context = {
            "apply_types":apply_types,
        }
        return render(request,"put_apply.html",context)

    def my_apply(self,request,*args,**kwargs):
        user_id = request.session["user_info"].get("nid")
        user_obj = models.UserInfo.objects.filter(user_id=user_id).first()
        record_obj=models.Record.objects.filter(operate=user_obj).all()
        print("______record_obj_list",record_obj)
        secondtype_obj_list=models.SecondType.objects.all()
        context={
            "record_obj":record_obj,
            "secondtype_obj_list":secondtype_obj_list,
        }

        return render(request,"my_apply.html",context)
    def my_apply_detail(self,request,pk,*args,**kwargs):
        base_obj=self.model_class.objects.filter(pk=pk).first()
        print("___base_obj",base_obj)#暂时不会做了

        return HttpResponse("详情页")
    def extra_urls(self):
        app_model_name = self.model_class._meta.app_label, self.model_class._meta.model_name

        patterns = [
            url(r'^put_apply/$', self.wrap(self.put_apply), name="%s_%s_put_apply" % app_model_name),
            url(r'^my_apply/$', self.wrap(self.my_apply), name="%s_%s_my_apply" % app_model_name),
            url(r'^my_apply_detail/(.+)/$', self.wrap(self.my_apply_detail), name="%s_%s_my_apply_detail" % app_model_name),

        ]
        return patterns


v1.site.register(models.BaseApply, BaseApplyConfig)

