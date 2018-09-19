from django.shortcuts import render, redirect

def bookinfo(request):  
    title = "書籍資訊"
    
    return render(request,'bookbor/bookinfo.htm',locals())