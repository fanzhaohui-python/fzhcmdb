# Generated by Django 2.2 on 2020-04-02 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'default_permissions': [], 'permissions': (('add_user', '添加用户'), ('delete_user', '删除用户'), ('show_user', '查看用户'), ('update_user', '修改用户'))},
        ),
    ]
