from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from member.models import Members
from .modelsmember import Member
import datetime
from django.core import serializers
#建立物件
member = Member()

# Create your views here.
def index(request):  
    title = "會員資料"
    # with connection.cursor() as cursor:
    #     sql = """select * from members"""
    #     cursor.execute(sql)
    #     members = cursor.fetchall()
    # return render(request,'member/index.htm',locals())
    #呼叫方法
    members = member.all()
    return render(request,'member/index.htm',locals())

def login(request):  
    # title = "會員登入"
    if request.method =="POST":
        email = request.POST["email"]    
        password = request.POST["password"] 
        theMember=Members.objects.filter(email=email,password=password).values('name')
        if theMember:
            if 'url' in request.GET:
                theUrl=request.GET["url"]
            else:
                theUrl="/"
            name=theMember[0]['name']
            strJS = "<script>alert('登入成功');location.href='" + theUrl + "'</script>"
            response = HttpResponse(strJS)
            
            remember = None
            if 'remember' in request.POST.keys():
                # remember = request.POST["remember"]
                expiresdate= datetime.datetime.now() + datetime.timedelta(days=7)
                response.set_cookie('name',name,expires=expiresdate)
            else:    
                response.set_cookie('name',name)
            return response
        else:
            return HttpResponse("<script>alert('登入失敗');location.href='/member/login'</script>") 
    return render(request,'member/login.htm',locals())

def logout(request):
    back = HttpResponse("<script>location.href='/'</script>")
    back.delete_cookie('name')
    return back

def register(request):  
    # title = "會員註冊"
    if request.method == "POST":
        #接收表單傳過來的資料
        name = request.POST["name"]
        email = request.POST["email"]  #w124@gmail.com
        password = request.POST["password"]  
        checkpassword = request.POST["checkpassword"] 
        age = request.POST["age"] 

        if password == checkpassword:
            #將資料寫進資料庫
            with connection.cursor() as cursor:
                sql = """insert into members(name,email,password,age)
                        values(%s,%s,%s,%s)"""
                #tuple
                cursor.execute(sql,(name,email,password,age))
            # _member = (name,email,password,age)
            # member.create(_member)
            #轉到會員的首頁上
            return redirect("/")
        else:
            return HttpResponse("<script>alert('驗證密碼不符');location.href='/member/register'</script>") 
        
    return render(request,'member/register.htm',locals())

def delete(request, id):
    # with connection.cursor() as cursor:
        # sql = """delete from members where id=%s"""
        #tuple
        # cursor.execute(sql,(id,))
    member.delete(id)
    return redirect("/member/")
    

    # return HttpResponse("<h2>" + str(id) + "</h2>")

def update(request, id):
    #步驟二
    if request.method == "POST":
        #接收表單傳過來的資料
        name = request.POST["name"]
        email = request.POST["email"]  #w124@gmail.com
        password = request.POST["password"]  
        age = request.POST["age"] 

        #將資料寫進資料庫
        with connection.cursor() as cursor:
            sql = """update members set name=%s,email=%s,password=%s,age=%s
                     where id=%s"""
            #tuple
            cursor.execute(sql,(name,email,password,age,id))
        # _member = (name,email,password,age,id)
        # member.update(_member)
        #轉到會員的首頁上
        return redirect("/member/")

    #步驟一
    with connection.cursor() as cursor:
        sql = """select * from members where id=%s"""
        #tuple
        cursor.execute(sql,(id,))
        member = cursor.fetchone()
    # membersingle = member.single(id)
    return render(request,'member/update.htm',locals())

def show(request):
    data=serializers.serialize("json",Members.objects.all())
    return HttpResponse(data,content_type="applications/json")

def checkname(request,name):
    result = Members.objects.filter(name = name)
    cm = "0"
    if result:
        cm = "1"
    return HttpResponse(cm)

def checkemail(request,email):
    result = Members.objects.filter(email = email)
    cm = "0"
    if result:
        cm = "1"
    return HttpResponse(cm)