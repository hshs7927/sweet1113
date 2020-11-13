from django.db import models
from django.contrib.auth.models import User
from manager.models import Store, Today_lineup

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cus_insta = models.CharField(max_length=15, unique=True)
    

    def __str__(self):
        return f'userPK고객이름:{self.user.first_name} 인스타아이디:{self.cus_insta}'

class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ##주문한시간
    set_day = models.DateField()
    order_date = models.DateTimeField(auto_now_add=True)
    pickuptime = models.TimeField(null=True)
    picktf = models.BooleanField(null=True)
    reservetf = models.BooleanField(null=True)
    def __str__(self):
        return f'store:{self.store.biz_name} first_name:{self.user.first_name} set_day:{self.today_lineup.set_day}pickuptime:{self.pickuptime} picktf:{self.picktf} reservetf:{self.reservetf}'
    

class Orderlist(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    today_lineup = models.ForeignKey(Today_lineup, on_delete=models.CASCADE, null=True)
    order_quota = models.IntegerField()

def __str__(self):
        return f'order_number:{self.order.id} / Today_lineup:{self.today_lineup.id} / order_quota:{self.order_quota}'