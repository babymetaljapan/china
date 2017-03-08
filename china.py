import requests
import lxml.html
import time

def makelink():
    #ページ最大値検索
    url = "https://retrip.jp/locations/Japan/"
    page_html = requests.get(url).text
    page_root = lxml.html.fromstring(page_html)
    page_cont = page_root.xpath("//*[contains(@class,'page')]")
    page_max = int(page_cont[-1].text_content())

    #記事読み込み
    page_url = "https://retrip.jp/locations/Japan/?page="
    #i = page_max
    i=1
    while i>0:
        #時間制御
        time.sleep(1)
        #URL生成
        target_url = page_url+'{0:d}'.format(i)
        #ウェブアクセス
        all_html = requests.get(target_url).text
        #スクレイピング
        root = lxml.html.fromstring(all_html)
        art_title = root.xpath("//section/*//*[contains(@class,'exp')]/a")
        art_sub = root.xpath("//section/*//*[contains(@class,'sub')]")
        art_count = root.xpath("//section/*//*[contains(@class,'countView')]")

        #記事タイトルと記事先URLの出力
        t=0
        while t < len(art_title):
            print(art_title[t].get("title"))
            art_url = "https://retrip.jp" + art_title[t].get("href")
            print(art_url)
            print(art_sub[t].text_content())
            print(art_count[t].text_content())
            print("\n")
            t=t+1
        i=i-1
        
makelink()

