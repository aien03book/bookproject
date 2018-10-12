from django.urls import path
from . import views

#urlNamespace
app_name = "boards"

urlpatterns = [
    #http://localhost:8000/boards
    path('',views.site,name="site"),  #urlName
    #http://localhost:8000/boards/post
    path('post/',views.post,name="post"),
    #http://localhost:8000/boards/checkid
    path('checkid/<int:id>/',views.checkid,name="checkid"),
    #http://localhost:8000/boards/update
    path('update/<int:id>',views.update,name="update"),
    #http://localhost:8000/boards/chart
    path('chart/',views.chart,name="chart"),
    #http://localhost:8000/boards/count
    path('count/',views.count,name="count"),



    #以下路徑無用
    #http://localhost:8000/boards/remove
    # path('remove/<int:id>',views.remove,name="remove"),
    #http://localhost:8000/boards/searchall
    #path('searchall/',views.searchall,name="searchall"),
    # http://localhost:8000/boards/searchone
    # path('searchone/<str:searchone>',views.searchone,name="searchone"),
    
]