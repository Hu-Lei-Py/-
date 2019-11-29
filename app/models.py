from django.db import models


class good_type(models.Model):
    """商品分类"""
    title = models.CharField(max_length=10, verbose_name='商品类目')
    type_pic = models.CharField(max_length=100, verbose_name='图片链接')


class good_info(models.Model):
    """商品详情"""
    title = models.CharField(max_length=150, verbose_name='商品名称')
    image = models.CharField(max_length=100, verbose_name='商品图片路径')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='商品价格')
    good_type = models.ForeignKey('good_type', on_delete=models.CASCADE, verbose_name='关联类别', null=True, blank=True)
    good_num = models.IntegerField(default=20, verbose_name='商品库存')
    is_onsale = models.BooleanField(default=True, verbose_name='是否在销售')


# 用户表

# 地址表
class address(models.Model):
    address = models.CharField(max_length=40, verbose_name='地址')
    user = models.CharField(max_length=50, verbose_name='用户')
    phone = models.IntegerField(max_length=30, verbose_name='电话')


# class Order(models.Model):
#     """订单表"""
#     addr = models.CharField(max_length=100)
#     total_money = models.DecimalField(max_digits=10, decimal_places=2)
#     create_date = models.DecimalField(auto_now=True)
#
#
# class Order_goods(models.Model):
#     gid = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     num = models.SmallIntegerField()
#     fk_order = models.ForeignKey('Order', on_delete=models.CASCADE)
