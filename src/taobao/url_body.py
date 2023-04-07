from fake_useragent import UserAgent as ua

ua = ua().chrome
url = {
    "taobao": "https://s.taobao.com/search?q=",
}
# https://s.taobao.com/search?q=%E5%A4%A7%E7%B1%B3&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306
# https://s.taobao.com/search?q=%E5%A4%A7%E7%B1%B3&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&p4ppushleft=2%2C48&s=44
# https://s.taobao.com/search?q=%E5%A4%A7%E7%B1%B3&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&p4ppushleft=2%2C48&s=132
# https://s.taobao.com/search?q=%E5%A4%A7%E7%B1%B3&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=-2&ntoffset=-2&p4ppushleft=2%2C48&s=88
# https://s.taobao.com/search?q=%E5%A4%A7%E7%B1%B3&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=-5&ntoffset=-5&p4ppushleft=2%2C48&s=132
