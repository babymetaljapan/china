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
    with open("retrip.csv","w") as f:
        page_url = "https://retrip.jp/locations/Japan/?page="
        i = page_max
        while i>0:
            #page表示
            print(i)
            #時間制御
            time.sleep(1)
            #URL生成
            target_url = page_url+'{0:d}'.format(i)

            #ウェブアクセス
            net_check=0
            while net_check==0:
                try:
                    all_html = requests.get(target_url).text
                    net_check=1
                except:
                    print("ネットワークエラー再接続します")
                    time.sleep(5)

            #スクレイピング
            root = lxml.html.fromstring(all_html)
            art_title = root.xpath("//section/*//*[contains(@class,'exp')]/a")
            art_sub = root.xpath("//section/*//*[contains(@class,'sub')]")
            art_count = root.xpath("//section/*//*[contains(@class,'countView')]")

            #記事タイトルと記事先URLの出力
            t=0
            while t < len(art_title):
                TITLE = art_title[t].get("title")
                URL = "https://retrip.jp" + art_title[t].get("href")
                SUB = art_sub[t].text_content()
                CONTENT = art_count[t].text_content()
                obj = '"{}",{},{},{}\n'.format(TITLE,URL,SUB,CONTENT)
                obj_len = len(obj)
                #ファイル出力
                try:
                    f.write(obj)
                #UnicodeEncodeError時の対処
                except UnicodeEncodeError:
                    for j in range(0,obj_len):
                        try:
                            f.write(obj[j])
                            print(obj[j],end="")
                        except UnicodeEncodeError:
                            f.write("??")
                            print("encode error",end="")
                    print()
                t=t+1
            i=i-1

makelink()
