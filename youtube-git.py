from googleapiclient.discovery import build
import json
import os 
import datetime

"""
参考サイト
https://qiita.com/rkamikawa/items/dd1fd4c1427ece787eea
"""

#API情報
API_KEY='OWN_YOUTUBE_API_KEY'
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'
search_word='UC8xkzBruPP96NI22ki4mB_w'


youtube=build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey = API_KEY
)

search_respose=youtube.channels().list(
    part='snippet,statistics',
    id=search_word
).execute()

#jsonファイルに結果を書き込む
print('please input file name.(no extension)')
fn=input()
fn=fn+'.json'

with open(fn,'w',encoding='utf-8') as f:
    for search_result in search_respose.get('items',[]):
        if search_result['kind'] !='youtube#channel':
            continue
        print(json.dumps(search_result,indent=2,ensure_ascii=False),file=f)

#自動commit
gad='git add ' + fn + ' ' + 'youtube-git.py'
today=datetime.date.today()
d1=today.strftime('%y-%m-%d')
gcm='git commit -m ' + d1
os.system(gad)
os.system(gcm)
os.system('git push origin y1')