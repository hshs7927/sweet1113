from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    biz_name = models.CharField(max_length=10, null=True)
    biz_num = models.IntegerField(null=True)
    biz_url = models.CharField(max_length=15, unique=True, null=True)
    biz_insta = models.CharField(max_length=15, null=True)
    biz_address = models.CharField(max_length=40, null=True)
    biz_tel = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f'가게명:{self.biz_name} 인스타아이디:{self.biz_insta} URL:/{self.biz_url}'


class Allitem(models.Model):
    store = models.ForeignKey('Store', on_delete=models.CASCADE, null=True)
    item_category = models.CharField(max_length=10)
    item_name = models.CharField(max_length=10)
    item_price = models.IntegerField(null=True)

    def __str__(self):
        return f'가게명:{self.store.biz_name} 카테고리:{self.item_category} 품목명:{self.item_name} 가격:{self.item_price}'

class Today_lineup(models.Model):
    store = models.ForeignKey('Store', on_delete=models.CASCADE, null=True)
    item = models.ForeignKey('Allitem', on_delete=models.PROTECT, null=True)
    set_day = models.DateField()
    quota = models.IntegerField()
            
    def __str__(self):
        return f'품목:{self.item.item_name} / 판매날짜:{self.set_day} / 재고:{self.quota}'


class Store_set(models.Model):
    store = models.ForeignKey('Store', on_delete=models.CASCADE, null=True)
    openday = models.DateField()
    opentime = models.TimeField()
    pickuptime = models.TimeField(null=True)
    notification = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'가게명:{self.store.biz_name} 오픈날짜:{self.openday}'

class Balance(models.Model):
    today_lineup = models.ForeignKey('today_lineup', on_delete=models.CASCADE, null=True)
     
#리뷰모델은 customer app에서 만들 것