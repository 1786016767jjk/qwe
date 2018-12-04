


from django.urls import path,re_path,include

from user_operation.views import UserFavView,UserAddressView
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()
router.register('user_fav',UserFavView)
router.register("user_address",UserAddressView,basename='useraddress')



urlpatterns = [
    path('', include(router.urls)),
]
