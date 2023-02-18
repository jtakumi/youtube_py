from googleapiclient.discovery import build
import json
import os
import datetime
import sys

key=''

"""
参考サイト
https://qiita.com/rkamikawa/items/dd1fd4c1427ece787eea
https://ccie-go.com/python-json/#toc9
https://techacademy.jp/magazine/23279
"""

def read_json():
    key=input()
    fnp='search/search_' + key + '.json'

    #ファイルがなかったときは強制終了
    try:
        with open(fnp,"r",encoding='utf-8') as f:
            jsn=json.load(f)
    except Exception as e:
        sys.exit('error')
        
    else:
        #idというkeyの中のchannelIdを取り出す
        return jsn['id']['channelId']
    

def file_make(fn,search_respose):
    with open(fn,'w',encoding='utf-8') as f:
        for search_result in search_respose.get('items',[]):
            if search_result['kind'] !='youtube#channel':
                continue
            print(json.dumps(search_result,indent=2,ensure_ascii=False),file=f)

def git(fn):
    #自動commit
    gad='git add ' + 'youtube-json/'+ fn
    os.system(gad)
    print('Do you want to commit? [y/n]')
    dc=input()
    if(dc=='y'):
        today=datetime.date.today()
        d1=today.strftime('%y-%m-%d')
        gcm='git commit -m ' + d1
        os.system(gcm)
    else:
        print('Bye')



#API情報
API_KEY='AIzaSyBqcCdqt3MGyFiAp9mmmHsMt5JjwJBSiGY'
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'

print("please input the keyword.")
search_word=read_json()


#jsonファイルに結果を書きこむ
fn = 'youtube-json/' +  key + '.json'


youtube=build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY
)

search_respose=youtube.channels().list(
    part='snippet,statistics',
    id=search_word
).execute()

file_make(fn,search_respose)
git(fn)


