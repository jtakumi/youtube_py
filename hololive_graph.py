import json
from os import listdir
import matplotlib as mpl
from pandas import read_json
from csv import writer
import os
import csv

dir='.\hololive'

header=['ライバー','VideoCount']

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
    with open('hololive_videoCount.csv','w',encoding='utf-8') as wf:
        #改行まで書きます
        writer=csv.writer(wf,lineterminator='\n')
        #ヘッダーを書き出す
        writer.writerow(header)
        for i in listdir(dir):
            path=os.path.join(dir,i)
            vc=read_json(path)
            member=os.path.splitext(os.path.basename(path))[0]
            print(member,'videoCount=',vc)
            print(member,vc,file=wf)

if __name__== '__main__':
    main()
  
        