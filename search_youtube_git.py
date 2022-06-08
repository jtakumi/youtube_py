from googleapiclient.discovery import build
import json
import os
import datetime

"""
参考サイト
https://qiita.com/rkamikawa/items/dd1fd4c1427ece787eea
"""

#API情報
API_KEY='own_key'
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'
print('please input a  keyword.')
search_word=input()

#jsonファイルに結果を書きこむ

fn='search/search_' + search_word + '.json'


youtube=build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY
)

search_respose=youtube.search().list(
    q=search_word,
    part='id,snippet',
    maxResults=25
).execute()


def make_file():
    with open(fn,'w',encoding='utf-8') as f:
        for search_result in search_respose.get('items',[]):
            if search_result['id']['kind'] !='youtube#channel':
                continue
            print(json.dumps(search_result,indent=2,ensure_ascii=False),file=f)

def git():
    #自動commit
    gad='git add ' + fn
    os.system(gad)
    print('Do you want to move to youtube.py?[y/n]')
    dc=input()
    if(dc=='y'):
        import youtube
        youtube.main()
    else:
            print('Bye')

def main():
    make_file()
    git()


