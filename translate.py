# クライアントIDに書いた文字列
clientId = 'project_china'
# 顧客の秘密に書かれていた文字列
clientSecret = 'vmefZLSAQKA7gt7fFzg5UApBBOwTGZhJXq9+Ab958YY='

from microsofttranslator import Translator
translator = Translator(clientId, clientSecret)

retrip1="いつか全て巡ってみたい！日本のSNS映えスポットランキングTOP10"
retrip2="食も雑貨も揃うオススメスポット！“学芸大学”にあるオシャレなお店15選"
retrip3="ここはエビ好きの天国！エビだらけのお店「ババガンプ・シュリンプ」とは"

#一天周圍都喜歡 ！ 日本 SNS 光澤現貨排名 TOP10
print(translator.translate(text=retrip1, to_lang='zh-TW', from_lang='ja'))
#ある日の周りのような！日本のSNS光沢のあるスポットランキングTOP10

#推薦點食物和雜物是可用 ！ 時尚商店 15 選舉是"學藝大學"
print(translator.translate(text=retrip2, to_lang='zh-TW', from_lang='ja'))
#いくつかの食品や雑貨が用意されていおすすめ！ファッションショップ15選挙は「学芸大学」でした


#這是一個像蝦一樣的天堂 ！ 布巴阿甘蝦蝦沾滿了商店
print(translator.translate(text=retrip3, to_lang='zh-TW', from_lang='ja'))
#これはエビのような楽園です！ババ・ガンプ・シュリンプシュリンプ覆わ店
