# model    1. 数据库的配置

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoshop.settings")

import django
django.setup()

from goods.models import Goods
from goods.models import GoodsCategory
from dbtools.data.product_data import row_data

def addGoods():
    for item in row_data:

        name  = item['name']
        desc = item['desc']
        if not desc : # 把空给排除掉
            desc = ''
        sale_price = float(item['sale_price'].replace('￥','').replace('元',''))  # '￥232元'
        market_price = float(item['market_price'].replace('￥','').replace('元','')) # '￥232元'
        goods_desc = item['goods_desc']
        images = item['images']
        goods_front_image=images[0]
        categorys = item['categorys'] # 分类的路径
        category = GoodsCategory.objects.filter(name=categorys[-1]).first() # 分类

        # item  每一件商品
        Goods.objects.create(name=name,
                             goods_brief = desc,
                             shop_price=sale_price,
                             market_price=market_price,
                             goods_desc=goods_desc,
                             category=category,
                             goods_front_image=goods_front_image)



addGoods()
from goods.models import GoodsImage
def  Banner():
    for   i  in range(1,53):
        item=Goods.objects.filter(id=i).first()
        GoodsImage.objects.create(goods=item,image ='goods/banner/sxsp-3_jG6lwp4_F5duPQM.jpg')


Banner()











