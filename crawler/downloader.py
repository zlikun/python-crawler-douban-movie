import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie': 'gr_user_id=b6c0778d-f8df-4963-b057-bd321593de1e; __yadk_uid=SVIYYP9lXyOGypIDdCCjpK1m0uBlLlhW; bid=T-M5aFmoLY0; viewed="26311273_26877306_26340992_26649178_3199438_3015786_27038473_10793398_26754665"; ll="108296"; ps=y; _vwo_uuid_v2=E57494AA9988242B62FB576F22211CE4|e95afc3b3a6c74f0b9d9106c6546e73e; ct=y; as="https://movie.douban.com/subject/26752088/comments?start=100&limit=20&sort=new_score&status=P"; dbcl2="141556470:wy9CrWy1wmk"; ck=z-r8; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1531450593%2C%22https%3A%2F%2Fopen.weixin.qq.com%2Fconnect%2Fqrconnect%3Fappid%3Dwxd9c1c6bbd5d59980%26redirect_uri%3Dhttps%253A%252F%252Fwww.douban.com%252Faccounts%252Fconnect%252Fwechat%252Fcallback%26response_type%3Dcode%26scope%3Dsnsapi_login%26state%3DT-M5aFmoLY0%252523None%252523%252F%22%5D; _pk_id.100001.8cb4=19ef2583613054ed.1500397890.16.1531450593.1531191390.; _pk_ses.100001.8cb4=*; push_doumail_num=0; __utmt=1; __utma=30149280.1283677058.1481968276.1531412908.1531450277.39; __utmb=30149280.2.10.1531450277; __utmc=30149280; __utmz=30149280.1524482884.31.29.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.14155; ap=1; push_noty_num=0'
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