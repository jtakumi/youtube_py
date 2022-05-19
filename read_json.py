import json
import os

#ファイル名だけを入力するとsearchフォルダからjsonファイルを取り出す
print('please enter file name.(no extention)')
fn=input()
fnp='search/search_' + fn + '.json'

with open(fnp,"r",encoding='utf-8') as f:
    jsn=json.load(f)
    #idというkeyの中のchannelIdを取り出す
    print(jsn['id']['channelId'])
   
