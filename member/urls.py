from django.urls import path
from . import views

#urlNamespace
app_name = "member"

urlpatterns = [
    #http://localhost:8000/member
    path('',views.index,name="index"),  #urlName
    #views表示views.py的module
    #index表示views.py下的function
    #http://localhost:8000/member/login
    path('login/',views.login,name="login"),    
    path('logout/',views.logout,name="logout"),
    #http://localhost:8000/member/register
    path('register/',views.register,name="register"),
    #http://localhost:8000/member/delete/1
    path('delete/<int:id>',views.delete,name="delete"),
    #http://localhost:8000/member/update/1
    path('update/<int:id>', views.update, name="update"),
     #http://localhost:8000/show/
    path('show/',views.show),
     #http://localhost:8000/member/update/1
    path('checkin/', views.index, name="index"),
    path('check/<str:name>/',views.checkname,name="checkname"),
    path('check/<str:email>/',views.checkemail,name="checkemail"),
  
]