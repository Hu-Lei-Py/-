import requests
import re
import json

import time
import random

class QcwySpider:
    def __init__(self):
        """初始化"""
        # url模板
        self.base_url="https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        self.start_url = self.base_url.format(1)
        # 请求列表
        self.url_list = list()
        # 数据存放的列表
        self.data_list = list()

    def update(self):
        self.make_url_list()
        # 往self.url_list中添加每一个文章列表页的url

        # 遍历请求列表依次发起请求，获取全部文章的数据
        self.parse_url_list()

        # 数据保存到文件中，保存为json格式
        # 当前的所有数据都在self.data_list
        self.save_data()

    def parse_url_list(self):
        for url in self.url_list:
            print('当前页码链接', url)
            html = self.parse_url(url)
            # print('html')
            # print(html)
            # print('*'*10)
            # title = self.get_title()
            # href = self.get_href()

            # 从html中抽出文章的标题与链接
            self.add_article_data(html)

            n = random.randint(1,5)
            time.sleep(n)

    def add_article_data(self,html):
        """
        从html中抽出文章的标题与链接
        :param
        html: 一个列表页的html代码
        :return:
        """
        com = re.compile(r'<div class="el">.*?</div>', re.DOTALL)
        div_list = com.findall(html)
        print(div_list)
        for div in div_list:
            d1 = re.compile(r'<a target="_blank" title="(.*?) href="(.*?)">(.*?)')
            href = d1.findall(div)

            # print("职位",href[0][0],"公司名",href[1][0],"链接",href[1][1])
            position=href[0][0]

            # s1 = re.compile(r'<p class="t1 tg1"<span ><a target="_blank" href="(.*?)">')
            # link = s1.findall(div)
            s2 = re.compile(r'<span class="t2">(.*?)</span>')
            Company_name = s2.findall(div)


            link=href[0][1]

            s3 = re.compile(r'<span class="t3">(.*?)</span>')
            address=s3.findall(div)
            # print("地址：",address)


            s4 = re.compile(r'<span class="t4">(.*?)</span>')
            wages = s4.findall(div)
            # print("工资：", wages)
            # <a target="_blank" title="成都天府新区创新创业人才服务中心" href="https://jobs.51job.com/all/co5670045.html">成都天府新区创新创业人才服务中心...</a>
            if not all([position,Company_name,link,address,wages]):
                print("爬到空数据position",position),
                print("爬到空数据Company_name",Company_name),
                print("爬到空数据link",link),
                print("爬到空数据address",address),
                print("爬到空数据wages",wages),
                continue

            articel_data = {
                "position": position,  # "     标题      "    []
                "Company_name": Company_name,#公司名
                "link":link,#链接
                "address":address[0].strip(),#地址
                "wages":wages[0].strip(),#工资
            }
            # print('得到的文章字典为：')
            print(articel_data)
            self.data_list.append(articel_data)
            print('self.datalist')
            print(self.data_list)


    def save_data(self):
        """ 保存数据到文件中，用json """
        str_data = json.dumps(self.data_list, ensure_ascii=False)
        print("8888888",str_data)
        with open('data.db', 'w', encoding='utf8') as f:
            f.write(str_data)
            print("999999",str_data)



    def make_url_list(self):
        # 爬取第一页，获得html内容
        start_html = self.parse_url(self.start_url)
        # 保存爬取的内容
        # self.save_html(start_html)
        # 获取最大的页码数
        max_num = self.get_max_num(start_html)
        print(max_num)
        # 生成url请求列表
        self.add_url_by_max_num(max_num)

    def add_url_by_max_num(self, max_num):
        """根据最大页码数，生成URL列表"""
        for i in range(1, max_num + 1):
            # 拼url
            temp = self.base_url.format(i)
            self.url_list.append(temp)

        print(self.url_list)

    def get_max_num(self, html):
        """根据html内容，提取最大页码数"""
        # html 中 """<li data-page="38" class="ui-pager">38</li>"""
        # com = re.compile(r'<span class="count">742</span>')
        # 获取总页码数
        com = re.compile(r'<span class="td">[^\d]+(\d+)[^\d]+</span>')
        article_num = com.findall(html)
        # return int(article_num[0])        #最大页码数
        return int(20)


    def parse_url(self, url):
        """
        发起get请求，返回请求内容
        :param url:
        :return: 响应内容str
        """
        """发起get请求，返回响应的内容"""
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        response = requests.get(url, headers=header)
        print(response)
        return response.content.decode("gbk")

    # def save_html(self, html):
    #     """保存"""
    #     import time
    #     name = str(int(time.time())) + ".txt"
    #     with open(name, "w", encoding="utf8") as f:
    #         f.write(html)

if __name__ == '__main__':
    qcwy=QcwySpider()
    qcwy.update()
