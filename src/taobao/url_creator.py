import url_body


class taobao_url(object):
    def __init__(self) -> None:
        self.start_url = url_body.url['taobao']
        pass

    # 返回一个简单的url用于淘宝的数据的获取
    def create_url(self):
        goods = input("please input the name of goods:")
        self.start_url = self.start_url + goods
        return self.start_url

    def create_head(self):
        self.head = {
            'User-Agent': url_body.ua
        }
        return self.head
