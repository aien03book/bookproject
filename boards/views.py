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
        createby = request.COOKIES['name']
        Post.objects.create(board=Board.objects.get(boardid=boardid),message=message,createdby=Members.objects.get(name=createby))
        return redirect('/boards')
    
    return render(request,'boards/post.html',locals())

def remove(request,id):
    if 'name' not in request.COOKIES:
        # return redirect("/member/login")
        theUrl = request.path
        strJS = "<script>alert('刪除留言前，請先登入');location.href='/member/login/?url=" + theUrl + "'</script>"
        return HttpResponse(strJS)

    post = Post.objects.get(postid=id)
    postname = post.createdby
    name = request.COOKIES['name']
    name1 = Members.objects.get(name=name)
    # return HttpResponse(name == name1)
    if postname == name1:
        post.delete()
        return redirect('/boards')
    else:
        return HttpResponse("<script>alert('您非反應者，無法刪除此留言。');location.href='/boards'</script>")

def update(request,id):
    if 'name' not in request.COOKIES:
        # return redirect("/member/login")
        theUrl = request.path
        strJS = "<script>alert('更新內容前，請先登入');location.href='/member/login/?url=" + theUrl + "'</script>"
        return HttpResponse(strJS)
    
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
    else:
        return HttpResponse("<script>alert('您非反應者，無法更新此留言。');location.href='/boards'</script>")
    
    return render(request,'boards/update.html',locals())
    