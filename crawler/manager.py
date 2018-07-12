class Manager(object):

    def __init__(self, base_url=None):
        self.base_url = base_url
        self.new_urls = []
        self.old_urls = []

    def append_new_urls(self, urls):
        if len(urls) == 0:
            return
        for url in urls:
            # 过滤非目标URL
            if self.base_url not in url:
                continue
            # 去掉多余查询参数
            if '&percent_type=' in url:
                url = url.replace('&percent_type=', '')
            # URL重复检查
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.append(url)

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        """
        获取一个新的URL，内部隐含了URL抓取过后加入已抓取队列操作(所以这里不考虑实际抓取过程中的失败情况)
        :return:
        """
        url = self.new_urls.pop()
        self.old_urls.append(url)
        return url
