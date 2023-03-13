from googleapiclient.discovery import build
import csv,json,datetime,os
from read_files import ReadFiles
from os import listdir
from csv import writer

class Update:

    """
    this is program which is update vtuber groups data.
    """
    

    def make_csv(self,fdn,data):
        header = ['streamer']
        header = header + data
        for i in fdn:
            path = os.path.join(i+'_csv',i+'.csv')
            with open(path,'w',encoding='utf-8-sig') as f:
                wr = csv.writer(f,lineterminator='\n')
                wr.writerow(header)
                for j in range(len(data)):
                    print(data[j],file=f)

    def read_data(self,dirname,filename,data):
        wana_get=[['snippet','title','publishedAt','country'],['statitics','subscriberCount','videoCount','viewCount']]
        data = list()
        rf = ReadFiles()
        try:            
            filedata = rf.json_input(dirname,filename)
        except Exception as e:
            print(dirname,filename)
            print(e)
        else:
            for h in range(len(wana_get)):
                for i in range(len(wana_get[0])):
                    data.append(filedata[wana_get[h,0]][wana_get[h,i+1]])
        return data            
    
    def load_id(self,dirname,filename):
        rf = ReadFiles()
        try:
            filedata = rf.json_input(dirname,filename)
        except Exception as e:
            print(dirname,filename)
            print(e)
        else:
            id = filedata['id']
            return id

    def makedata(self,fdn):
        #API情報
        API_KEY='own_key'
        YOUTUBE_API_SERVICE_NAME='youtube'
        YOUTUBE_API_VERSION='v3'
        youtube=build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey = API_KEY)

        for i,n in enumerate(fdn):
            rf = ReadFiles()
            td = datetime.datetime.today()
            tdr = td.strftime("%Y-%m-%d")
            operate = "mkdir " + os.path.join(fdn[i] + '_update',i + tdr) 
            os.system(operate)
            member =member_id=vc=sub=pubat=ct = list()

            for j in os.listdir(fdn[n]):
                member.append(os.path.splitext(os.path.basename(j))[0])
                member_id.append(self.load_id(fdn[n],j))
                search_respose=youtube.channels().list(
                part='snippet,statistics',
                id=member_id[i]
                ).execute()
                
                for search_result in search_respose.get('item',[]):
                    if search_result['kind'] != 'youtube#channel':
                        continue
                    jout = json.dumps(search_result,indent=2,ensure_ascii=False)
                rf.json_output(fdn[n],j,jout)
            data = self.read_data()
            self.make_csv(fdn)


    
        
    def read_data(self,dirname,filename,data,wana_get):
        data = list()
        rf = ReadFiles()
        try:            
            filedata = rf.json_input(dirname,filename)
        except Exception as e:
            print(dirname,filename)
            print(e)
        else:
            for h in range(2):
                for i in range(3):
                    data.append(filedata[wana_get[h,0]][wana_get[h,i+1]])
        return data            

    def doit(self):
        data =list()
        fdn =list()
        rf = ReadFiles()
        fdn = rf.dat_read_file_lines('foldername','foldername.dat')
        self.makedata(fdn)
        self.read_data(fdn,data)

if __name__ == '__main__':
    upd = Update()
    upd.doit()