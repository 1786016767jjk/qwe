from trade.views import ShoppingCartView,OrderInfoView
from django.urls import path,re_path,include
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()

router.register("shopping_cart",ShoppingCartView,basename="shoppingcart")
router.register('order_info_view',OrderInfoView,basename="order_info_view")


urlpatterns = [
    path('', include(router.urls)),
]
