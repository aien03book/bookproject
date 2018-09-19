from django.urls import path
from homepage import views
app_name="homepage"
urlpatterns = [
    path('',views.index,name="index"),
    # path('',views.index,name="index"),  #urlName
    #views表示views.py的module
    #index表示views.py下的function
    path('ourteam/',views.ourteam,name="ourteam"),
    path('checkin/',views.checkin,name="checkin"),
    path('register/',views.register,name="register"),
    path('login/',views.checkin,name="login"),
    
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
    
    
]
