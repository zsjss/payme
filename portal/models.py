from django.db import models
from django.contrib import admin


################################
class User(models.Model):
    username = models.CharField(max_length=255, db_index=True, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, db_index=True)
    real_name = models.CharField(max_length=255)
    real_id = models.CharField(max_length=40)
    email = models.EmailField()
    signup_at = models.DateTimeField(auto_now=True)
    avater = models.CharField(max_length=255)
    location_province = models.CharField(max_length=255)
    location_city = models.CharField(max_length=255)

    def __unicode__(self):
        return self.username


class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


##################################
class House(models.Model):
    owner = models.ForeignKey(User)
    house_name = models.CharField(max_length=255)
    house_size = models.IntegerField()
    house_style = models.CharField(max_length=30)

    def __unicode__(self):
        return self.house_name


class HouseAdmin(admin.ModelAdmin):
    list_display = ['owner', 'house_name']


##################################
class Order(models.Model):
    house = models.ForeignKey(House)
    renter = models.ForeignKey(User)

    def __unicode__(self):
        return self.id


class OrderAdmin(admin.ModelAdmin):
    list_display = ['house', 'renter']


###################################
class Payment(models.Model):
    to_who = models.ForeignKey(User, related_name='payment_to_me_set')
    from_who = models.ForeignKey(User, related_name='payment_from_me_set')
    money = models.IntegerField()

    def __unicode__(self):
        return self.id


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['money', 'to_who', 'from_who']
