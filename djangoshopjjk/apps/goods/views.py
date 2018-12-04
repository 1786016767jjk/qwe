from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
import django_filters
from django_filters import rest_framework as filters
from .models import Goods,GoodsCategory
from .serializer import GoodsSerializer,CategarySerializer,\
    BannerSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters as resfilters
from .models import  Banner
from rest_framework.permissions import IsAuthenticated


class ProductFilter(filters.FilterSet):
    # 价格区间   # name模糊查找   # 支持分类查找
    pricemin = filters.NumberFilter(field_name="market_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name="market_price", lookup_expr='lte')
    name = filters.CharFilter(field_name='name',lookup_expr='contains')
    top_category = filters.NumberFilter(field_name='category',method='filterGoodsByCategary')

    # 不管是第几分类的都可以查找到
    def filterGoodsByCategary(self,queryset, name, value):
        print(value)
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax','name','top_category']

class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 12
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100

class GoodsView(viewsets.ReadOnlyModelViewSet):
    '''
      list Goods View
    '''
    queryset = Goods.objects.all()
    pagination_class = GoodsPagination # 定义局部的分页
    serializer_class = GoodsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,resfilters.SearchFilter,resfilters.OrderingFilter)
    filterset_class = ProductFilter
    # permission_classes = (IsAuthenticated,)
    ordering_fields = ('sold_num', 'shop_price') # 进行排序
    search_fields = ('name', 'goods_brief', 'goods_desc') # 进行搜索

# 分类列表给到前端
class CategaryView(viewsets.ReadOnlyModelViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1).all() # 只查询一级分类
    serializer_class = CategarySerializer


# banner图
class BannerView(viewsets.GenericViewSet,mixins.ListModelMixin):
    """goods_goodsimage
    首页商品分类数据
    """
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer

# 热搜
# class HotSearchsView(viewsets.GenericViewSet,mixins.ListModelMixin):
#     """
#     热搜
#     """
#     queryset = HotSearchWords.objects.all().order_by("-index")
#     serializer_class = HotWordsSerializer

#class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    #"""
    #首页商品分类数据
    #"""
    # 获取is_tab=True（导航栏）里面的分类下的商品数据
    #queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    #serializer_class = IndexCategorySerializer