from urllib import request


if __name__ == "__main__":
    print('urllib.')
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    html = html.decode("utf-8")
    print(html)

    print(response.geturl())
    print(response.getcode())
    print(response.info())