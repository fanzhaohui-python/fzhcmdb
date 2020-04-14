from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from dashboard.views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^admin/',admin.site.urls),
    # url(r'^indexa/', IndexView.as_view(), name='index'),
    url(r'^$', LoginView.as_view(), name='user_login'),
    # url(r'login', LoginView.asview()),
]
