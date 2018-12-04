from django.contrib import admin

# Register your models here.

from .models import UserFav,UserAddress
import xadmin

class UserFavAdmin(object):
    list_display = ['goods','user','id']

class UserAddressAdmin(object):
    pass

xadmin.site.register(UserFav,UserFavAdmin)
xadmin.site.register(UserAddress,UserAddressAdmin)

