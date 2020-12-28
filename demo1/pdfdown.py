import requests

# 下载银联回单
dtlTransNo = '795575815729295451705'
dtlTransDt = '20201217'
b2bElecReceiptType = '01'
url = "https://merchant.unionpay.com/mcms/B2B/transQry!downPdfFile.action?dtlTransNo=" + dtlTransNo + "&dtlTransDt= " + dtlTransDt + "&b2bElecReceiptType=" + b2bElecReceiptType
payload = {}
files = {}
headers = {
    'Cookie': 'WEBSITE_LANG=zh-cn; bke_newmcms=CebZCIXbL5VHAxp20pJ8zIdIOTee0XFjC0HTn5DB.spmcs01mcs04; WEBSITE_LANG=zh-cn; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22176a82e94713b2-08d4c4b015e508-c791039-2073600-176a82e94721cb%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fopen.unionpay.com%2Ftjweb%2Flogin%3FservletPath%3D%252Fuser%252FmchTest%252Fparam%22%7D%2C%22%24device_id%22%3A%22176a82e94713b2-08d4c4b015e508-c791039-2073600-176a82e94721cb%22%7D',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'Referer': 'https://merchant.unionpay.com/mcms/login/index.action',
    'Origin': 'https://merchant.unionpay.com',
    'Host': 'merchant.unionpay.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

with open('D:/xixi.pdf', "wb") as code:
    code.write(response.content)
