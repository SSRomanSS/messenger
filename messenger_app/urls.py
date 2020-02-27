# -*- coding: utf-8 -*-

from django.urls import path, re_path
from .api import views

urlpatterns = [
    path('messages/list/', views.MessageListView.as_view(), name=None),
    re_path(r'^messages/list/(?P<page_num>\d+)', views.PaginateListView().as_view(), name=None),
    path('messages/post_message/', views.MessagePost().as_view()),
    re_path(r'messages/single/(?P<slug>\d+)', views.SingleMessageGet.as_view(), name=None),
]