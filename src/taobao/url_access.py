import url_creator as urlC
import requests


class visit(object):
    def __init__(self) -> None:
        taobao = urlC.taobao_url()
        self.url = taobao.create_url()
        self.headers = taobao.create_head()
        pass

    def getHTML(self, page: int):
        try:
            r = requests.get(
                self.makeTargetUrl(page=page),
                timeout=30, headers=self.headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print("Failed to get page")
            return None

    def makeTargetUrl(self, page: int, pageSize=44) -> str:
        return self.url + "&s=" + str(pageSize * page)
