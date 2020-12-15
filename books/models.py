from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    address1_code = models.IntegerField()
    address1_prefecture = models.CharField(max_length=10)
    address1_city = models.CharField(max_length=100)
    address2_code = models.IntegerField(null=True)
    address2_prefecture = models.CharField(max_length=10,null=True)
    address2_city = models.CharField(max_length=100,null=True)
    sex = models.CharField(max_length=1,default='0')
    # '0':未入力,'1':男,'2':女,'9':不明
    birthday = models.DateField()
    phone = models.CharField(max_length=11)
    card_num = models.CharField(max_length=16,null=True)
    card_name = models.CharField(max_length=30,null=True)
    card_limit = models.DateField(null=True)

class Item(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    item_img = models.ImageField(null=True)
    publish = models.CharField(max_length=100)
    category_1 = models.CharField(max_length=100)
    category_2 = models.CharField(max_length=100)
    p_date = models.DateField(null=True)
    stock = models.IntegerField(null=True,default=0)
    isbn = models.IntegerField(null=True)
    jan = models.IntegerField(null=True)
    item_ex = models.TextField(null=True)

class Review(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField()
    # 0~5を使用。☆の数
    review_txt = models.TextField()
    review_date = models.DateField()

class Slip(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slip_fee = models.CharField(max_length=1)
    shipping = models.CharField(max_length=1)
    slip_status = models.CharField(max_length=1,default='0')
    # '0':カートの中,'1':購入済み,'2':発送済み
    slip_date = models.DateField()

class Order(models.Model):
    slip_id = models.ForeignKey(Slip, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_cnt = models.IntegerField(default=1)

class Info(models.Model):
    info_name = models.CharField(max_length=20)
    info_mail = models.CharField(max_length=100)
    info_txt = models.TextField()
    info_status = models.CharField(max_length=1,default='0')
    # '0':未処理,'1':処理済
    info_date = models.DateField()

