from django.http import JsonResponse
from django.views.generic import View, TemplateView, ListView
from users.models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
# class UserListView(TemplateView):
#     template_name = 'user_list.html'
#     # def get(self, request):
#     #     return render(request, 'user_list.html')
#     def get_context_data(self, **kwargs):
#         content = super(UserListView,self).get_context_data(**kwargs)
#         content['userList']=User.objects.all()
#         return content
class UserListView(ListView):
    template_name = 'user_list.html'
    model = User
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(UserListView, self).get_context_data(**kwargs)
        content['page_range'] = self.page_range(content['page_obj'], content['paginator'])
        print(content)
        return content

    def page_range(self, page_obj, paginator):
        current_index = page_obj.number
        start = current_index - 2
        end = current_index + 3
        if start <= 1:
            start = 1
        if end >= paginator.num_pages:
            end = paginator.num_pages + 1
        current_pages_num = end - start
        if (end == paginator.num_pages + 1):
            start = start - (5 - current_pages_num)
        else:
            if current_pages_num < 5:
                end = end + (5 - current_pages_num)
        return range(start, end)


class TestDataView(View):
    def get(self, request):
        for i in range(0, 100):
            user = User()
            profile = Profile()
            user.username = '测试{}'.format(i)
            user.password = make_password('123456')
            user.email = '{}.qq@com'.format(i)
            user.save()
            profile.profile_id = user.id
            profile.name_cn = '用户{}'.format(i)
            profile.wechat = 'wechat_user{}'.format(i)
            profile.phone = '1333333333{}'.format(i)
            profile.info = '测试用户{}'.format(i)
            profile.save()


class UserAddView(TemplateView):
    template_name = 'user_add.html'
    # @method_decorator(login_required)
    # @method_decorator(permission_required('user.add_user'))
    # def get(self, request, *args, **kwargs):
    #     context = super(UserAddView,self).get_context_data()
    #     return context
    def post(self, request):
        print(request.POST)
        res = {'status': 0, 'msg': '创建成功'}
        # 添加数据
        try:
            user = User.objects.create(
                username=request.POST.get('username'),
                password=make_password(request.POST.get('password')),
                email=request.POST.get('email')
            )
            profile = Profile.objects.create(
                profile_id=user.id,
                name_cn=request.POST.get('name_cn'),
                phone=request.POST.get('phone'),
                wechat=request.POST.get('wechat')
            )

            print(user.username)
            print(type(user.username))

            print(user.password)
            print(type(user.password))
            print(user.email)
            print(type(user.email))

            print(profile.name_cn)
            print(type(profile.name_cn))
            # profile.info = request.POST.get('name_cn')
            print(type(profile.wechat))
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '添加失败'}
        print(res)
        return JsonResponse(res)


class UserUpdateView(TemplateView):
    # def get(self,request):
    #     return render(request, 'user_update.html', {'user_obj':User.objects.get(id=request.GET.get('id'))})

    template_name = 'user_update.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        uid = self.request.GET.get('uid')
        context['user_obj'] = User.objects.get(id=uid)
        return context

    def post(self, request):
        res = {'status': 0, 'msg': '更新成功'}
        uid = request.POST.get('uid')
        print(uid)
        try:
            User.objects.filter(id=uid).update(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                email=request.POST.get('email')
            )
            Profile.objects.filter(profile=uid).update(
                name_cn=request.POST.get('name_cn'),
                phone=request.POST.get('phone'),
                wechat=request.POST.get('wechat')
            )
        except Exception:
            res = {'status': 1, 'msg': '更新失败'}
        return JsonResponse(res)


class UserDeleteView(View):

    def get(self, request):
        uid = request.GET.get('uid')
        res = {'status': 0, 'msg': '删除成功'}
        try:
            User.objects.get(id=uid).delete()
            print(User.DoesNotExist)
        except User.DoesNotExist:
            res = {'status': 1, 'msg': '用户不存在，删除失败。'}
        except Exception:
            res = {'staus': 1, 'msg': '未知错误，请联系管理员。'}
        return JsonResponse(res)


class UserStatusView(View):
    def get(self, request):
        uid = request.GET.get('uid')
        res = {'status': 0, 'msg': '更新状态成功'}
        user = User.objects.filter(id=uid)
        username = user[0].username
        print(user[0].is_active)
        if user[0].is_active:
            update_status = 0
            res['msg'] = username + '禁用成功'
        else:
            update_status = 1
            res['msg'] = username + '启用成功'
        try:
            rs = user.update(
                is_active=update_status
            )
            print(rs)
        except User.DoesNotExist:
            res = {'status': 1, 'msg': '用户不存在，更新失败'}
        except Exception:
            res = {'status': 1, 'msg': '未知错误更新失败'}
        return JsonResponse(res)


class GroupListView(ListView):
    template_name = 'group_list.html'
    model = Group
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(GroupListView, self).get_context_data(**kwargs)
        content['page_range'] = self.page_range(content['page_obj'], content['paginator'])
        return content

    def page_range(self, page_obj, paginator):
        current_index = page_obj.number
        start = current_index - 2
        end = current_index + 3
        if start < 1:
            start = 1
        if end > paginator.num_pages + 1:
            end = paginator.num_pages + 1
        return range(start, end)


class GroupAddView(ListView):
    template_name = 'group_add.html'
    model = User

    def post(self, request):
        res = {'status': 0, 'msg': '创建成功'}
        try:
            group = Group.objects.create(
                name=request.POST.get('name')
            )
            for i in request.POST.getlist('group_user'):
                group.user_set.add(User.objects.get(id=i))
        except Exception:
            res['status'] = 1
            res['msg'] = '创建失败'
        return JsonResponse(res)


class GroupUpdateView(TemplateView):
    template_name = 'group_update.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        gid = self.request.GET.get('id')
        print(self.request.GET)
        context['group_obj'] = Group.objects.get(id=gid)
        context['user_list'] = User.objects.all()
        return context

    def post(self, request):
        res = {'status': 0, 'msg': '更新成功'}
        gid = request.POST.get('gid')
        Group.objects.filter(id=gid).update(
            name=request.POST.get('name')
        )
        group_obj = Group.objects.get(id=gid)
        group_obj.user_set.clear()
        for i in request.POST.getlist('group_user'):
            group_obj.user_set.add(User.objects.get(id=i))
        return JsonResponse(res)


class GroupDeleteView(View):
    def get(self, request):
        gid = request.GET.get('gid')
        print(gid)
        res = {'status': 0, 'msg': '删除成功！'}
        try:
            Group.objects.get(id=gid).delete()
            print(Group.DoesNotExist)
        except Group.DoesNotExist:
            res = {'status': 1, 'msg': '用户组不存在，删除失败！'}
        except Exception:
            res = {'status': 1, 'msg': '未知错误，请联系管理员！'}
        return JsonResponse(res)


class PermListView(ListView):
    template_name = 'perm_list.html'
    model = Permission
    paginate_by = 7

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     content = super(PermListView, self).get_context_data(**kwargs)
    #     content['page_range'] = self.page_range(content['page_obj'],content['paginator'])
    #     return content
    def get_queryset(self):
        queryset = super(PermListView, self).get_queryset()
        # queryset['page_range'] = self.page_range(queryset['page_obj'], queryset['paginator'])
        queryset = queryset.exclude(name__regex='[a-zA-Z0-9]')
        return queryset

    def page_range(self, page_obj, paginator):
        current_index = page_obj.number
        start = current_index - 2
        end = current_index + 3
        if start < 1:
            start = 1
        if end > paginator.num_pages + 1:
            end = paginator.num_pages + 1
        return range(start, end)


class UserSetPermView(ListView):
    template_name = 'user_set_perm.html'
    model = Permission
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        uid = self.request.GET.get('id')
        context = super(UserSetPermView, self).get_context_data(**kwargs)
        context['user_obj'] = User.objects.get(id=uid)
        return context

    def get_queryset(self):
        queryset = super(UserSetPermView, self).get_queryset()
        queryset = queryset.exclude(name__regex='[a-zA-Z0-9]')
        return queryset

    def post(self, request):
        res = {'status': 0, 'msg': '设置成功'}
        uid = request.POST.get('uid')
        # data = request.POST
        # print(data)
        # try:
        #     user = User.objects.get(id=data.get('uid'))
        #     user.user_permissions = data.getlist('perm_list')
        #     user.save()
        # except Exception as e:
        #     print(e)
        #     res = {'status': 1, 'msg': '设置失败'}
        # return JsonResponse(res)
        try:
            user = User.objects.get(id=uid)
            user.user_permissions.clear()
            pe_list = request.POST.getlist('perm_list[]')
            for i in pe_list:
                user.user_permissions.add(i)
            user.save()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '设置失败'}
        return JsonResponse(res)
