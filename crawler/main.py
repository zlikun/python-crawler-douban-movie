# 爬虫启动入口

from crawler.manager import Manager
from crawler.downloader import download
from crawler.parser import parse
from crawler.processor import Processor

movie_id = 26752088
base_url = 'https://movie.douban.com/subject/{}/comments'.format(movie_id)


class Crawler(object):

    def __init__(self):
        self._manager = Manager(base_url)
        self._processor = Processor(host='192.168.0.105',
                                    collection='movie_{}_comments'.format(movie_id))

    def start(self, urls):
        """
        启动爬虫方法
        :param urls: 启动URL
        :return: 抓取的URL数量
        """
        number = 0
        self._manager.append_new_urls(urls)
        while self._manager.has_new_url():
            number += 1
            new_url = self._manager.get_new_url()
            print('开始下载第{:03}个URL：{}'.format(number, new_url))
            html = download(new_url)
            if html is None:
                # print('html is empty .')
                continue
            links, results = parse(html, new_url)
            if len(links) > 0:
                self._manager.append_new_urls(links)
            if len(results) > 0:
                self._processor.process(results)
        return number


if __name__ == "__main__":
    crawler = Crawler()
    # 同时抓取看过和未看过的链接，两者区别在于status查询参数上
    root_urls = ['?'.join([base_url, 'start=0&limit=20&sort=new_score&status=P']),
                 '?'.join([base_url, 'start=0&limit=20&sort=new_score&status=F'])]
    nums = crawler.start(root_urls)
    print('爬虫执行完成，共抓取{}个URL'.format(nums))
