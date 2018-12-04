from rest_framework import serializers
from goods.models  import Goods,Banner
from goods.models import GoodsCategory,GoodsImage


class CategarySerializer3(serializers.ModelSerializer): # 三级分类
    class Meta:
        model= GoodsCategory
        fields = '__all__'

class CategarySerializer2(serializers.ModelSerializer): # 二级分类
    sub_cat = CategarySerializer3(many=True)
    class Meta:
        model= GoodsCategory
        fields = '__all__'

class CategarySerializer(serializers.ModelSerializer): # 一级分类
    sub_cat = CategarySerializer2(many=True)
    class Meta:
        model= GoodsCategory
        fields = '__all__'


# class GoodsSerializer(serializers.Serializer):
#     # 只能读不能修改
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True, allow_blank=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_num = serializers.IntegerField(default=0)
#     goods_brief = serializers.CharField(max_length=500)
#     category = CategarySerializer() # 使用上面的那个进行序列化
#
#     # validated_data 表单中获取的数据
#     def create(self, validated_data):
#         """
#         当调用post请求, 创建新的时候执行这个
#         """
#         return Goods.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         更新的时候使用
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        #fields = ""  #序列化
        fields = ('image',)


class GoodsSerializer(serializers.ModelSerializer):
    category = CategarySerializer()  # 重写序列化
    images = GoodsImageSerializer(many=True)  # 商品轮播图
    class Meta:
        model = Goods
        fields = "__all__"  #序列化
        #fields = ('name','id')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

# class HotWordsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HotSearchWords
#         fields = '__all__'

