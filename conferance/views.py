import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from .models import ConfeRoom, Order, Members
from django.contrib import messages
from .forms import Add_form


#顯示可用的會議室
def list(request):
    room = ConfeRoom.objects.all()
    content = {
        'room': room
    }
    return render(request, 'list.html', content)

#某個會議室的deatail
def appointment(request, id):
    room = get_object_or_404(ConfeRoom, id=id)
    d = datetime.date.today()
    order = Order.objects.filter(room=room, time__gte=d).order_by('time')
    content = {
        'order': order,
        'room': room
    }
    return render(request, 'order.html', content)


def add(request, id):
    if 'name' not in request.COOKIES:
        theUrl = request.path
        strJS = "<script>alert('預約前，請先登入');location.href='/member/login/?url=" + theUrl + "'</script>"
        return HttpResponse(strJS)
    rooms = ConfeRoom.objects.all()
    if request.method == "POST":
        roomid = request.POST['roomid']
        date = request.POST['date']
        name = request.COOKIES['name']
        date1 = datetime.datetime.strptime(date, "%Y-%m-%d").date()                   
        order_list = Order.objects.filter(room=roomid)
        time_list = []        
        for order in order_list:
            time_list.append(order.time)
        print(time_list)
        print(date1)
        print(date)
        print(type(date1))
        if date1 not in time_list:
            if date_is_valid(date1):
                Order.objects.create(room=ConfeRoom.objects.get(id=roomid),time=date,user=Members.objects.get(name=name))                    
                return redirect('/conferance')
            else:
                return HttpResponse("<script>alert('超出預約範圍。');location.href='/conferance'</script>")
                # return redirect('/%s' %id)
        else:
            return HttpResponse("<script>alert('已被預約');location.href='/conferance'</script>")
            # return redirect('/conferance/%s' %id)
    return render(request, 'add.html', locals())

def delete(request, room_id, order_id):
    if 'name' not in request.COOKIES:
        # return redirect("/member/login")
        theUrl = request.path
        strJS = "<script>alert('修改前，請先登入');location.href='/member/login/?url=" + theUrl + "'</script>"
        return HttpResponse(strJS)
    
    order = Order.objects.get(id=order_id)
    ordername = order.user
    name = request.COOKIES['name']
    name1 = Members.objects.get(name=name)
    # return HttpResponse(name == name1)
    if ordername == name1:
        order.delete()
        return redirect('/conferance')
    else:
        return HttpResponse("<script>alert('您非預約人，無法刪除預約。');location.href='/conferance/'</script>")

#設置預約範圍，判斷是否重複
def date_is_valid(date1):
    d1 = datetime.date.today()
    d2 = d1 + datetime.timedelta(days=15)
    # print(type(d1))
    # print(type(d2))
    # print(d1)
    if date1 >= d1 and date1 < d2:
        return True
    else:
        return False

def update(request, room_id, order_id):
    if 'name' not in request.COOKIES:
        # return redirect("/member/login")
        theUrl = request.path
        strJS = "<script>alert('修改前，請先登入');location.href='/member/login/?url=" + theUrl + "'</script>"
        return HttpResponse(strJS)
    rooms = ConfeRoom.objects.all()
    order = Order.objects.get(id=order_id)
    ordername = order.user
    name = request.COOKIES['name']
    name1 = Members.objects.get(name=name)
    
    if ordername == name1:
        if request.method == "POST":
            order.room_id = request.POST['roomid']
            order.time = request.POST['date']
            order.save()
            return redirect('/conferance')
    else:
        return HttpResponse("<script>alert('您非預約人，無法修改預約。');location.href='/conferance/'</script>")
    return render(request,'update.html',locals())    

