import requests


header = {"Accept": "text/plain, */*; q=0.01",
          "Accept - Encoding": "gzip, deflate, br",
          "Accept-Language": "en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6",
          "Connection": "keep-alive",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}


def get_urls():
    r = requests.get("https://www.baidu.com", header=header)
    print(r.text)
