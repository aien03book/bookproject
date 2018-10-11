from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from  member.models  import Members
from .modelsmember import Member
import datetime
from django.core import serializers
#建立物件
member = Member()

# Create your views here.
def index(request):  
    title = "會員專區"
    # with connection.cursor() as cursor:
    #     sql = """select * from members"""
    #     cursor.execute(sql)
    #     members = cursor.fetchall()
    # return render(request,'member/index.htm',locals())
    
    
    #呼叫方法
    members = member.all()
    return render(request,'member/index.htm',locals())

def login(request):  
    title = "會員登入"
    if request.method =="POST":
        email = request.POST["email"]    
        password = request.POST["password"] 
        captcha = request.POST["captcha"]
        print(request.session)
        if captcha == request.session['captcha']:
            theMember=Members.objects.filter(email=email,password=password).values('name')
            theid=Members.objects.filter(email=email,password=password).values('memberid')
            id1=Members.objects.filter(email=email,password=password).values('id')
            if theMember:
                if 'url' in request.GET:
                    theUrl=request.GET["url"]
                else:
                    theUrl=["/"]
                name=theMember[0]['name']
                memberId=theid[0]['memberid']
                # id1=id1[0]['id']
                response= HttpResponse("<script>alert('登入成功');location.href='" + theUrl+ "'</script>")
                remember = None
                if 'remember' in request.POST.keys():
                    remember = request.POST["remember"]
                    expiresdate= datetime.datetime.now() + datetime.timedelta(days=7)
                    response.set_cookie('name',name,expires=expiresdate)
                else:    
                    response.set_cookie('name',name)
                    response.set_cookie('memberId',memberId)
                    # response.set_cookie('id1',id1)
                return response
            else:
                return HttpResponse("<script>alert('登入失敗');location.href='/member/login'</script>")
        else:
            return HttpResponse("<script>alert('驗證碼錯誤,請重新輸入');location.href='/member/login'</script>")  
    return render(request,'member/login.htm',locals())
    
def register(request):  
    title = "會員註冊"
    if request.method == "POST":
        #接收表單傳過來的資料
        name = request.POST["name"]
        email = request.POST["email"]  #w124@gmail.com
        password = request.POST["password"]  
        age = request.POST["age"]
        checkpassword = request.POST["Cpassword"]
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
    with connection.cursor() as cursor:
        sql = """delete from members where id=%s"""
        #tuple
        cursor.execute(sql,(id,))
    # member.delete(id)
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


def hello(request):
    return HttpResponse("<h1>helloAjax</h1>")

def show(request):
    data=serializers.serialize("json",Members.objects.all())
    return HttpResponse(data)

def ajax(request):
    return render(request,'member/ajax.htm')
def captcha(request):    
    from django.contrib.staticfiles import finders
    import random
    # 安裝 pillow  pip install pillow
    from PIL import Image,ImageDraw,ImageFont   
    list1 = random.sample(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],5)
    txt = ''.join(list1)    
    
    # todo 將產生的數字及字母存到session中
    request.session['captcha'] = txt  
    
    width = 15 * 4
    height = 30
    image = Image.new('RGB', (width, height), (255, 255, 255))    
    # 下載字體https://fonts.google.com/
    thefont = finders.find('fonts/Kavivanar-Regular.ttf')
    font = ImageFont.truetype(thefont, 16)   
    draw = ImageDraw.Draw(image)
    draw.text((5, 5), txt,font=font, fill=(255, 0, 0))
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response

def logout(request):
    back = HttpResponse("<script>location.href='/'</script>")
    back.delete_cookie('name')
    return back

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