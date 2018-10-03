from django.urls import path
from . import views

app_name = "meetingroom"

urlpatterns = [
    #http://localhost:8000/meetingroom
    #views表示views.py的module
    #index表示views.py下的function
    path('',views.index,name="index"),  #urlName
    path('calendar',views.calendar,name="calendar"),  
    ]
    