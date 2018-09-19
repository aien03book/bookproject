from django.urls import path
from . import views

#urlNamespace
app_name = "store"

urlpatterns = [
    #http://localhost:8000/boards
    path('',views.index,name="index"),  #urlName
    #http://localhost:8000/store
    # path('create/',views.create,name="create")

]