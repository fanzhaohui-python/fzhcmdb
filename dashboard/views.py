from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


# Create your views here.
# class IndexView(View):
#     def get(self, request):
#         return render(request, 'index.html', {'body':'这是devops首页！'})

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['body'] = '这是devops首页！'
        return context


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        # print(request.POST)
        data = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        # 会自动连接数据库进行校验
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            data['status'] = 0
        else:
            data['status'] = 1
        return JsonResponse(data)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
