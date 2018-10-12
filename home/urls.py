from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from todo import views
from home import views
from . import views

router = DefaultRouter()
router.register('todo', views.TodoViewSet)
router.register('bookpool', views.BookpoolViewSet)
router.register('bookcate', views.BookcateViewSet)

app_name = "home"
urlpatterns = [
    #http://localhost:8000
    path('',views.index,name="index"),  #urlName
    #views表示views.py的module
    #index表示views.py下的function
    # path('about/',views.about,name="about"),
    # path('about/<str:type>',views.about1,name="about1"),
    # path('contact/',views.contact,name="contact"),
    path('main/',views.main),
    #http://localhost:8000/member/delete/1
    path('delete/<int:id>',views.delete,name="delete"),

    # http://localhost:8000/member/update/1

    path('update/<int:id>', views.update, name="update"),
    path('create/', views.create, name="create"),
    path('chart/', views.chart, name="chart"),
    # path('show/<int:id>', views.show, name="show"),

    path('api/', include(router.urls)),
    # path('jquery/',include('jquery.urls')),

    # path('/<int:id>', views.update, name="update"),
    #     #http://localhost:8000/member/delete/1

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

