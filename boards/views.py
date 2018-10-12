from django.shortcuts import render, redirect
from django.http import HttpResponse
from member.models  import Members
from boards.models import Members, Board, Post
from boards.serializers import MembersSerialize, BoardSerialize, PostSerialize
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
import json
from django.db import connection

#以下未成功
from django.db.models import Count   #嘗試回傳各類反應統計數值
from django.core import serializers  #嘗試透過序列化方式回傳json檔，但無法讀取fk的value


# Create your views here.
def site(request):
    title = "與我們聯繫"
    return render(request,'boards/site.html',locals())

def post(request):  
    if 'name' not in request.COOKIES:
        theUrl = request.path
        strJS = "<script>alert('留言前，請先登入');location.href='/member/login/?url=" + theUrl + "'</script>"
        return HttpResponse(strJS)

    title = "我有話要說"
    boards = Board.objects.all()
    if request.method == "POST":
        boardid = request.POST['boardid']
        message = request.POST['message']
        createby = request.COOKIES['name']
        Post.objects.create(board=Board.objects.get(boardid=boardid),message=message,createdby=Members.objects.get(name=createby))
        return redirect('/boards')
    
    return render(request,'boards/post.html',locals())

def checkid(request,id):
    post = Post.objects.get(postid=id)
    postname = post.createdby
    name = request.COOKIES['name']
    name1 = Members.objects.get(name=name)
    return HttpResponse(postname == name1)

def update(request,id):
    title = "換個方式說"
    post = Post.objects.get(postid=id)
    postname = post.createdby
    name = request.COOKIES['name']
    name1 = Members.objects.get(name=name)
    
    if postname == name1:
        if request.method == "POST":
            post.message = request.POST['message']
            post.save()
            return redirect('/boards')
    
    return render(request,'boards/update.html',locals())

def chart(request):
    title = "統計報表"
    return render(request,'boards/chart.html',locals())

def count(request):
    with connection.cursor() as cursor:
        sql = """select COUNT(*) from posts"""
        cursor.execute(sql)
        total = cursor.fetchall()
        a=[]
        for i in total:
            datas={
                "total" : i[0],
            }
            a.append(datas)
        total = json.dumps(a)
        
    with connection.cursor() as cursor:
        sql = """SELECT b.name, COUNT(*) number 
                FROM posts p Left Join boards b
                ON p.boardid = b.boardid
                GROUP BY name
                ORDER BY number desc"""
        cursor.execute(sql)
        Categories = cursor.fetchall()
        b=[]
        for i in Categories:
            datas={
                "name" : i[0],
                "y": i[1]/a[0]['total']
            }
            b.append(datas)
        results = json.dumps(b)

    return HttpResponse(results,content_type='application/json')


#以下透過restframework進行restful api製作

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerialize

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerialize

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerialize
    filter_backends = (filters.SearchFilter,)    #使用restframework下的篩選
    search_fields = ('message',)                   #針對特定欄位進行篩選

#以下代碼序列化後無法讀出fk value

# def searchall(request):
#     posts_serialize = serializers.serialize('json',Post.objects.all())
#     return HttpResponse(posts_serialize,content_type="application/json")

# def searchone(request,searchone):
#     results = serializers.serialize('json',Post.objects.filter(message__contains=searchone))
#     return HttpResponse(results,content_type="application/json")