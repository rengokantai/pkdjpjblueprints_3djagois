"""pkdjpjblueprints_3djagois URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from data_collector.views import StatusView,AlertListView,NewAlertView,EditAlertView,DeleteAlertView,RecordDataApiView

from django.views.decorators.csrf import csrf_exempt

# new for remote connection

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',StatusView.as_view() ,name='status'),
    url(r'^alerts/$',AlertListView.as_view() ,name='alerts_list'),
    url(r'^alerts/new/$',NewAlertView.as_view() ,name='alerts_new'),
    url(r'^alerts/(?P<pk>\d+)/edit/$',EditAlertView.as_view() ,name='alerts_edit'),
    url(r'^alerts/(?P<pk>\d+)/delete/$',DeleteAlertView.as_view() ,name='alerts_delete'),
    url(r'^record/$',csrf_exempt(RecordDataApiView.as_view()) ,name='record_data'),
]
