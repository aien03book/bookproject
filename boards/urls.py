from django.urls import path
from . import views

#urlNamespace
app_name = "boards"

urlpatterns = [
    #http://localhost:8000/boards
    path('',views.site,name="site"),  #urlName
    #http://localhost:8000/boards/post
    path('post/',views.post,name="post"),
    #http://localhost:8000/boards/delete
    path('remove/<int:id>',views.remove,name="remove"),
    #http://localhost:8000/boards/update
    path('update/<int:id>',views.update,name="update"),
]