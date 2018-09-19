from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    title = "活動室"
    return render(request,'meetingroom/index.html',locals())