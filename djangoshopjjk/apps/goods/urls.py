from django.urls import path,include
from goods.views import BannerView
from goods.views import GoodsView,CategaryView

# goods_list = GoodsView.as_view({ # 一个资源对应的一个接口
#     'get': 'list',
# })
#

from rest_framework.routers import DefaultRouter
from goods.views import GoodsView
router = DefaultRouter() # 创建一个路由
router.register(r'lst', GoodsView) # viewset
router.register(r"category",CategaryView)
router.register(r'banner',BannerView)
# router.register(r"banner",BannerView)
# router.register(r"hot_searchs",HotSearchsView)

# def createToken(request):
#     from user.models import User
#     from rest_framework.authtoken.models import Token
#
#     for user in User.objects.all():
#         Token.objects.get_or_create(user=user)



urlpatterns = [
    # path('lst/', goods_list, name='goods_list'),
    path('', include(router.urls)),
    # path('token',createToken)
]