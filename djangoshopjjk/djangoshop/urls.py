"""djangoShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin

from django.urls import path,re_path,include

# 文件下发的接口
from django.views.static import serve
from djangoshop.settings import MEDIA_ROOT

from rest_framework.authtoken import views

from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsView,CategaryView

# goods_list = GoodsView.as_view({ # 一个资源对应的一个接口
#     'get': 'list',
# })


from rest_framework.routers import DefaultRouter
from goods.views import GoodsView
from goods.views import  BannerView
from user_operation.views import UserFavView,UserAddressView
from trade.views import ShoppingCartView,OrderInfoView

router = DefaultRouter() # 创建一个路由

# 地址

# 购物车


# 订单
router.register('order_info_view',OrderInfoView,basename="order_info_view")
import xadmin

# from trade.views import  AlipayView
from django.shortcuts import render
def returnIndex(request):
    return render(request,'index.html')

urlpatterns = [
# 项目的首页
   path('', include('social_django.urls', namespace='social')),
    re_path('^index/$',returnIndex),
   # path('alipay/return/',AlipayView.as_view()),
    path('xadmin/', xadmin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    path('goods/',include("goods.urls")),
    path('user_options/', include("user_operation.urls")),
    path('trade/',include("trade.urls")),
    # 富文本中有图片需要上传
    path('ueditor/',include('DjangoUeditor.urls' )),
    # 静态资源的下发
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # token
    path(r'api-token-auth/', views.obtain_auth_token),
    path('jwt-auth/', obtain_jwt_token)
]






















