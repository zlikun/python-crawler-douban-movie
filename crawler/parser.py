import datetime
import urllib.parse

from bs4 import BeautifulSoup


def parse(html, url):
    soup = BeautifulSoup(html, 'html.parser')

    # 超链接列表
    links = []
    for a in soup.select('#paginator > a'):
        links.append(urllib.parse.urljoin(url, a.get('href')))

    # 数据列表
    results = []
    # 根据 status 参数判断用户是否看过
    is_visit = ('status=P' in url)
    for div in soup.select('#comments > div.comment-item'):
        author = div.select_one('h3 > span.comment-info > a').get_text(strip=True)
        date = div.select_one('h3 > span.comment-info > span.comment-time').get_text(strip=True)
        rating = div.select_one('h3 > span.comment-info > span.rating')
        star = None
        if rating is not None:
            star = rating.get('class')[0].replace('allstar', '')
        vote = div.select_one('h3 > span.comment-vote > span.votes').get_text(strip=True)
        comment = div.select_one('div.comment > p').get_text(strip=True)
        results.append({
            'author': author,
            'date': datetime.datetime.strptime(date, '%Y-%m-%d'),
            'star': star,
            'vote': int(vote),
            'comment': comment,
            'is_visit': is_visit
        })

    return links, results
