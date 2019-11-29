from django.shortcuts import render, HttpResponse, redirect
from app import models
from jia import one
import json

def login(request):
    return render(request, "sou.html")


def zong(request):
    res = models.good_type.objects.all()

    for sp_list in res:
        sp_show = sp_list.good_info_set.all().order_by("-id")[:8]
        sp_list.show = sp_show

    # res_two = models.good_info.objects.all()
    res_dict = {"res_name": res, }
    return render(request, 'snfresh/goods.html', res_dict)


def data(request):
    data = [{'title': ['泰国 进口金枕头榴莲 单果2千克以上 新鲜水果'], 'price': 178.0,
             'img': 'https:https://uimgproxy.suning.cn/uimg1/sop/commodity/Adxs8eli9JewYQxtf7FTmw.png_800w_800h_4e'},
            {'title': ['泰国进口龙眼 桂圆 1kg装 新鲜水果'], 'price': 25.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/uYJk6Lm4XSqvgIqRNtty3A.jpg_800w_800h_4e'},
            {'title': ['【越南进口】玉芒果青芒5斤装 单果200g以上 当季新鲜热带水果青芒果 非台农凯特芒'], 'price': 29.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/Ru0buES1Hri2vj3xc-kxlQ.jpg_800w_800h_4e'},
            {'title': ['泰国 进口金枕头榴莲 单果1.5千克以上 新鲜水果'], 'price': 148.0,
             'img': 'https:https://uimgproxy.suning.cn/uimg1/sop/commodity/Adxs8eli9JewYQxtf7FTmw.png_800w_800h_4e'},
            {'title': ['【产地直发】雉鲜生 越南进口青芒 玉芒8斤装 新鲜水果'], 'price': 39.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/NnrDbEgPljzzaU5fLANoRg.jpg_800w_800h_4e'},
            {'title': ['大土澳 智利绿果12颗装 单果80-100g 智利进口绿心猕猴桃奇异果'], 'price': 37.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/keUlHIWEJ3NQHv3rxIFZEQ.jpg_800w_800h_4e'},
            {'title': [' ', ' ', ' 波得泰国进口急冻树熟金枕榴莲1.2-1.5kg简装'], 'price': 0,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/FGQ1HNGGjxFnDm3yMD5pGQ.jpg_800w_800h_4e'},
            {'title': ['越南进口红心火龙果 3个装 单果约330-420g 新鲜水果'], 'price': 24.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/8YNbndqmLWE4IehQPVx02A.jpg_800w_800h_4e'},
            {'title': ['【泰国进口】泰国龙眼 2斤 新鲜桂圆新鲜水果 香甜可口 多汁饱满'], 'price': 25.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/pwIXV6h8ldfyB0aVAwk58A.jpg_800w_800h_4e'},
            {'title': ['泰国进口椰青 椰子9个装 单果约750g 配开椰器和吸管 新鲜水果'], 'price': 98.0,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/6--0bA_lZsqnVneSF_5N5w.jpg_800w_800h_4e'},
            {'title': ['泰国 进口金枕头榴莲 单果3千克以上 新鲜水果'], 'price': 238.0,
             'img': 'https:https://uimgproxy.suning.cn/uimg1/sop/commodity/Adxs8eli9JewYQxtf7FTmw.png_800w_800h_4e'},
            {'title': ['大土澳 泰国进口椰青 9个装 单果750g以上 椰子 新鲜水果'], 'price': 108.0,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/mmhdXERsWnIqJlLTmCyjOw.jpg_800w_800h_4e'},
            {'title': ['墨西哥进口水果牛油果8个装 单果130克-160克 新鲜水果'], 'price': 84.0,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/3J3yKjdE7w6e3IP2JzPVJA.jpg_800w_800h_4e'},
            {'title': ['越南进口红心火龙果 4个装 单果约250~350g 新鲜水果'], 'price': 26.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/YQTElrNZZggdyC6cGPK1NQ.jpg_800w_800h_4e'},
            {'title': ['泰国进口水果释迦果3斤装4个果 新鲜水果'], 'price': 68.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/zELhGdZJx1ewxxhjMKtbMA.png_800w_800h_4e'},
            {'title': ['展卉 泰国进口龙眼 精选一级果 带箱5斤 净重4斤 新鲜水果'], 'price': 49.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/aVB0SOj3sBHwkmFzSpvfSA.jpg_800w_800h_4e'},
            {'title': [' ', ' ', ' 越南进口白心火龙果 3个装 中果 单果375~500g 新鲜水果'], 'price': 21.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/h25NS-FC2oeTrH3WQtajPw.jpg_800w_800h_4e'},
            {'title': ['恒虎 泰国树熟金枕冷冻榴莲果泥 500G*1袋装'], 'price': 59.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/uGasGcfm0dLEjrqHDTo13g.jpg_800w_800h_4e'},
            {'title': [' ', ' ', ' 波得泰国进口急冻树熟金枕榴莲1.5-2.2kg简装'], 'price': 0,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/bTxNnI4BrBwdeMX5lUbG0w.jpg_800w_800h_4e'},
            {'title': ['泰国 进口金枕头榴莲 一或两个总重4千克以上 新鲜水果'], 'price': 288.0,
             'img': 'https:https://uimgproxy.suning.cn/uimg1/sop/commodity/81ifEy-jSJyRvp8PoN4FuA.jpg_800w_800h_4e'},
            {'title': [' ', ' ', ' 进口红心火龙果 6个/盒 单果约350G-450G新鲜水果'], 'price': 128.0,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/wRPxLQ8b5JU6sZICuno7Qw.jpg_800w_800h_4e'},
            {'title': ['墨西哥进口水果牛油果6个装 单果130克-160克 新鲜水果'], 'price': 69.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/lSzvQfM1kMiK13LhDvNxSw.jpg_800w_800h_4e'},
            {'title': ['墨西哥进口水果牛油果4个装大果 单果160克-190克 新鲜水果'], 'price': 50.9,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/DGRuksrHLVsQ3goqeSrV9Q.jpg_800w_800h_4e'},
            {'title': ['进口水果 越南红心火龙果带箱2.5千克，新鲜水果'], 'price': 45.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/Z_LDP0L45RkxxmkWLC0nBQ.png_800w_800h_4e'},
            {'title': ['【越南进口】高乐蜜芒果 3斤装 单果200g以上 现摘当季孕妇水果时令新鲜甜水果 非凯特台农芒果'], 'price': 24.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/ujyRZFbwtKtxmORl-DolpA.jpg_800w_800h_4e'},
            {'title': ['恒虎泰国进口 冷冻无核金枕头烤榴莲肉 1盒装 4*100g/盒'], 'price': 92.0,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/Eid91yKu65f0-vQca2DyzA.jpg_800w_800h_4e'},
            {'title': [' ', ' ', ' 进口凤梨 2kg/盒 单果约1kg新鲜水果'], 'price': 61.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/EqvrMLuGrDYrsHR2TDys2Q.jpg_800w_800h_4e'},
            {'title': [' ', ' ', ' 进口白心火龙果 6个/盒 单果约350G-450G新鲜水果'], 'price': 72.8,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/n_3_wxG1yHlolhVhdwGjzA.jpg_800w_800h_4e'},
            {'title': [' ', ' ', ' 进口牛油果 6个/盒 单果约120g 新鲜水果'], 'price': 96.0,
             'img': 'https://imgservice.suning.cn/uimg1/b2c/image/qXr67haRGiReLSNAHOoHhg.jpg_800w_800h_4e'},
            {'title': ['泰国 进口金枕头榴莲 单果2.5千克以上 新鲜水果'], 'price': 208.0,
             'img': 'https:https://uimgproxy.suning.cn/uimg1/sop/commodity/Adxs8eli9JewYQxtf7FTmw.png_800w_800h_4e'}]
    good_num_list = 1
    for d in data:
        new_line = models.good_info()
        new_line.title = d['title']
        new_line.image = d['img']
        new_line.price = d['price']
        new_line.good_type_id = good_num_list
        new_line.save()
    return HttpResponse("OK")


def get_redis_conn():
    import redis
    ip = '121.40.207.159'
    port = 6379
    conn = redis.StrictRedis(host=ip, port=port, db=9)
    return conn


def text(request):
    res = request.GET.get('id', 0)
    print(res, '!!!!!!!!!!!!!')
    conn = get_redis_conn()
    # 用户id
    uid = 777
    car_key = "car_{}".format(uid)
    # num = conn.hget(car_key, id)
    # if num:
    #     new_num = int(num) + 1
    # else:
    #     new_num = 1
    re_two = conn.hset(car_key, res, "1")
    print(re_two)
    return HttpResponse("成功-{}".format(res))


# hset 键 字段1 值1
# hget 键 字段
def gouwuche(request):
    if request.method == 'GET':
        print('!!!!!!!!!!!!!!!')
        rlone = get_redis_conn()
        car_key = "car_777"
        qwe = rlone.hgetall(car_key)
        list_data = []
        for k, v in qwe.items():
            asd = models.good_info.objects.get(id=k)

            dict_qwe = {"titie": asd, "num": int(v)}
            list_data.append(dict_qwe)
            # print(list_data)
        # res = request.GET.getlist("goods_che")
        # res2 = request.GET.getlist("goods_shu")
        #     print(res3, "*" * 10)
        context = {
            'list_data': list_data
        }
        return render(request, "snfresh/gou.html", context)
    if request.method == 'POST':
        res = request.POST.get("id", [])  # [33,6]
        # print(res, "***")
        # print(type(res), "***")
        list = res.split(",")
        # print(list)
        gid = list[0]
        gnum = list[1]
        # print(gid)
        # print(gnum)
        context = {
            'status': 0,
            'msg': None,
        }
        try:
            models.good_info.objects.get(id=gid)
        except:
            context['status'] = 1
            context['msg'] = '商品下架了'
        return HttpResponse(json.dumps(context))
