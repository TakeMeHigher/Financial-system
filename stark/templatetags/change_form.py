from django.template import Library
from django.urls import reverse

from stark.service.v1 import site

register =Library()

# '''
# for bfield in form:
#     print(bfield.field, '--------------', type(bfield.field))
# <django.forms.fields.CharField object at 0x00000179480E6F60> -------------- <class 'django.forms.fields.CharField'>
# <django.forms.fields.CharField object at 0x00000179480E6FD0> -------------- <class 'django.forms.fields.CharField'>
# <django.forms.fields.TypedChoiceField object at 0x00000179480F5048> -------------- <class 'django.forms.fields.TypedChoiceField'>
# <django.forms.models.ModelChoiceField object at 0x00000179480F50B8> -------------- <class 'django.forms.models.ModelChoiceField'>
# <django.forms.models.ModelMultipleChoiceField object at 0x00000179480F5128> -------------- <class 'django.forms.models.ModelMultipleChoiceField'>
# '''
#
#
# ''''
# #bfield.field.queryset
# <QuerySet [<Department: 教育部>, <Department: 销售部>]>
# <QuerySet [<Role: 老师>, <Role: 学生>]>
# '''
#
# '''
# #bfield.field.queryset.model
# <class 'app03.models.Department'>
# <class 'app03.models.Role'>
# '''
#
# '''
# #bfield.auto_id
# id_depart
# id_roles
# '''

@register.inclusion_tag('stark/form.html')
def changeForm(config,model_obj_form):
    print(config)
    new_form = []
    for bfield in model_obj_form:
        temp = {"is_popup": False, "bfiled": bfield}
        from django.forms import ModelChoiceField
        #判断是不是外键和多对多
        if isinstance(bfield.field, ModelChoiceField):
            #获取相关联的model类
            relate_class_name = bfield.field.queryset.model
            #判断当前获取的model类是否注册了
            if relate_class_name in site._registry:
                #app名称和modellei名称
                app_model_name = relate_class_name._meta.app_label, relate_class_name._meta.model_name
                #获取当前获取model类add的url
                baseurl = reverse('stark:%s_%s_add' % app_model_name)

                model_name=config.model_class._meta.model_name
                related_name=config.model_class._meta.get_field(bfield.name).rel.related_name
                print(related_name,'related_name',type(related_name),'------------')
                #构建popup的url
                popurl = '%s?_popbackid=%s&model_name=%s&related_name=%s' % (baseurl, bfield.auto_id,model_name,related_name)
                temp["is_popup"] = True
                temp['popurl'] = popurl

        new_form.append(temp)
    return {"form":new_form}