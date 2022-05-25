import json
from os import listdir
import matplotlib as mpl
from pandas import read_json
from csv import writer
import os
import csv
import numpy as np
from operator import itemgetter

dir='.\hololive'

header=['ライバー','VideoCount']
member_a=[]
video=[]


def read_json(path):
    try:
        with open(path,'r',encoding='utf-8') as f:
            fjn=json.load(f)
    except Exception as e:
        print(e)
    else:
        vc=int(fjn['statistics']['videoCount'])
        f.close()
        return vc



def main():
    with open('./holo_csv/hololive_videoCount_sort.csv','w',encoding='utf-8') as wf:
        global member_a
        global video
        print('before sort')
        #改行まで書きます
        writer=csv.writer(wf,lineterminator='\n')
        #ヘッダーを書き出す
        print('descending order',file=wf)
        print('DATA date is 2022/5/18',file=wf)
        writer.writerow(header)
        for i in listdir(dir):
            path=os.path.join(dir,i)
            vc=read_json(path)
            member=os.path.splitext(os.path.basename(path))[0]
            member_a.append(member)
            video.append(vc)
            print(member,'videoCount=',vc)
        
        #ビデオ投稿数とメンバーの名前の配列を統合
        sm=list(zip(video,member_a))
        sm.sort(key=itemgetter(0))
        sm.reverse()
        #戻す
        video,member_a=zip(*sm)
        for j in range(len(video)):
            print(member_a[j],video[j],file=wf)

                       

if __name__== '__main__':
    main()
  
        