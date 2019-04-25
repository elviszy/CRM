from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerInfo(models.Model):
    '''客户信息表'''
    name = models.CharField('姓名',max_length=64,default=None)
    user = models.ForeignKey(to="UserProfile",to_field="id")
    create_date = models.DateField('受理日期',auto_now_add=True)
    cert_num = models.CharField('身份证号',max_length=128,blank=True,null=True)
    sex_choices = ((0, '男'), (1, '女'))
    sex = models.PositiveSmallIntegerField(choices=sex_choices, verbose_name='性别', blank=True, null=True)
    contact = models.CharField('联系电话', max_length=64, unique=True)
    agency = models.CharField('中介',max_length=128,blank=True,null=True)
    agency_fee = models.IntegerField('中介费用')
    charges = models.IntegerField('收费标准')
    company_fee = models.IntegerField('公司费用')
    charge_amount = models.IntegerField('收费金额')
    success_date = models.DateTimeField('完成日期',blank=True,null=True)
    connect_detail = models.TextField('办理详情', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name


class Records(models.Model):
    nid = models.ForeignKey(to="CustomerInfo",to_field="id",null=True,blank=True,related_name="content")
    user = models.ForeignKey(to="UserProfile",to_field="id")
    content = models.CharField(max_length=255,null=True,blank=True) #评论内容

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '跟进记录'
        verbose_name_plural = verbose_name


class UserProfile(AbstractUser):
    '''用户表'''

    name = models.CharField(null=True, unique=True,blank=True,max_length=64,verbose_name="姓名")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
