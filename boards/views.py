# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from boards.models import Members, Board, Post


#建立物件
# member = Members()

# Create your views here.
def index(request):  
    title = "與我們聯繫"
    members = Members.objects.all()
    return render(request,'boards/site.html',locals())

def post(request):  
    title = "我有話要說"
    boards = Board.objects.all()
    return render(request,'boards/post.html',locals())

# def login(request):  
#     title = "會員登入"
#     # POST
#     if request.method == "POST":
#         #name=value > key=value
#         # print(request.POST.keys())
#         mail = request.POST["email"]
#         pwd = request.POST["password"]

#         theMember = Members.objects.filter(email=mail,password=pwd).values('name')
#         #print()

#         if theMember:
#             if 'url' in request.GET:
#                 theUrl = request.GET['url']
#             else:
#                 theUrl = "/"
#             # print("登入成功：", theMember[0].name)
#             #return HttpResponse("<h2>登入成功</h2>")
#             name = theMember[0]['name']
#             strJS = "<script>alert('登入成功');location.href='" + theUrl + "'</script>"
#             response = HttpResponse(strJS)
           
#             remember = None
#             #記住我有打勾保留cookie7天
#             if 'remember' in request.POST.keys():
#                 #    remember = request.POST["remember"]
#                 expiresdate = datetime.datetime.now() + datetime.timedelta(days=7)
#                 response.set_cookie("name",name,expires=expiresdate)
#             else:
#                 response.set_cookie("name",name)

#             return response
#         else:
#             # print("登入失敗")
#             #return HttpResponse("<h2>登入失敗</h2>")
#             return HttpResponse("<script>alert('登入失敗');location.href='/member/login'</script>")



        
        
#         # print(email, password, remember)


#     # GET   
#     return render(request,'member/login.html',locals())

# def logout(request):
#     response = HttpResponse("<script>location.href='/'</script>")
#     response.delete_cookie('name')
#     return response
# def register(request):  
#     title = "會員註冊"
#     if request.method == "POST":
#         #接收表單傳過來的資料
#         name = request.POST["name"]
#         email = request.POST["email"]  #w124@gmail.com
#         password = request.POST["password"]  
#         age = request.POST["age"] 

#         #將資料寫進資料庫
#         # with connection.cursor() as cursor:
#         #     sql = """insert into members(name,email,password,age)
#         #              values(%s,%s,%s,%s)"""
#         #     #tuple
#         #     cursor.execute(sql,(name,email,password,age))
#         _member = (name,email,password,age)
#         member.create(_member)
#         #轉到會員的首頁上
#         return redirect("/member/")
   
        
#     return render(request,'member/register.html',locals())


# def delete(request, id):
#     # with connection.cursor() as cursor:
#     #     sql = """delete from members where id=%s"""
#     #     #tuple
#     #     cursor.execute(sql,(id,))
#     member.delete(id)
#     return redirect("/member/")

#     # return HttpResponse("<h2>" + str(id) + "</h2>")

# def update(request, id):
#     #步驟二
#     if request.method == "POST":
#         #接收表單傳過來的資料
#         name = request.POST["name"]
#         email = request.POST["email"]  #w124@gmail.com
#         password = request.POST["password"]  
#         age = request.POST["age"] 

#         #將資料寫進資料庫
#         # with connection.cursor() as cursor:
#         #     sql = """update members set name=%s,email=%s,password=%s,age=%s
#         #              where id=%s"""
#         #     #tuple
#         #     cursor.execute(sql,(name,email,password,age,id))
#         _member = (name,email,password,age,id)
#         member.update(_member)
#         #轉到會員的首頁上
#         return redirect("/member/")

#     #步驟一
#     # with connection.cursor() as cursor:
#     #     sql = """select * from members where id=%s"""
#     #     #tuple
#     #     cursor.execute(sql,(id,))
#     #     member = cursor.fetchone()
#     membersingle = member.single(id)
#     return render(request,'member/update.html',locals())