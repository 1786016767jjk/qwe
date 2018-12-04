from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import  UserFav,UserAddress
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializer import  UserFaverializers,UserFavDetailSerializers,UserAddresserializers


# Create your views here.

# 列表 (token)  # 必须是登陆的
# 增加 (token, goods_id) # 必须是登陆的 (增加)
# 取消收藏 (token, goods_id) # 取消收藏 (删除)
# 是不是收藏的 (token,goods_id) # 是否要收藏 (查询)
#



class UserFavView(viewsets.ModelViewSet): # 删除
    queryset = UserFav.objects.all() # 其实是没用的

    # 使用多个序列化的类
    def get_serializer_class(self):
        if self.action == 'list': # 查找全部
            return  UserFavDetailSerializers
        return UserFaverializers


    def get_queryset(self):
        # self.request.user 当前用户
        return UserFav.objects.filter(user=self.request.user)

    # 权限
    permission_classes = (IsAuthenticated,)#必须是自己
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication]

    # 这个商品有没有被收藏 (传入goods_id + token)
    lookup_field = 'goods_id' # 根据goods_id进行查找了



# 增加
# 删除
# 查询列表
# 查一个
# 修改

class UserAddressView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  # 必须是自己
    authentication_classes = [BasicAuthentication, SessionAuthentication, JSONWebTokenAuthentication]
    serializer_class = UserAddresserializers
    def get_queryset(self):
        # 跟用户相关的地址
        return UserAddress.objects.filter(user=self.request.user)