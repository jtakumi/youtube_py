from datetime import datetime
import datetime
from googleapiclient.discovery import build
import json
from os import listdir
import matplotlib as mpl
from pandas import read_json
from csv import writer
import os
import csv
import numpy as np
from operator import itemgetter

#ベースのディレクトリのパス
dir='nijisanji'

header=['ライバー','subscriberCount']
member_a=[]
video=[]
member_id=[]

today = datetime.date.today()
d1 = today.strftime('%y-%m-%d')

def load_id(path):
    #jsonファイル内にあるidデータを検索する
    try:
        with open(path,'r',encoding='utf-8') as f:
            fjn=json.load(f)
    except Exception as e:
        print(path)
        print(e)
    else:
        id=fjn['id']
        f.close()
        return id

def read_json(path):
    try:
        with open(path,'r',encoding='utf-8') as f:
            fjn=json.load(f)
    except Exception as e:
        print(e)
    else:
        vc=int(fjn['statistics']['subscriberCount'])
        f.close()
        return vc

def load_data():
    global member_a
    global member_id
    for i in listdir(dir):
        path=os.path.join(dir,i)
        id=load_id(path)
        member=os.path.splitext(os.path.basename(path))[0]
        member_a.append(member)
        member_id.append(id)

def make_file(youtube,tddir):
    global member_a
    global member_id
    for i in range(len(member_a)): 
        #すでに入手したyoutubeChannelのidを使って新しくデータを作る
        member_p=member_a[i] + '.json'
        path=os.path.join(tddir,member_p)
        search_respose=youtube.channels().list(
        part='snippet,statistics',
        id=member_id[i]
        ).execute()
        with open(path,'w',encoding='utf-8') as f:
            for search_result in search_respose.get('items',[]):
                if search_result['kind'] !='youtube#channel':
                    continue
                print(json.dumps(search_result,indent=2,ensure_ascii=False),file=f)

def make_csv(tddir):
    global member_a
    global video
    fn='niji_subscriber_before_sort' + d1 + 'data.csv'
    csv_dir=os.path.join('niji_csv',d1)
    path=os.path.join(csv_dir,fn)
    #utf-8 with BOM
    with open(path,'w',encoding='utf-8-sig') as wf:
        #改行まで書きます
        writer=csv.writer(wf,lineterminator='\n')
        #ヘッダーを書き出す
        print('DATA date is ',d1,file=wf)
        writer.writerow(header)
        #ソート前のデータを作る
        for j in range(len(video)):
            print(member_a[j],video[j],file=wf)

#ビデオ投稿数とメンバーの名前の配列を統合
    sm=list(zip(video,member_a))
    sm.sort(key=itemgetter(0))
    sm.reverse()
    #戻す
    video,member_a=zip(*sm)
    fna='niji_subscriber_after_sort' + d1 + 'data.csv'
    csv_dir=os.path.join('niji_csv',d1)
    path_a=os.path.join(csv_dir,fna)
    with open(path_a,'w',encoding='utf-8-sig') as wf:
         #改行まで書きます
        writer=csv.writer(wf,lineterminator='\n')
        #ヘッダーを書き出す
        print('descending order',file=wf)
        print('DATA date is ',d1,file=wf)
        writer.writerow(header)
        for j in range(len(video)):
            print(member_a[j],video[j],file=wf)


def make_dir():
    mkdir='mkdir '+ dir + d1
    csv_dir=os.path.join('niji_csv',d1)
    mk_csv_dir='mkdir '+ csv_dir
    os.system(mkdir)
    os.system(mk_csv_dir)
    todir=dir + d1
    return todir

def git(tddir):
    #自動commit
    gad='git add ' + tddir + '\.'
    git_csv='git add ' + 'niji_csv\.'
    os.system(gad)
    os.system(git_csv)
    """print('Do you want to commit? [y/n]')
    dc=input()
    if(dc=='y'):
        gcm='git commit -m ' + d1
        os.system(gcm)
    else:
        print('Bye')"""


def main():
     #API情報
    API_KEY='own_key'
    YOUTUBE_API_SERVICE_NAME='youtube'
    YOUTUBE_API_VERSION='v3'

    youtube=build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey = API_KEY
    )

    
    load_data()
    tddir=make_dir()
    make_file(youtube,tddir)
    for i in range(len(member_a)): 
        member_p=member_a[i] + '.json'
        path=os.path.join(tddir,member_p)
        video.append(read_json(path))

    make_csv(tddir)
    git(tddir)

if __name__== '__main__':
    main()
