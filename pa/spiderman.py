import requests
from lxml import etree


class WuyouSpider:
    def __init__(self):
        """初始化操作"""
        # self.url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        self.data_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def start(self, key):
        """爬虫程序启动"""
        # 调用一个解析方法，得到请求后的内容

        # content = self.parse_url(self.url)

        content = self.parse_url(self.data_url.format(key))

        # 把提取数据的工作，交给一个方法来处理
        job_dict_list = self.get_data(content)

        # 打印最后得到的结果
        # print(job_dict_list)
        # print('成功获取了{}条数据'.format(len(job_dict_list)))
        # for job_dict in job_dict_list:
        #     print(job_dict)

        # 返回运行的结果
        return job_dict_list  # [{},{}]

    def parse_url(self, url):
        """
        解析url，发起请求，获取响应
        :param url: 需要请求的网址
        :return content: 请求所得到的内容
        """
        # 发起请求，获取响应
        res = requests.get(url, headers=self.user_agent)
        # print('得到的响应对象是', res)
        # 获取响应的内容
        content = res.content.decode('gbk')
        return content

    def get_data(self, content):
        """
        从内容中提取有效的数据
        :return:
        """
        # 获取一个对象
        eobj = etree.HTML(content)
        divs = eobj.xpath("//div[@id='resultList']/div[@class='el']")

        # 数据容器，存储内容
        job_dict_list = list()

        # 遍历每一个div，提取相关的数据
        for div in divs:
            print(type(div))
            # 获取岗位名称
            name = div.xpath("./p//a/@title")[0]
            job_url = div.xpath("./p//a/@href")[0]
            # 获取工作单位
            company = div.xpath("./span[1]/a/@title")[0]
            company_url = div.xpath("./span[1]/a/@href")[0]
            # 工作地点
            place = div.xpath("./span[2]/text()")[0]
            # 薪资水平
            temp_salary = div.xpath("./span[3]/text()")
            salary = temp_salary[0] if len(temp_salary) else "面议"
            # 发布日期
            pub_date = div.xpath("./span[4]/text()")[0]
            # 构建岗位数据字典
            job_info_dict = {
                "name": name,
                "job_url": job_url,
                "company": company,
                "company_url": company_url,
                "place": place,
                "salary": salary,
                "pub_date": pub_date,
            }
            # 把构建好的数据，添加到容器中，就是那个列表
            job_dict_list.append(job_info_dict)

        # 返回数据容器
        return job_dict_list


# wu = WuyouSpider()
# print(wu)
# wu.start()
