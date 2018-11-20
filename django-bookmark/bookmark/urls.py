from django.urls import path, re_path

from bookmark import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.bookmark_list, name='bookmark list'),
    re_path(r'(?P<pk>[0-9]+)/$', views.bookmark_detail, name="bookmark detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
