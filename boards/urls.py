from django.urls import path
from . import views

#urlNamespace
app_name = "boards"

urlpatterns = [
    #http://localhost:8000/boards
    path('',views.index,name="index"),  #urlName
    #http://localhost:8000/boards/post
    path('post/',views.post,name="post")

]