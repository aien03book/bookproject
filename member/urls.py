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

    #http://localhost:8000/member/hello
    path('hello/',views.hello,name="hello"),
     #http://localhost:8000/show/
    path('show/',views.show),
    path('ajax/',views.ajax,name="ajax"),
     #http://localhost:8000/member/update/1
    path('checkin/', views.index, name="index"),
    #http://localhost:8000/member/captcha/
    path('captcha/', views.captcha, name="captcha"),
    
    
  
]