from django.shortcuts import render, HttpResponse, redirect
import requests
from pa import spiderman


# def dec_shu(request):
#     # ju = request.POST.get("shu")
#     # url = "https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(
#     #     ju)
#     # head = {
#     #     "User-Agent:" "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#     # conn = requests.get(url, headers=head)
#     # res = conn.content.decode("gbk")
#     # print(res)
#     # c =pa.on()
#     return redirect(dec_jie)


def dec_jie(request):
    key = request.POST.get("shu")
    xx = spiderman.WuyouSpider()
    # # key = request.POST.get("lie")
    res = xx.start(key)

    data_dict = {"job_data": res, "ti": key}
    return render(request, "job_list.html", data_dict)
