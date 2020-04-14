from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView
from resource.models import *
from django.http import *


# Create your views here.

class IdcListView(ListView):
    template_name = 'idc_list.html'
    model = Idc


class IdcAddView(TemplateView):
    template_name = 'idc_create.html'

    def post(self, request):
        print(request.POST)
        data = request.POST
        res = {'status': 0, 'msg': '创建成功！'}
        try:
            Idc.objects.create(
                name=data.get('name'),
                name_cn=data.get('name_cn'),
                address=data.get('address'),
                phone=data.get('phone'),
                username=data.get('username'),
                username_phone=data.get('username_phone'),
                username_email=data.get('username_email'),
            )
        except Exception as e:
            print(e)
            res['status'] = 1
            res['msg'] = '创建失败！'
        return JsonResponse(res)


class IdcUpdateView(TemplateView):
    template_name = 'idc_modify.html'

    def get_context_data(self, **kwargs):
        data = self.request.GET
        idc_id = data.get('id')
        context = super(IdcUpdateView, self).get_context_data(**kwargs)
        context['idc_obj'] = Idc.objects.get(id=idc_id)
        return context

    def post(self, requset):
        data = requset.POST
        res = {'status': 0, 'msg': '更新成功！'}
        print(data)
        idc_id = data.get('id')
        try:
            Idc.objects.filter(id=idc_id).update(
                name=data.get('name'),
                name_cn=data.get('name_cn'),
                address=data.get('address'),
                phone=data.get('phone'),
                username=data.get('username'),
                username_email=data.get('username_email'),
                username_phone=data.get('username_phone'),

            )
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '更新失败！'}
        return JsonResponse(res)


class IdcDeleteView(View):
    def post(self, request):
        res = {'status': 0, 'msg': '删除成功！'}
        try:
            Idc.objects.get(id=request.POST.get('id')).delete()
        except Idc.DoesNotExist:
            res = {'status': 1, 'msg': '机房不存在，删除失败！'}
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '发生未知错误，请联系管理员！'}
        return JsonResponse(res)


class ServerUserListView(ListView):
    template_name = 'serveruser_list.html'
    model = ServerUser


class ServerUserCreateView(TemplateView):
    template_name = 'serveruser_create.html'
    def post(self,request):
        res = {'status': 0, 'msg': '添加成功'}
        data = request.POST
        print(data)
        try:
            ServerUser.objects.create(
                name=data.get('name'),
                username=data.get('username'),
                password=data.get('password'),
                info=data.get('info')
            )
        except Exception:
            res = {'status': 1, 'msg': '添加失败！'}
        return JsonResponse(res)


class ServerUserDeleteView(View):
    def post(self,request):
        res = {'status': 0, 'msg': '删除成功！'}
        serveruser_id = request.POST.get('id')
        try:
            ServerUser.objects.get(id=serveruser_id).delete()
        except ServerUser.DoesNotExist:
            res = {'status': 1, 'msg': '此用户不存在，删除失败！'}
        except Exception:
            res = {'status': 1, 'msg':'未知错误，检票失败！'}
        return JsonResponse(res)


class ServerUserUpdateView(TemplateView):
    template_name = 'serveruser_modify.html'
    def get_context_data(self, **kwargs):
        serveruser_id = self.request.GET.get('id')
        context = super(ServerUserUpdateView,self).get_context_data(**kwargs)
        context['serveruser_obj'] = ServerUser.objects.get(id=serveruser_id)
        return context

    def post(self, request):
        print(request.POST)
        res = {'status': 0, 'msg': '更新成功！'}
        data = request.POST
        print(data)
        serveruser_id = data.get('id')
        try:
            ServerUser.objects.filter(id=serveruser_id).update(
                name = data.get('name'),
                username = data.get('username'),
                password = data.get('password'),
                info = data.get('info')

            )
        except Exception:
            res = {'status': 1, 'msg': '更新失败！'}
        return JsonResponse(res)