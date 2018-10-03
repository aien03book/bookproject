from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .modelsMR import MR
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):
    title = "活動室"
    mr =MR()
    rooms = mr.all
    return render(request,'meetingroom/index.html',locals())
def calendar(request,id):
    return render(request,'meetingroom/calendar.html',locals())
def calendar1(request,id):
    return render(request,'meetingroom/calendar1.html',locals())