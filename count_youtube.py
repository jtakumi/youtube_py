import json
import os
import datetime

c=0
dir='.\hololive'
today=datetime.date.today()
today=today.strftime('%y/%m/%d')
with open('hololive_members.csv','w',encoding='utf-8') as f:
    print('---hololive members---',file=f)
    print('date:',today,file=f)
    print(file=f)
    for i in os.listdir(dir):
        c+=1
        #ファイルのパスを取得
        path=os.path.join(dir,i)
        #拡張子なしでファイル名を取得
        member=os.path.splitext( os.path.basename(path))[0]
        print(member,file=f)
    print(file=f)
    print("member count=",c,file=f)

os.system('git add count_youtube.py hololive_members.csv')
time=datetime.date.today()
time=time.strftime('%y-%m-%d')
commit='git commit -m' + ' ' + time
os.system(commit)
os.system('git push origin y2')

