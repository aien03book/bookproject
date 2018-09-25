# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from boards.models import Members, Board, Post


#建立物件
# member = Members()

# Create your views here.
def site(request):
    title = "與我們聯繫"
    posts = Post.objects.all()
    return render(request,'boards/site.html',locals())

def post(request):  
    if 'name' not in request.COOKIES:
        # return redirect("/member/login")
        theUrl = request.path
        strJS = "<script>alert('留言前，請先登入');location.href='/member/login/?url=" + theUrl + "'</script>"
        return HttpResponse(strJS)

    title = "我有話要說"
    boards = Board.objects.all()
    if request.method == "POST":
        boardid = request.POST['boardid']
        message = request.POST['message']
        Post.objects.create(board=Board.objects.get(boardid=boardid),message=message)
        return redirect('/boards')
    boards = Board.objects.all()
    return render(request,'boards/post.html',locals())

def remove(request,id):
    post = Post.objects.get(postid=id)
    post.delete()
    return redirect('/boards/')

def update(request,id):
    title = "換個方式說"
    post = Post.objects.filter(postid=id)
    if request.method == "POST":
        message = request.POST['message']
        post.update(message=message)        
        return redirect('/boards')
    return render(request,'boards/update.html',locals())