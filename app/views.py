from django.shortcuts import render, HttpResponse
from app import models
from django.views.generic import View
from jia import one
from django.core.paginator import Paginator
from lianx import settings
from lianx.views import get_redis_conn
import json


# def show_tyoe(request, typeid):
#     res = models.good_type.objects.get(id=typeid)
#     # page = Paginator(res, 5)
#     #     # yeshu = page.num_pages
#     #     # yema = page.page_range
#     line = res.good_info_set.all()
#     dict_line = {"line": line}
#     return render(request, "snfresh/goods_list.html", dict_line)


def xiang(request, id):
    list = models.good_info.objects.get(id=id)
    dict_lone = {"list": list}
    return render(request, "snfresh/good_xiang.html", dict_lone)


def branch(request):
    res = request.GET.get("id")  # [33,6]
    print(res)
    return HttpResponse("hehe")


def cccc(request):
    return render(request, "snfresh/one.html")


# 读取json中的数据
def Payment_method():
    import os
    lu = settings.BASE_DIR
    jing = os.path.join(lu, "templates")
    lu = os.path.join(jing, "snfresh")
    lu2 = os.path.join(lu, "method.json")
    with open(lu2, "r", encoding="utf8") as f:
        jue = f.read()
        lei = json.loads(jue)
        # print(lei,"*"*10)
        return lei


def order(request):
    gid = request.GET.get('gid')
    r = gid.split(',')
    # print(r, "*" * 10)
    good_list = []
    for i in r:
        goods_line = models.good_info.objects.get(id=i)
        # print(goods_line)
        # redis查询购物车数量
        res = get_redis_conn()
        zhi = res.hget("car_777", i)  # 数量  类型列表
        # print(type(zhi), "zhi" * 10)
        # print(zhi, "zhi" * 10)
        # print(int(zhi), "zhi" * 10)
        jia = goods_line.price
        # print(jia,"@"*10)

        good_dict = {}
        # 都写在字典中
        good_dict['number'] = int(zhi)
        total_price = good_dict['number'] * jia
        good_dict['good_line'] = goods_line
        good_dict['total_price'] = total_price

        good_list.append(good_dict)
        # 最后用append方法添加到列表里面去

    user_addres = [
        {"id": 1, "addr": "汉阳", "phone": "1231313", "fk_user_id": "用户777对象", "is_default": 1, "name": "张三"},
        {"id": 2, "addr": "光谷", "phone": "110119120", "fk_user_id": "用户777对象", "is_default": 0, "name": "李四"},
        {"id": 3, "addr": "汉口", "phone": "110119120", "fk_user_id": "用户777对象", "is_default": 0, "name": "王五"},
    ]
    # Payment_method = [
    #     {"Payment_method": ["支付宝", "微信", "第三方支付方式"]}
    # ]
    context = {
        'good_list': good_list,  # [{},{}]
        'user_addres': user_addres,
        'Payment_method': Payment_method()  # {"Payment_method":[]}
    }

    return render(request, 'snfresh/Order.html', context)


class SubmitView(View):
    def get(self, request):
        pass

    def post(self, request):
        print(">>>>>>>>>>>>>>>>>>>>>>>")

        # address user phone  地址
        res = request.POST.get("browser")
        list_res = res.split("-")
        print(type(res))  # <class 'str'>
        print(list_res[0])  # 光谷

        zhi_fu = request.POST.get("browse")
        print(type(zhi_fu), zhi_fu)
        if zhi_fu != "on":
            return HttpResponse("没有选择支付方式")
        else:
        # 插入数据
            cha = models.address.objects.create(
                address=list_res[0],
                user=list_res[1],
                phone=list_res[2],
            )
            cha.save()

            return HttpResponse("ok")
