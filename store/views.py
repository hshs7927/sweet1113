from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from manager.models import Store, Today_lineup
# Create your views here.
def new(request, biz_utl):
    # teststore = Store.objects.get(today_lineup.id)
    # test = Today_lineup.objects.filter(store=teststore)
    # testitem = Today_lineup.objects.filter(store=teststore)
    # testquota = Today_lineup.objets.filter(store=teststore)
    # testprice = Allitem.objects.get(allitem.id == today_lineup.item)
    
    # context={
    #     "teststore":teststore,
    #     "test":test,
    #     "testitem":testitem,
    #     "testquota":testquota,
    #     "testprice":testprice,
    #     }
    return render(request,'store/new.html', context)
#balance에서 갖고 오기 나중에는 
def create(request):
    set_day = request.POST['set_day']
    pickuptime = request.POST['pickuptime']
    today_lineup = request.POST['today_lineup']
    order_quota = request.POST['order_quota']
    ordered_date = request.POST['orderd_date']
    order = Order(set_day=set_day, pickuptime=pickuptime, orderedate=timezone.now())
    orderlist = Orderlist(today_lineup=today_lineup, order_quota=order_quota)
    order.save()
    orderlist.save()
#누구누구님안녕하세요 기능넣고, first_name order db로 넘기기 
    return redirect('store:order_detail', order_id=order.id)    

def index(request):
    return render(request, 'store/index.html')

def delete(request):
    return redirect('store:index')

def order_detail(request, order_id):
    return render(request, 'store/order_detail.html')

def order_history(request, order_id):
    return render(request, 'store/order_history.html', context)
# Create your views here.