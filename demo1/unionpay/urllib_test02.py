import urllib.request
from urllib import parse
from io import BytesIO
import gzip

import lxml.etree
import shutil

cookie = 'WEBSITE_LANG=zh-cn; bke_newmcms=aEqr9X5UBRS0GIYmGw6iWACoSxI4NP8h8D68ymC9.spmcs01mcs01; WEBSITE_LANG=zh-cn; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22176a82e94713b2-08d4c4b015e508-c791039-2073600-176a82e94721cb%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fopen.unionpay.com%2Ftjweb%2Flogin%3FservletPath%3D%252Fuser%252FmchTest%252Fparam%22%7D%2C%22%24device_id%22%3A%22176a82e94713b2-08d4c4b015e508-c791039-2073600-176a82e94721cb%22%7D'


#
# 下载电子回执单
#
def eleBill(dtlTransNo, dtlTransIdx, dtlMchntOrderId, dtlTransStDesc):
    if dtlTransIdx.strip() == '':
        return
    else:
        print(dtlTransNo)
        print(dtlTransIdx)
        print(dtlMchntOrderId)
        print(dtlTransStDesc)

        request_url = 'https://merchant.unionpay.com/mcms/B2B/transQry!vaildDownPdfFile.action'
        request = urllib.request.Request(requet_url)

        request.add_header('Accept', '*/*')
        request.add_header('Accept-Encoding', 'gzip, deflate, br')
        request.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
        request.add_header('Connection', 'keep-alive')
        request.add_header('Content-Length', '96')
        request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        # request.add_header('Cookie', 'WEBSITE_LANG=zh-cn; bke_newmcms=yX2OJyt1UUFBR1K4L6U36zASWR4hrHtz61vB5MtC.spmcs01mcs04; WEBSITE_LANG=zh-cn')
        request.add_header('Cookie', cookie)
        request.add_header('Host', 'merchant.unionpay.com')
        request.add_header('Origin', 'https://merchant.unionpay.com')
        request.add_header('Referer', 'https://merchant.unionpay.com/mcms/login/index.action')
        request.add_header('sec-ch-ua', '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"')
        request.add_header('sec-ch-ua-mobile', '?0')
        request.add_header('Sec-Fetch-Dest', 'empty')
        request.add_header('Sec-Fetch-Mode', 'cors')
        request.add_header('Sec-Fetch-Site', 'same-origin')
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
        request.add_header('X-Requested-With', 'XMLHttpRequest')

        # print "downloading with urllib"
        # url = 'http://download.redis.io/releases/redis-5.0.5.tar.gz'
        # print "downloading with urllib"
        # urllib.urlretrieve(url, "demo.zip")
        post_data = {}
        post_data['dtlTransNo'] = '439069209280950510606'
        post_data['dtlTransDt'] = '20201218'
        post_data['b2bElecReceiptType'] = '01'
        data = parse.urlencode(post_data).encode('utf-8')
        response = urllib.request.urlopen(request, data)
        htmlres = response.read()
        buff = BytesIO(htmlres)
        f = gzip.GzipFile(fileobj=buff)
        print(f)

        # print(response)
        # print(response.fp)
        # print(response.version)
        # print(response.status)
        # print(response.getcode())
        # print(response.reason)
        # print(response.geturl())
        # print(response.getheader(name="Content-Type"))
        # print(response.getheaders())
        # print(response.info())
        # shutil.copyfileobj(response.fp, 'D:/hello.pdf')

        shutil.copyfileobj(f, open('D:/hello.pdf', 'wb'))
        # myfile = open('d:/' + dtlMchntOrderId +  '.pdf', 'wb')
        # shutil.copyfileobj(response.fp, myfile)
        # myfile.close()

        # 下载百度log图片
        # data1 = urllib.request.urlretrieve("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png", "d:/baidu_log.png")
        # data1 = urllib.request.urlretrieve(request, 'd:/' + dtlMchntOrderId + '.pdf', 'loading', data)

        return


if __name__ == "__main__":
    requet_url = 'https://merchant.unionpay.com/mcms/B2B/transQry!qryTransPage.action'
    request = urllib.request.Request(requet_url)
    request.add_header('Accept', '*/*')
    request.add_header('Accept-Encoding', 'gzip, deflate, br')
    request.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
    request.add_header('Connection', 'keep-alive')
    request.add_header('Content-Length', '181')
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    # request.add_header('Cookie', 'WEBSITE_LANG=zh-cn; bke_newmcms=yX2OJyt1UUFBR1K4L6U36zASWR4hrHtz61vB5MtC.spmcs01mcs04; WEBSITE_LANG=zh-cn')
    request.add_header('Cookie', cookie)
    request.add_header('Host', 'merchant.unionpay.com')
    request.add_header('Origin', 'https://merchant.unionpay.com')
    request.add_header('Referer', 'https://merchant.unionpay.com/mcms/login/index.action')
    request.add_header('sec-ch-ua', '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"')
    request.add_header('sec-ch-ua-mobile', '?0')
    request.add_header('Sec-Fetch-Dest', 'empty')
    request.add_header('Sec-Fetch-Mode', 'cors')
    request.add_header('Sec-Fetch-Site', 'same-origin')
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    request.add_header('X-Requested-With', 'XMLHttpRequest')

    post_data = {}
    post_data['startDate'] = '2020-12-18'
    post_data['endDate'] = '2020-12-18'
    data = parse.urlencode(post_data).encode('utf-8')
    response = urllib.request.urlopen(request, data)
    htmlres = response.read()
    buff = BytesIO(htmlres)
    f = gzip.GzipFile(fileobj=buff)
    htmls = f.read().decode('utf-8')
    # print(htmls)
    # target_lable = dom.xpath("//div[@id='target_lable_id']")[0]
    # target_lable = dom.xpath("//tr")[0]
    doc = lxml.etree.HTML(htmls)
    allTrs = doc.xpath("//tr")
    print(len(allTrs))
    # titleTr = allTrs[0]
    # titleTds = titleTr.xpath('//th/text()')
    # print(titleTds)
    # print(len(titleTds))
    dtlTransNo = allTrs[0].xpath('//td[@class="txtCenter"]/input[@name="dtlTransNo"]/@value')
    dtlTransIdx = allTrs[0].xpath('//td[@class="txtCenter"]/input[@name="dtlTransIdx"]/@value')
    dtlMchntOrderId = allTrs[0].xpath('//td[@class="txtCenter"]/input[@name="dtlMchntOrderId"]/@value')
    dtlTransStDesc = allTrs[0].xpath('//td[@class="txtCenter"]/input[@name="dtlTransStDesc"]/@value')

    print(dtlTransNo)
    print(dtlTransIdx)
    print(dtlMchntOrderId)
    print(dtlTransStDesc)

    num = 0
    while num < len(dtlTransIdx):
        eleBill(dtlTransNo[num], dtlTransIdx[num], dtlMchntOrderId[num], dtlTransStDesc[num])
        num = num + 1
