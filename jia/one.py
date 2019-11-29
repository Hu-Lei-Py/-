import requests
from lxml import etree
from jia import get_goods_info


class Fen():
    def __init__(self):
        self.url = "https://search.suning.com/进口水果/&sc=0&sc=0&ct=1&st=0#second-filter"

    def lei(self):
        c_list = []
        con = requests.get(self.url)
        te = con.content.decode()
        obj = etree.HTML(te)
        # 详情页路径
        data_list = obj.xpath("//div[@class='title-selling-point']/a/@href")
        for i in data_list:
            res = "https:" + i
            c_tuple = get_goods_info.main(res)
            c_dict = {
                "title": c_tuple[0],
                "price": c_tuple[1],
                "img": c_tuple[2],
            }
            c_list.append(c_dict)
        return c_list
        # print(c_list)

    def bao(self):
        cont = self.lei()
        with open("abc.txt", "w", encoding="utf8") as f:
            f.write(str(cont))


if __name__ == '__main__':
    text = Fen()
    # text.lei()
    text.bao()
