from django.shortcuts import render
from django.views import View # django View
# django rest_framework中的view
from rest_framework.views import APIView # 继承 django View
from rest_framework.response import Response

from goods.models import Goods
from rest_framework.views import  APIView
from rest_framework.generics import  GenericAPIView
from rest_framework.mixins import ListModelMixin
from goods.serializer import GoodsSerializer
from django.http import JsonResponse
# Create your views here.

# 生成个列表, 返回给前端
# 基于函数(function  base  view)  (fbc)
# 基于类 (class base view) (cbv)

# 我们django中视图
# class GoodsView(View):
#     def get(self,request):
#         gs = Goods.objects.all()
#         lst = GoodsSerializer(gs,many=True)
#         return JsonResponse(lst.data,safe=False)


# APiView
# class GoodsView(APIView):
#     """
#     list all Goods  # 生成在接口文档中
#     """
#     def get(self, request):
#         gs = Goods.objects.all()
#         lst = GoodsSerializer(gs,many=True)
#         return Response(lst.data)


# from rest_framework import mixins
# from rest_framework import generics
# class GoodsView(mixins.ListModelMixin,
#                   generics.GenericAPIView):
#     queryset = Goods.objects.all()  # 给父类使用
#     serializer_class = GoodsSerializer # 给父类使用
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#             # self.get_queryset()
#             # get_queryset
#
#     def get_queryset(self): # 过滤
#         key = self.request.query_params['name'] # 查询的参数
#         return Goods.objects.filter(name__contains=key)



#ListCreateAPIView
from rest_framework import generics
import django_filters
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="market_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="market_price", lookup_expr='lte')
    name = filters.CharFilter(field_name='name',lookup_expr='contains')
    class Meta:
        model = Goods
        fields = ['min_price', 'max_price','name']

class GoodsView(generics.ListCreateAPIView):
    queryset = Goods.objects.all()  # 给父类使用
    serializer_class = GoodsSerializer # 给父类使用
    # 局部注册过滤的控件
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    # 填写需要过滤的字段和条件  # 只支持相等  (contain  10-100)
    #filter_fields = ('market_price')
    # 定义查询规则
    filterset_class = ProductFilter # 定义过滤的类


# get(获取) post(新建) put(更新) delete(删除) patch(更新)
# put(更新) 更新全部
# patch 那个字段提交了, 更新那个字段(很少用)

#
# from rest_framework import viewsets
#
# class GoodsView(viewsets.ReadOnlyModelViewSet):
#     """
#     列出所有的商品
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


# restful的状态码
from rest_framework import status

