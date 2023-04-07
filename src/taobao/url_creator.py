import url_body


class taobao_url(object):
    def __init__(self) -> None:
        self.start_url = url_body.url['taobao']
        pass

    # 返回一个简单的url用于淘宝的数据的获取
    def create_url(self):
        goods = input("please input the name of goods:")
        if goods == None:
            goods = "大米"
        self.start_url = self.start_url + \
            "&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20230407&" + \
            "ie=utf8&bcoffset=1&ntoffset=1&p4ppushleft=2%2C48" + \
            goods
        return self.start_url

    def create_head(self):
        self.head = {
            'User-Agent': url_body.ua,
            # 自行获取
            # 'cookie': 'miid=500474353987730592; enc=eK7WndYxTupaB8JNpO02SwrSttE/Kcsc3s8zBEmTAivg2x2mC1NPgHBbjkVPBl9qLhFRSsDy+NpinBm553ElAJCHKhvq/DgbuxNn0sv6m3MxHD2HyYluOyFErXk6/EkA; _m_h5_tk=9434f96afc15a8977b1c88fb1f45a4a1_1680884426340; _m_h5_tk_enc=7033d50a2067018840d70f119b7def77; xlly_s=1; cookie2=173f740e8c155ce2ab4be6b2995b49c9; t=471b9c9ae7893a6c803c310ecff17d32; _tb_token_=4aeee6fee177; _samesite_flag_=true; sgcookie=E100h23Q32ntYL8RciCxydMCxJrvGCRdelE8917eYZ0gWA9Ks6YxxwV4jBLtCTgovHEqfhhtYXRsIp3IK/XofjG/YJcH9JC8y7eDqKK6fSGGilJo/uLRzmUbuPQ4O8vM7UkC; unb=3419172803; uc3=vt3=F8dCsfUJYnCeeXWnDnk=&lg2=VT5L2FSpMGV7TQ==&nk2=Ggod2AsW&id2=UNQ2messrVWXsg==; csg=05e34a54; lgc=yabuto; cancelledSubSites=empty; cookie17=UNQ2messrVWXsg==; dnk=yabuto; skt=af694f73b5a2f8cb; existShop=MTY4MDg3NzQ5MQ==; uc4=nk4=0@GIai/nj1yc6SaBZ4OdX6g80=&id4=0@UgP9omHkiU1olhDPi4de+qDvJcJN; tracknick=yabuto; _cc_=UIHiLt3xSw==; _l_g_=Ug==; sg=o31; _nk_=yabuto; cookie1=VTsWQsh4Wp+zjZqF2Tn/luAS9EHNv9O5eGj559wCMIY=; mt=ci=4_1; thw=cn; uc1=existShop=false&cookie14=Uoe8iqMd0Jl1VA==&pas=0&cookie15=UtASsssmOIJ0bQ==&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw==&cookie21=VT5L2FSpczFp; ariaDefaultTheme=undefined; isg=BLa23bfSzjFOnr6W9_-_mQE6B-y41_oRFQptUyCfohk0Y1b9iGdKIRwSez8PS_Ip; l=fBgnTVvujdfTUCE5BOfwPurza77OSIRAguPzaNbMi9fPOb5B58kdW1gxgOL6C3GVF6uyR3o-P8F6BeYBqQd-nxvOMiMVIODmndLHR35..; tfstk=c1lABJ0V73xmB3-gaSplbUc6v1KhwyQYjZZO6X2toUa_wu1cGXcdN-pb7krvy'
        }
        return self.head
