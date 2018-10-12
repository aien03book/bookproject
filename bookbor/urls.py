from django.urls import path
from . import views

#urlNamespace
app_name = "bookbor"

urlpatterns = [
     #http://localhost:8000/bookbor
    path('',views.index,name="index"),  #urlName
    
    path('bookinfo/<str:bookname>/',views.bookinfo1,name="bookinfo1"),
    path('bookbor/<str:bookname>/',views.bookbor,name="bookbor"),
    path('find/',views.find,name="find"),
    path('add/',views.add,name="add"),
    path('search/<str:name>/',views.search,name="search"),
    path('update/<int:id>/',views.update,name="update"),
    path('memberinfo/<str:memberid1>/',views.memberinfo,name="memberinfo"),
    path('member_bookinfo/<str:memberId>/',views.member_bookinfo,name="member_bookinfo"),
    path('scraw/',views.scraw,name="scraw"),
    ]