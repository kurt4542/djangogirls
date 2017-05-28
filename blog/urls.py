#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    # name='post_list'는 URL에 이름을 붙인 것
    url(r'^$', views.post_list, name='post_list'),
]