from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.core.files.storage import FileSystemStorage
from django.utils.encoding import smart_str
import base64, datetime
from django.core import serializers

from .serializers import TodoSerializer
from home.serializers import BookpoolSerializer
from home.serializers import BookcateSerializer

from rest_framework import viewsets
from home import views

from .models import Todo
from .models import Bookpool
from .models import Bookcate
from .modelsdef import Book


# Create your views here.

class BookpoolViewSet(viewsets.ModelViewSet):
    queryset = Bookpool.objects.all()
    serializer_class = BookpoolSerializer

class BookcateViewSet(viewsets.ModelViewSet):
    queryset = Bookcate.objects.all()
    serializer_class = BookcateSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

book=Book()

def main(request):  
    return redirect("/")

def index(request):  
    title = "書籍採購"
    books = book.all()
    return render(request,'home/index.html',locals())

def delete(request, id):
    book.delete(id)
    return redirect("/")

def create(request):
    btntext =" 新 增"
    if request.method == "POST":
        bookcate = request.POST["selected"]
        bookid = request.POST['bookid']
        bookname = request.POST["bookname"]
        author=request.POST["author"]
        issuedate = request.POST["issuedate"]  
        buydate = request.POST["buydate"] 
        whoissue = request.POST["whoissue"] 
        # print(bookid)
        if request.FILES["bookimg01"]:
            #檔案上傳到media資料夾中
            myFile = request.FILES["bookimg01"]
            fs = FileSystemStorage()
            bookimg01 = fs.save(myFile.name,myFile)
            # file name 上傳到sql中
            # bookimg01 = request.POST["bookimg01"]  
            _book = (bookid, bookcate, bookname, author, issuedate, buydate, whoissue, bookimg01)
            book.create(_book)
            # print(bookimg01)
            # _book=(bookimg01)
            # book.create(_book)

        return redirect("/home/")

    # booksingle = book.single(id)
    bookcates = book.cateall()
    return render(request,'home/create.html', locals())

def update(request, id):
    btntext = " 修 改"
    if request.method == "POST" :
        bookname = request.POST["bookname"]
        author=request.POST["author"]
        issuedate = request.POST["issuedate"]  
        buydate = request.POST["buydate"] 
        whoissue = request.POST["whoissue"] 
        _book = (bookname, author, issuedate, buydate, whoissue, id)
        book.update(_book)

        if request.FILES["bookimg01"]:
        #     #檔案上傳到media資料夾中
            myFile = request.FILES["bookimg01"]
            fs = FileSystemStorage()
            bookimg01 = fs.save(myFile.name, myFile)
        #     # bookimg01 = request.POST["bookimg01"] 
            _book=(bookimg01, id)
            book.updateimg(_book)
        
        return redirect("/home/")
 
    booksingle = book.single(id)
    return render(request,'home/update.html',locals())

def chart(request):
    if request.method == "POST" :
        return redirect("/home/")
    return render(request,'home/chart.html', locals())
# def show(request):
#    datas = serializers.serialize("json", bookpool.objects.all())
#    return HttpResponse(datas, content_type="ProductsAll/json")
