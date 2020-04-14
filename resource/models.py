from django.db import models


# Create your models here.
class Idc(models.Model):
    name = models.CharField(max_length=10, verbose_name='机房简称')
    name_cn = models.CharField(max_length=32, verbose_name='机房名称')
    address = models.CharField(max_length=64, verbose_name='机房地址')
    phone = models.CharField(max_length=11, verbose_name='机房座机电话')
    username = models.CharField(max_length=32, verbose_name='机房负责人姓名')
    username_email = models.CharField(max_length=32, verbose_name='机房负责人邮箱')
    username_phone = models.CharField(max_length=11, verbose_name='机房负责人手机号')

    class Meta:
        default_permissions = []
        permissions = (
            ('add_idc', '添加IDC'),
            ('show_idc', '查看IDC'),
            ('delete_idc', '删除IDC'),
            ('update_idc', '更新IDC'),
        )


class ServerUser(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称')
    username = models.CharField(max_length=32, verbose_name='系统用户')
    password = models.CharField(max_length=32, verbose_name='系统密码')
    info = models.TextField(verbose_name='备注')
    class Meta:
        default_permissions = []
        permissions = (
            ('add_serveruser', '添加资产用户'),
            ('show_serveruser', '查看资产用户'),
            ('delete_serveruser', '删除资产用户'),
            ('update_serveruser', '更新资产用户'),
        )