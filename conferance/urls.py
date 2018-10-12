from django.urls import path
from django.conf.urls import url
from . import views

app_name = "conferance"

urlpatterns = [
    #http://localhost:8000/conferance   
    url(r'^$', views.list, name='list'),#所有會議室
    url(r'^(?P<id>[0-9]+)/$', views.appointment, name='appointment'),#單獨會議室預約情況
    url(r'^(?P<id>[0-9]+)/add/$', views.add, name='add'),
    url(r'^(?P<room_id>[0-9]+)/(?P<order_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<room_id>[0-9]+)/(?P<order_id>[0-9]+)/update/$', views.update, name='update')
    ]
    