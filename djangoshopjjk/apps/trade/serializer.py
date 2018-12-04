# 序列化

from rest_framework import serializers
from goods.serializer import GoodsSerializer
from .models import ShoppingCart,OrderGoods,OrderInfo
from goods.models import Goods


# 获取购物车所有数据

# 根据购物车id 获取商品的数据

# 更新购物车 (更新数量)
    # 库存的变化

# 根据购物车id 删除商品
    # 商品的库存需要添加

# 添加购物车
    # 查看购物车有没有这个商品, 如果有这个商品, 数量添加, 否则添加一条数据
    # 商品的库存需要减少

class ShoppingCartSerializers(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()  # 当前用户
    )
    nums = serializers.IntegerField(required=True,min_value=1,
                                    error_messages={
                                        'required':'nums是必须写',
                                        'min_value':'最小为1'
                                    })
    goods = serializers.PrimaryKeyRelatedField(many=False,queryset=Goods.objects.all())
    class Meta:
        model = ShoppingCart
        fields = '__all__'

    # def create(self, validated_data):
    #     # 创建的时候
    #
    # def update(self, instance, validated_data):
    #     # 更新和删除

# 购物车
class ShoppingCartDetailSerializers(serializers.ModelSerializer):
    goods = GoodsSerializer()
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class OrderInfoSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # 订单号唯一
    order_sn = serializers.CharField(read_only=True)
    # 微信支付会用到
    nonce_str = serializers.CharField(read_only=True)
    # 支付宝交易号
    trade_no = serializers.CharField(read_only=True)
    # 支付状态
    pay_status = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    # 支付的url
    alipay_url = serializers.SerializerMethodField(read_only=True)

    # get_字段名
    def get_alipay_url(self, obj):
        from trade.util.aliPay import AliPay
        alipay = AliPay(
            # 沙箱里面的appid值
            appid="2016092000553317",
            # notify_url是异步的url
            app_notify_url="http://47.94.241.247:8000/alipay/return/",
            # 我们自己商户的密钥的路径
            app_private_key_path="apps/trade/keys/siyao.txt",
            # 支付宝的公钥
            alipay_public_key_path="apps/trade/keys/zhifugongyao.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            # debug为true时使用沙箱的url。如果不是用正式环境的url
            debug=True,  # 默认False,
            return_url="http://47.94.241.247:8000/alipay/return/"
        )

        url = alipay.direct_pay(
            # 订单标题
            subject=obj.order_sn,
            # 我们商户自行生成的订单号
            out_trade_no=obj.order_sn,
            # 订单金额
            total_amount=obj.order_mount,
            # 成功付款后跳转到的页面，return_url同步的url
            return_url="http://47.94.241.247:8000/alipay/return/"
        )
        # 将生成的请求字符串拿到我们的url中进行拼接
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        return re_url

    class Meta:
        model = OrderInfo
        fields = '__all__'

    def generate_order_sn(self):
        # 生成订单号
        # 当前时间+userid+随机数
        from random import Random
        import time
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id,
                                                       ranstr=random_ins.randint(10, 99))
        return order_sn

    # 订单号  订单时间用户id随机数
    def create(self, validated_data):
        validated_data['order_sn'] = self.generate_order_sn() # 必须是唯一
        return OrderInfo.objects.create(**validated_data)


class OrderGoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderGoods
        fields = '__all__'


