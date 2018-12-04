from rest_framework import serializers
from .models import  UserFav,UserAddress
from apps.goods.serializer import GoodsSerializer
from rest_framework.validators import UniqueTogetherValidator
# from .models import UserAddress


# 列表 (token)  # 必须是登陆的
# 增加 (token, goods_id) # 必须是登陆的
# 取消收藏 (token, goods_id) # 取消收藏
# 是不是收藏的 (token,goods_id) # 是否要收藏

class UserFaverializers (serializers.ModelSerializer):
    '''给增加,删除,修改...'''
    # HiddenField 隐藏不前台看,
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault() # 当前用户
    )  # 需要拿到用户的信息, 但是这个信息不能给前台
    class Meta:
        model = UserFav
        validators = [ # 校验
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                # 如果已经收藏过了, 回返回给前端
                message="已经收藏"
            )
        ]
        fields = '__all__'

class UserFavDetailSerializers (serializers.ModelSerializer):
    '''给收藏列表'''
    goods = GoodsSerializer()
    class Meta:
        model = UserFav
        fields = ('id','goods')


class UserAddresserializers(serializers.ModelSerializer):
    # 不需要提交
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()  # 当前用户
    )
    class Meta:
        model = UserAddress
        fields = "__all__"


