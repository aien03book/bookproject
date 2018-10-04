from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .modelsMR import MR
from django.core.files.storage import FileSystemStorage
# Create your views here.
mr =MR()
def index(request):
    title = "活動室"
    rooms = mr.all
    return render(request,'meetingroom/index.html',locals())
def calendar(request,id):
    return render(request,'meetingroom/calendar.html',locals())
def booking(request):
    # roomsingle = mr.single(id)
    return render(request,'meetingroom/booking.html',locals())