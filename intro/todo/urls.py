from django.conf.urls import url

from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newtodo/$', views.newtodo, name='newtodo'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<pk>\d+)$', views.edit, name='edit'),
]