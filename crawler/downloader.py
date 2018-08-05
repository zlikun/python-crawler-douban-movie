import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie': ''
}


def download(url):
    try:
        # 如果不登录抓取的数据可能会很有限（未证实），这里简化处理认证部分逻辑，直接把我的cookie信息复制过来
        resp = requests.get(url,
                            headers=HEADERS,
                            timeout=3.0)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(e)
    except Exception as e:
        print(e)