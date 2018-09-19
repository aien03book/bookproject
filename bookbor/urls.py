from django.urls import path
from . import views
#urlNamespace
app_name = "bookbor"

urlpatterns = [
     #http://localhost:8000/bookbor
    # path('',views.index,name="index"),  #urlName
    path('bookinfo/',views.bookinfo,name="bookinfo"),
    ]