from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    name_cn = models.CharField(max_length=32, verbose_name='中文名')
    wechat = models.CharField(max_length=32, verbose_name='微信')
    phone = models.CharField(max_length=32, verbose_name='电话')
    info = models.TextField(verbose_name='备注')
    class Meta:
        default_permissions = []
        permissions = (
            ('add_user','添加用户'),
            ('delete_user', '删除用户'),
            ('show_user', '查看用户'),
            ('update_user', '修改用户')
        )