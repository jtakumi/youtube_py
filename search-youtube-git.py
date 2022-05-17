from googleapiclient.discovery import build
import json
import os
import datetime

"""
参考サイト
https://qiita.com/rkamikawa/items/dd1fd4c1427ece787eea
"""

#API情報
API_KEY='own-youtube-api-key'
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'
print('please input a  keyword.')
search_word=input()

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

#jsonファイルに結果を書きこむ

fn='search_' + search_word + '.json'

with open(fn,'w',encoding='utf-8') as f:
    for search_result in search_respose.get('items',[]):
        if search_result['id']['kind'] !='youtube#channel':
            continue
        print(json.dumps(search_result,indent=2,ensure_ascii=False),file=f)

#自動commit
gad='git add ' + fn + ' ' + 'search-youtube-git.py'
today=datetime.date.today()
d1=today.strftime('%y-%m-%d') + ':' +  fn
gcm='git commit -m ' + d1
os.system(gad)
os.system(gcm)


