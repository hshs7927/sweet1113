from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from manager.models import Store, Today_lineup, User, Store_set, Allitem
from store.models import Order, Orderlist, Customer, Review
import pdb
# Create your views here.
#여기 인덱스에다가 가게 정보 불러오기도 넣어야해! 
def index(request, biz_url):
    sample = Store.objects.all()
    result = Store.objects.filter(biz_url=biz_url)
    print("result :", len(result))

    if len(result) == 0:
        return render(request, "store/index.html")
    else:
        context = {
            "sample": result,
        }

        return render(request, "store/index.html", context)

def new(request, biz_url):
    sample = Store.objects.all()
    result = Store.objects.filter(biz_url=biz_url)
    #biz_url 이 sugangcaron 이라면 
    #24번째 줄에서 <QuerySet [<Store: 가게명:수강카롱 인스타아이디:sugangcaron URL:/sugangcaron>]>  
    #이렇게 뽑힌다
    store = Store.objects.get(biz_url=biz_url).id
    set_day = Today_lineup.objects.get(date=date)
    # month
    # day
    # month dyay => strftime => fianldate
    # if request.method == "POST":
    #     date = request.get("date")
    #     strftime

    testitem = Today_lineup.objects.filter(store = store, date=date)
    testquota = Today_lineup.objects.filter(store = store, date=date)
    testprice = Today_lineup.objects.filter(store = store, date=date)
     
    context = { 
         "store": store,
         "set_day": set_day,
         "testitem":testitem,
         "testquota":testquota,
         "testprice":testprice,
    }

    return render(request, 'store/new.html', context)

def create(request):
    #set_day = request.POST['set_day'] 셋데이 여기서 빼고, 밑에 order=Order(set_day 여기서도 뺐다)
    today_lineup = request.POST['today_lineup']
    # pdb.set_trace() 이거 보내는 이름은 내마음이다. 
    order_quota = request.POST['order_quota']
    ordered_date = request.POST['orderd_date']
    pickuptime = request.POST['pickuptime']
    order = Order(pickuptime=pickuptime, ordered_date=timezone.now())
    orderlist = Orderlist(today_lineup=today_lineup, order_quota=order_quota)
    order.save()
    orderlist.save()
    # context = {
    #     'test_varible' = today_lineup
    # } 이건 테스트용으로! 
#누구누구님안녕하세요 기능넣고, first_name order db로 넘기기 
    return redirect('store:order_detail', order_id=order.id)    

def home(request):
    return render(request, 'store/home.html')

def delete(request, order_id):
    order = Order.objects.get(id=order_id)
    post.delete()
    return redirect('store:home')
#order.id 뺌, detail history에서, 그리고 히스토리에서, context 도 뺌
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    orderlist = Orderlist.objects.get(order=order_id)
    #order_store= Order.objects.get(order=order) #fk를 써야할것같은데,, 실패,,
    #today_lineup = 도 불러오고(orderlist=orderlist)
    #quota / price 다 불러오고 
    #orderdate도 불러오고 
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
#리뷰=리뷰 눌렀을 때 액션 // review create = 리뷰 submit 했을 때 액션
def review(request, order_id):
    return render(request, 'store/review.html')

def review_index(request):
    reviews = Review.objects.all()
    context = {'reviews': review}

    return render(request, 'review_index.html', context)

def review_edit(request, review_id):
    review = Review.objects.get(id=Review_id)
    context = {'review': review}

    return render(request, 'review_edit.html', context)

def review_update(request, review_id):
    review = Review.objects.get(id=review_id)
    review.order = request.POST['order']
    review.review_content = request.POST['review_content']
    review.save()
    return redirect('store:review_index')

def review_delete(request, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return redirect('store:review_index')
def review_create(request, order_id):
    #order = get_object_or_404(Order, pk=order_id)
    
    order = Order.objects.get(id=order_id)
    review_content = request.POST['review_content']
    #review_content = Review.objects.create(review_content=review_content)
    # if order_id == None:
    #     return Httpresponse("주문번호를 입력해주세요")
    # elif review_content == None:
    #     return Httpresponse("리뷰 내용을 입력해주세요")
    review_content.save()
    return redirect('store:review_index')
# Create your views here.

def myprofile(request):
    return render(request, 'store/myprofile.html')