import requests

from lxml import etree

url = "https://search.suning.com/进口水果/&sc=0&sc=0&ct=1&st=0#second-filter"
headers = {"User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
con = requests.get(url)
res =con.content.decode()
eobj = etree.HTML(res)
obj = eobj.xpath('//ul[@class="sort-list"][@class="sort-item"]/span/text()')
print(obj)
