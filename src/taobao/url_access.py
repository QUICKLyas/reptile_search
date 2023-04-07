import url_creator as urlC


class visit(object):

    def __init__(self) -> None:
        taobao = urlC()
        self.url = taobao.create_url()
        pass

    def getHTML(self):
        
        try :
            r = requests.get(self.makeTargetUrl(1))
        pass

    def makeTargetUrl(self, page: int, pageSize=44) -> str:
        return self.url + "&s=" + str(pageSize * page)
