from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from manager.models import Store, Today_lineup, User, Store_set, Allitem
from store.models import Order, Orderlist, Customer 
# Create your views here.
def new(request):
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
    return render(request,'store/new.html')
    #여기 리턴에서 , context 뺌 
#balance에서 갖고 오기 나중에는 
def create(request):
    #set_day = request.POST['set_day'] 셋데이 여기서 빼고, 밑에 order=Order(set_day 여기서도 뺐다)
    pickuptime = request.POST['pickuptime']
    today_lineup = request.POST['today_lineup']
    order_quota = request.POST['order_quota']
    ordered_date = request.POST['orderd_date']
    order = Order(pickuptime=pickuptime, orderedate=timezone.now())
    orderlist = Orderlist(today_lineup=today_lineup, order_quota=order_quota)
    order.save()
    orderlist.save()
#누구누구님안녕하세요 기능넣고, first_name order db로 넘기기 
    return redirect('store:order_detail', order_id=order.id)    

def index(request):
    return render(request, 'store/index.html')

def delete(request):
    return redirect('store:index')
#order.id 뺌, detail history에서, 그리고 히스토리에서, context 도 뺌
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    orderlist = Orderlist.objects.get(order=order_id)
    #order_store= Order.objects.get() #fk를 써야할것같은데,, 실패,,
    #notification = Store_set.objects.get(store=order_store)
    context = {'order':order}
    context = {'orderlist':orderlist}
    #context = {'notification': notification}
    return render(request, 'store/order_detail.html', context)

def order_history(request):
    # order=Order.objects.filter(User.id=user.get_username)
    # order=Order.objects.get(id=order_id)
    # context = {'post':post} 와 진짜어렵다. 유저네임으로 오더불러오고 내용도 채워야하는거잔항
    return render(request, 'store/order_history.html')
# Create your views here.