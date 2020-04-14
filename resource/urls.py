from django.conf.urls import url, include
from resource.views import *



urlpatterns = [
    url(r'^idc/list/$', IdcListView.as_view(),name='idc_list'),
    url(r'^idc/add/$', IdcAddView.as_view(),name='idc_add'),
    url(r'^idc/update/$', IdcUpdateView.as_view(),name='idc_update'),
    url(r'^idc/delete/$', IdcDeleteView.as_view(),name='idc_delete'),
    url(r'^serveruser/list/$', ServerUserListView.as_view(), name='serveruser_list'),
    url(r'^serveruser/create/$', ServerUserCreateView.as_view(), name='serveruser_create'),
    url(r'^serveruser/delete/$', ServerUserDeleteView.as_view(), name='serveruser_delete'),
    url(r'^serveruser/update/$', ServerUserUpdateView.as_view(), name='serveruser_update'),
]