# django 批量导入数据

# model    1. 数据库的配置
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoshop.settings")# project_name 项目名称

# 在django 低版本中没必要写(1.6以下)
import django
django.setup()

from dbtools.data.category_data import row_data # 数据
from goods.models import  GoodsCategory

def addCategary():
    # 加载数据文件  row_data
    # 通过model写入  GoodsCategory 写入
    for item in row_data :
        # item 一级分类
        g = GoodsCategory.objects.create(name=item['name'],code=item['code'],category_type=1)
        for item2 in item['sub_categorys'] :
            # item2 二级分类
            g1 = GoodsCategory.objects.create(name=item2['name'], code=item2['code'], category_type=2,parent_category=g)
            for item3 in item2['sub_categorys'] :
                # item3是三级分类
                GoodsCategory.objects.create(name=item3['name'], code=item3['code'], category_type=3,
                                                  parent_category=g1)


# 调用函数
addCategary()






