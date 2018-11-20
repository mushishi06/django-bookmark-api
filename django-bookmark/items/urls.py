from django.urls import path, re_path

from items import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.item_list, name='Item list'),
    re_path(r'(?P<pk>[0-9]+)/$', views.item_detail, name="Item detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
