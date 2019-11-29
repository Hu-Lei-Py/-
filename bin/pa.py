import requests
from lxml import etree


class Fresh():
    def __init__(self):
        self.url = "https://search.suning.com/进口水果/&sc=0&sc=0&ct=1&st=0#second-filter"
        self.url_two = "https://sxs.suning.com/sxspc_huadong.html?safp=d488778a.newchaoshihome.80201522566.1"
        self.headers = {
            "User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def climb(self):
        res = requests.get(self.url, self.headers)
        data = res.content.decode()
        return data

    def climb_two(self):
        res = requests.get(self.url_two, self.headers)
        data = res.content.decode()
        return data

    def Analysis_data(self, Receive_data):
        eobj = etree.HTML(Receive_data)
        # 商品名称

        # 图片路径
        res_two = eobj.xpath("//div[@class='img-block']/a/img/@src")[0]
        first = {"图片地址": res_two, "商品价格": None, "商品名称": None}

        # 商品价格

        return first

    def class_data(self, Receive_data):
        """
        分类
        :param Receive_data:
        :return:
        """
        eobj = etree.HTML(Receive_data)
        # res = eobj.xpath("//li[@class='sort-item']/span/text()")[0]
        res = eobj.xpath("//li[@class='sort-item']/span/a")
        return res

    def run(self):
        """
        启动
        :return:
        """
        climb_data = self.climb()
        climb_data_two = self.climb_two()
        # 商品详情页
        shu = self.Analysis_data(climb_data)
        # 主页
        shu_two = self.class_data(climb_data_two)
        print(shu_two)


if __name__ == '__main__':
    test = Fresh()
    test.run()
    # test.climb()
    # test.Analysis_data()
    test.class_data()
# ￥
# //div[@class='price-box']/span/i[1]/text()
# 25
# //div[@class='price-box']/span/text()
# 0.80
# //div[@class='price-box']/span/i[last()]/text()
