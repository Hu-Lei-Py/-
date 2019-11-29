from lxml import etree


def init():
    """初始化无头浏览器对象"""
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=opt)
    return browser


browser = init()


def get_html_by_chrome(url):
    """
    通过驱动谷歌无头浏览器，拿到url的响应代码
    :param url: 需要访问的url
    :return html: 拿到的渲染后的html代码，商品的代码，包含价格的
    """
    browser.get(url)
    # print(url)
    # print(browser.__dict__)
    # <class 'selenium.webdriver.chrome.webdriver.WebDriver'>
    # print(type(browser))
    html = browser.page_source
    return html


def save_html(html):
    """ 保存html到文件的方法 """
    with open('a.html', 'w', encoding='utf8') as f:
        f.write(html)


def get_good_price(html):
    """
    获取商品的价格，通过html的内容来获取
    :param html: html代码
    :return price: 提取出来的价格
    """
    # <span class="mainprice"><i>¥</i>79.<span>00</span>		  </span>
    obj = etree.HTML(html)
    # print(type(obj))
    # print(obj)
    data_list = obj.xpath("//span[@class='mainprice']//text()")
    # print(data_list)
    try:
        price = data_list[1] + data_list[2]  # "79.00"
        price = float(price)
    except:
        price = 0
    # print(price)
    return price


def get_good_title(html):
    obk = etree.HTML(html)
    data_obk_list = obk.xpath("//div[@class='proinfo-title']/h1/text()")
    return data_obk_list


def get_good_img(html):
    obk = etree.HTML(html)
    data_obk_list = obk.xpath("//div[@class='imgzoom-main']/a/img/@src")
    for i in data_obk_list:
        res = "https:" + i
        return res


def main(url):
    # 获得一个url
    # 发起一个请求，得到html
    html = get_html_by_chrome(url)
    # 保存html内容
    save_html(html)
    # 从html中提取出价格
    price = get_good_price(html)
    img = get_good_img(html)
    title = get_good_title(html)

    # 打印价格
    # print('商品的价格是{},商品名称是{},图片地址是{}'.format(price, title, img))
    return title, price, img

# main(url)
