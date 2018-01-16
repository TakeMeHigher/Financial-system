from django.db import models
from rbac.models import User, Role


class UserInfo(models.Model):
    '''
    员工信息表
    '''
    user = models.ForeignKey(to=User, verbose_name="账号")
    name = models.CharField(max_length=32, verbose_name="姓名")
    english_name = models.CharField(max_length=32, null=True, blank=True,verbose_name="英文名")
    age = models.IntegerField("年龄", null=True)
    enroll_date = models.DateField("入职日期", null=True)
    leader = models.ForeignKey(to=Role, verbose_name="上司")
    department = models.ForeignKey(to='Department', verbose_name="部门")

    class Meta:
        verbose_name_plural = "员工信息表"

    def __str__(self):
        return self.name


class Department(models.Model):
    '''
    部门表
    '''
    name = models.CharField(max_length=32, verbose_name="部门名称")

    class Meta:
        verbose_name_plural = "部门表"

    def __str__(self):
        return self.name


class Company(models.Model):
    """
    有关付款公司，收款公司
    """
    name = models.CharField("公司名称", max_length=64)
    bank = models.CharField("账户银行", max_length=32)
    card_num = models.CharField("银行卡号", max_length=32)
    email = models.EmailField("邮箱", blank=True, null=True)

    class Meta:
        verbose_name_plural = "公司表"

    def __str__(self):
        return self.name


class Record(models.Model):
    """
    申请记录表,该记录表自动记录
    """
    apply_for = models.ForeignKey(verbose_name='流水号', to="BaseApply")
    apply_type=models.ForeignKey(verbose_name="表单类型",to="SecondType",null=True)#增加字段表单类型
    operate = models.ForeignKey(verbose_name='操作人', to=UserInfo)  # 自动获取

    status_choices = [
        (1, '已提交'),
        (2, '审核中'),
        (3, '未通过'),
        (4, '通过'),
        (5, '通过/已付款'),
        (6, '以归档'),
    ]

    note = models.CharField("备注", max_length=64, null=True)
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices)
    operate_time = models.DateTimeField(verbose_name="操作时间", auto_now_add=True)
    def __str__(self):
        return self.apply_for.apply_id


class BaseApply(models.Model):
    """
    所有申请表所要继承的父类
    """
    apply_id = models.CharField(verbose_name="流水单号", max_length=16, null=True,
                                blank=True)  # 4位随机字符串+今天日期（8位）自动生成12位不重复数字的字符串
    depart = models.ForeignKey(verbose_name="所属部门", to=Department)  # 申请部门多对多。自动获取,
    user = models.ForeignKey(verbose_name="申请人", to=User)  # 申请人自动获取,显示为用户姓名
    form = models.TextField(verbose_name="表单摘要", max_length=16)
    payer = models.ForeignKey(verbose_name="付款公司", to='Company', default=1)
    budget = models.IntegerField(verbose_name="金额")

    currency_type_choices = (
        (1, '人民币'),
        (2, '美元'),
    )

    currency_type = models.IntegerField(verbose_name="货币类型", choices=currency_type_choices, default=1)
    coin_capital = models.CharField(verbose_name="金额大写", max_length=64,null=True,blank=True)
    exigence_choices = (
        (1, "紧急"),
        (2, "不紧急"),
    )
    exigence = models.SmallIntegerField(verbose_name="紧急程度", choices=exigence_choices)
    true_or_false_choices = (
        (1, '是'),
        (2, '否')
    )
    def __str__(self):
        return str(self.apply_id)

class ApplyType(models.Model):
    """
    申请表类型,如 报批申请单 报销申请单
    """
    name = models.CharField("申请表类型",max_length=32,null=True)

    def __str__(self):
        return self.name

class SecondType(models.Model):
    """
    申请表具体类型,如 活动推广报批,日常需求采购报批..
    """
    name = models.CharField("申请表具体类型", max_length=32, null=True,blank=True)
    url = models.CharField("url",max_length=32, null=True,blank=True)
    base_type = models.ForeignKey(to="ApplyType",verbose_name="所属大类")
    def __str__(self):
        return self.name

class ActivityApply(BaseApply):
    """
    推广活动申请表
    """
    apply_type = models.ForeignKey(verbose_name="申请表类型", to="SecondType")
    apply_name = models.CharField(verbose_name="申请表名称", default="推广活动申请表", max_length=32, editable=False)
    product_name = models.CharField(verbose_name="推广产品名称", max_length=64)
    product_version = models.CharField(verbose_name="推广产品版本", max_length=64)
    advocate_platform = models.CharField(verbose_name="推广产品平台", max_length=32)
    advocate_des = models.TextField(verbose_name="推广方案描述", max_length=32)

    cause_choices = (
        (1, '提升收入'),
        (2, '提升在玩'),
        (3, '增加注册'),
        (4, '其他')
    )
    apply_cause = models.CharField(verbose_name="申请原因", choices=cause_choices, default=None, max_length=32)
    anticipate = models.TextField(verbose_name="预期效果")
    first_generalize = models.IntegerField(verbose_name="首次推广", choices=BaseApply.true_or_false_choices, default=1)
    before_result = models.TextField(verbose_name="以前效果描述", null=True, blank=True)
    buy_goods = models.IntegerField(verbose_name="需要申购物品", choices=BaseApply.true_or_false_choices, default=2)
    attachment = models.FileField(verbose_name="上传附件", upload_to='./upload/attachment/', null=True,
                                  blank=True)  # 上传的文件以当前订单订单号为文件夹
    note = models.CharField("备注", max_length=64, null=True)
    # apply_type_choices = [
    #     (1, '个人'),
    #     (2, '部门'),
    # ]
    # apply_type = models.SmallIntegerField('申请类型', choices=apply_type_choices)
