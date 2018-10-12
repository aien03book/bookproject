from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.db import connection
# Create your views here.
def index(request):
    return render(request,'homepage/index.htm')

    

def ourteam(request):
    title = "OUR TEAM"
    return render(request,'homepage/ourteam.htm',locals())
# def register(request):
#     title = "我要登入"
#         return render(request,'homepage/register.htm',{'title':'註冊'})
def checkin(request):
    title = "我要登入"
    with connection.cursor() as cursor:
        sql="""select * from members"""
        cursor.execute(sql)
        member=cursor.fetchall()
    # print(member)
    return render(request,'homepage/checkin.htm',locals())

def register(request):
    title = "會員註冊"
    if request.method == "POST":
        #接收表單傳過來的資料
        name = request.POST["name"]
        email = request.POST["email"]  #w124@gmail.com
        password = request.POST["password"]  
        age = request.POST["age"] 

        #將資料寫進資料庫
        with connection.cursor() as cursor:
            sql = """insert into members(name,email,password,age)
                     values(%s,%s,%s,%s)"""
            #tuple
            cursor.execute(sql,(name,email,password,age))
            
        #轉到會員的首頁上
        return redirect("/register/")
   
        
    return render(request,'homepage/register.htm',locals())

def delete(request, id):
    with connection.cursor() as cursor:
        sql="""delete from members where id=%s"""
        cursor.execute(sql,(id,)) 
    return redirect('/checkin/')


def update(request,id):
    if request.method=='POST':
        name = request.POST["name"]
        email = request.POST["email"]  #w124@gmail.com
        password = request.POST["password"]  
        age = request.POST["age"]

    with connection.cursor() as cursor:
        sql = """update members set name=%s,email=%s,password=%s,age=%s
                     where id=%s""" 
        cursor.execute(sql,(name,email,password,age,id))
    return redirect("/checkin/")

    with connection.cursor()as cursor:
        sql = """select * from member where id =%s"""
        cursor.execute(sql,(id,))
        select=cursor.fetchone()
    return render(request,'homepage/update.htm',locals())
        