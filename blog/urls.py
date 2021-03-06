#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    # name='post_list'는 URL에 이름을 붙인 것
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]