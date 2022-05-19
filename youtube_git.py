from googleapiclient.discovery import build
import json
import os
import datetime
import search_youtube


"""
参考サイト
https://qiita.com/rkamikawa/items/dd1fd4c1427ece787eea
https://ccie-go.com/python-json/#toc9
https://techacademy.jp/magazine/23279
"""

def read_json():
    fnp='search/search_' + search_youtube.fn + '.json'

    with open(fnp,"r",encoding='utf-8') as f:
        jsn=json.load(f)
        #idというkeyの中のchannelIdを取り出す
        return jsn['id']['channelId']

def work():
    #API情報
    API_KEY='own_key'
    YOUTUBE_API_SERVICE_NAME='youtube'
    YOUTUBE_API_VERSION='v3'

    print("please input the channel's id.")
    search_word=read_json()

    #jsonファイルに結果を書きこむ
    print('please input file name.(no extension)')
    fn=input()
    fn=fn+'.json'


    youtube=build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey = API_KEY
    )

    search_respose=youtube.channels().list(
        part='snippet,statistics',
        id=search_word
    ).execute()





    with open(fn,'w',encoding='utf-8') as f:
        for search_result in search_respose.get('items',[]):
            if search_result['kind'] !='youtube#channel':
                continue
            print(json.dumps(search_result,indent=2,ensure_ascii=False),file=f)

    mvf='mv'+ ' '+ fn + ' ' + 'youtube-json'
    os.system(mvf)

    #自動commit
    gad='git add ' + 'youtube-json/'+ fn
    os.system(gad)
    print('Do you want to commit? [y/n]')
    dc=input()
    if(dc=='y'):
        today=datetime.date.today()
        d1=today.strftime('%y-%m-%d') + ':' +  fn
        gcm='git commit -m ' + d1
        os.system(gcm)
    else:
        print('Bye')


def main():
    work()