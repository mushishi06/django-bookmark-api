from django.urls import path, re_path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.category_list, name='category list'),
    re_path(r'(?P<pk>[0-9]+)/$', views.category_detail, name="category detail"),
    re_path(r'(?P<pk>[a-zA-Z]+)/$', views.category_search, name="category Search"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
