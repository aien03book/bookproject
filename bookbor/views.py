from django.shortcuts import render, redirect
from django.db import connection
from bookbor.models import Bookpool
from bookbor.models import Bookrecord

# from  member.models  import Members
from  bookbor.models  import Members

from .modelsbookbor import Book
from django.http import HttpResponse
from datetime import datetime,timedelta
from django.core import serializers
from django.utils.encoding import smart_str
from django.core import serializers
import json
from django.core.files.storage import FileSystemStorage
from . models import Bookpool,Bookrecord
import time
from . import jsonDateTime as jd 
from django.db import models

import pytz
from pytz import timezone
# ------
import urllib.request as UR 
import urllib.parse as UP
import requests 
from bs4 import BeautifulSoup

import re
time=time.sleep(2)
# -------

# from django.forms.models import model_to_dict
# from django.contrib.auth.models import User
#建立物件

book=Book()
def bookinfo1(request,bookname):  
    title = "書籍資訊"
    bookinfo=serializers.serialize("json",Bookpool.objects.filter(bookname__icontains=bookname))
    bookinfo2=json.loads(bookinfo)
    for info in bookinfo2:
        print(info)
        bookname=(info['fields']['bookname'])
        author=(info['fields']['author'])
        publisher=(info['fields']['publisher'])
        issuedate=(info['fields']['issuedate'])
        ISBN=(info['fields']['isbn'])
        description=(info['fields']['description'])
        bookimage=(info['fields']['bookimage'])
        return render(request,'bookbor/bookinfo1.htm',locals())

def memberinfo(request,memberid1):  
    title = "會員資料"
    
    theId=request.COOKIES["memberId"]  
    memberinfo=serializers.serialize("json",Members.objects.filter(memberid=theId))
    # memberinfo=Members.objects.all()
    # print(memberinfo)
    

    memberinfo=json.loads(memberinfo)
    # return HttpResponse(memberinfo,content_type="application/json")
    name=memberinfo[0]['fields']['name']
    email=memberinfo[0]['fields']['email']
    joindate=memberinfo[0]['fields']['joindate'][:10]
    memberId=memberinfo[0]['fields']['memberid']
    
    return render(request,'bookbor/memberinfo.htm',locals())
    

def index(request):  
    title = "查找書籍"    
    current_time= str(datetime.now())[:19]
    return render(request,'bookbor/index.htm',locals())    

def find(request):
    title = "可借書籍"
    bookall=Bookpool.objects.all()
    return render(request,'bookbor/bookbor.htm',locals())

def search(request,name):
    title = "查找結果"
    bookp=serializers.serialize("json",Bookpool.objects.filter(bookname__icontains=name))
    return HttpResponse(bookp,content_type="application/json")
        
def add(request):  
    title = "新增書目"
     
    if request.method == "POST":
        #接收表單傳過來的資料
        bookname = request.POST["bookname"]
        author = request.POST["author"]  #w124@gmail.com
        issuedate = request.POST["issuedate"]  
        publisher = request.POST["publisher"] 
        ISBN = request.POST["ISBN"]
        #上傳書籍的圖片到media資料庫中
        myMedia=request.FILES["bookimage"]
        #上傳之前先建立一個暫存資料夾物件
        fs=FileSystemStorage()
        # #把資料存到該文件夾中
        bookimage=fs.save(myMedia.name,myMedia)
        # #將資料寫進資料庫
        # try:
        #     Bookpool.objects.create(bookname=bookname,author=author,issuedate=issuedate,publisher=publisher,isbn=ISBN,bookimage=bookimage)
        # except Error:
            # pass
            
        # with connection.cursor() as cursor:
        #     sql = """insert into bookpool(bookname,author,issuedate,publisher,ISBN)
        #              values(%s,%s,%s,%s,%s)"""
        #     #tuple
        #     cursor.execute(sql,(bookname,author,issuedate,publisher,ISBN))
        return redirect("/bookbor/find/")
   
        
    return render(request,'bookbor/newbook.htm',locals())
def update(request, id):
    #步驟二
    if request.method == "POST":
        #接收表單傳過來的資料
        author = request.POST["author"]
        bookname = request.POST["bookname"]  #w124@gmail.com
        issuedate = request.POST["issuedate"]  
        publisher = request.POST["publisher"] 

        #將資料寫進資料庫
        with connection.cursor() as cursor:
            sql = """update bookpool set author=%s,bookname=%s,issuedate=%s,publisher=%s
                     where id=%s"""
            #tuple
            cursor.execute(sql,(author,bookname,issuedate,publisher,id))
        
        #轉到會員的首頁上
        return redirect("/bookbor/")

    #步驟一
    with connection.cursor() as cursor:
        sql = """select * from bookpool where id=%s"""
        #tuple
        cursor.execute(sql,(id,))
        book = cursor.fetchone()
    # membersingle = member.single(id)
    return render(request,'bookbor/newbook1.htm',locals())


# def nice(x):
#     print('------\n\n')
#     print(x)
#     print('------\n\n')

def bookbor(request,bookname):
    if 'name' not in request.COOKIES:        
        theUrl = request.path
        print(theUrl)
        response= "<script>alert('借閱前請先登錄');location.href='/member/login/?url="+ theUrl +"'</script>"
        return HttpResponse(response)
    else:
        # 步驟一將要借的書的bookid、memberId新增至bookbor表格中
        # bookid=str(json.loads(serializers.serialize("json",Bookpool.objects.filter(bookname=bookname)))[0]['fields']['bookid'])
        bookid=str(json.loads(serializers.serialize("json",Bookpool.objects.filter(bookname=bookname)))[0]['pk'])
        memberid1=str(request.COOKIES['memberId'])
        memberid2=str(request.COOKIES['id1'])    
        # print(memberid1) 
        # localtz = timezone('Asia/Taipei')
        current_time = datetime.now()
        # current_time = datetime.now().strftime("%Y-%m-%d")
        return_time = str(datetime.now() + timedelta(days=60))
        print(current_time)
        # return_time = return_time.strftime("%Y-%m-%d")
 
    
        # d = datetime.utcnow()
        # d = pytz.utc.localize(d)

        # est = pytz.timezone('Asia/Taipei')
        # d = est.normalize(d)
        
        # current_time = localtz.localize(current_time)
        # return_time = localtz.localize(return_time)

        
        
        Bookrecord.objects.create(borrowtime=current_time,returntime=return_time,bookid=Bookpool.objects.get(id=bookid), memberid=Members.objects.get(memberid=memberid1))
        # Bookrecord.objects.create(borrowtime='2018-10-12')
        

        response= "<script>alert('確定借閱?書名為 "+bookname+" 的書');location.href='/bookbor/memberinfo/"+memberid1+"'</script>"
        return HttpResponse(response)
    return redirect('/bookbor/memberinfo/"+memberid1+"')

def member_bookinfo(request,memberId):
    title = "會員借書紀錄"
    id1=str(json.loads(serializers.serialize("json",Members.objects.filter(memberid=memberId)))[0]['pk'])
    # bookId=str(json.loads(serializers.serialize("json",Bookpool.objects.filter(bookname=bookname)))[0]['fields']['bookid'])
    bookrecord=Bookrecord.objects.filter(memberid=id1).values('bookid_id__bookname',"borrowtime","returntime")
    bookrecord= json.dumps(list(bookrecord),cls=jd.DateTimeEncoder)
   
    return HttpResponse(bookrecord,content_type="application/json")

def scraw(request):
    url="https://www.books.com.tw/web/sys_saletopb/books"

    header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    URL=requests.get(url,headers=header)
    soup=BeautifulSoup(URL.text,'lxml')
    bookname=soup.select('li.item')
    
     
    for book in bookname:  
              
        bookname=book.h4.string  
        author=book.li.a.string    
        bookimage=book.img.get('src')         
        
        Bookpool.objects.create(bookname=bookname,author=author,bookimage=bookimage)
    
    return redirect("/bookbor/")
