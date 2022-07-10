from googleapiclient.discovery import build
import json
import os
import datetime
import sys
import shutil

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

#search dirのjsonファイルに結果を書きこむ

fn='search/search_' + search_word + '.json'
fny='youtube-json/' +  search_word + '.json'
fnj=search_word+'.json'

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

#searchにファイルを作成
def make_file(fn):
    with open(fn,'w',encoding='utf-8') as f:
        wf=0
        #検索結果が複数なら","をエラー対策でつけたい
        for search_result in search_respose.get('items',[]):
            if wf==0:
                if search_result['id']['kind'] !='youtube#channel':
                    continue
                print(json.dumps(search_result,indent=2,ensure_ascii=False),file=f)
                wf=1
            else:
                break

def read_json(fn,search_word):
    #ファイルがなかったときは強制終了
    try:
        with open(fn,"r",encoding='utf-8') as f:
            jsn=json.load(f)
    except Exception as e:
        print(e)
        sys.exit()
    else:
        #idというkeyの中のchannelIdを取り出す
        return jsn['id']['channelId']


    
#youtube-jsonにファイルを作成
def file_make(fny,idc):
    search_id=youtube.channels().list(
        part='snippet,statistics',
        id=idc
        ).execute()
    with open(fny,'w',encoding='utf-8') as f:
        for search_result in search_id.get('items',[]):
            if search_result['kind'] !='youtube#channel':
                continue
            print(json.dumps(search_result,indent=2,ensure_ascii=False),file=f)

def fcopy(fny,fnj):
    njsnj='nijisanji/' +  fnj
    shutil.copyfile(fny,njsnj)
    return njsnj

def git(fn,fny,njf):
    #自動commit
    gad='git add ' + fn + ' ' + fny +' ' +  njf
    os.system(gad)
    


def main():
    make_file(fn)
    idc=read_json(fn,search_word)
    file_make(fny,idc)
    njf=fcopy(fny,fnj)
    git(fn,fny,njf)


if __name__ == '__main__':
    main()