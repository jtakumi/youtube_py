from googleapiclient.discovery import build
import json
import os
import datetime

"""
参考サイト
https://qiita.com/rkamikawa/items/dd1fd4c1427ece787eea
"""



#API情報
API_KEY='key'
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'
class Search_Youtube:
    def make_file(self,fn,search_word):

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


    def git(self,fn):
        #自動commit
        gad='git add ' + fn
        os.system(gad)
        


    def main(self):
        syt = Search_Youtube()
        print('please input a  keyword.')
        search_word=input()

        #search dirのjsonファイルに結果を書きこむ

        fn='search/search_' + search_word + '.json'
        syt.make_file(fn,search_word)
        syt.git(fn)


if __name__ == '__main__':
    syt = Search_Youtube()
    syt.main()