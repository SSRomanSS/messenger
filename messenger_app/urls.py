from django.urls import path, re_path
from .api import views

urlpatterns = [
    path('messages/list/', views.MessageListView.as_view(), name=None),
    re_path(r'^messages/list/(?P<gid>\d+)', views.PaginateListView().as_view(), name=None),
    path('test_message/', views.MessagePost().as_view()),
]
