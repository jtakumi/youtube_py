from googleapiclient.discovery import build
import csv,json,datetime,os
from read_files import ReadFiles
from os import listdir
from csv import writer

class Update:

    """
    this is program which is update vtuber groups data.
    """

    def make_csv(self,fdn,member):
        header = ['streamer']
        header = header + data
        for i in fdn:
            path = os.path.join(i+'_csv',i+'.csv')
            with open(path,'w',encoding='utf-8-sig') as f:
                wr = csv.writer(f,lineterminator='\n')
                wr.writerow(header)
                for j in range(len(member)):
                    print(member[j],file=f)

    def read_data(self,dirname,filename,data):
        title =publishAt = country =list()
        subscriberCount = videoCount = viewCount =list()
        data = list()
        rf = ReadFiles()
        try:            
            filedata = rf.json_input(dirname,filename)
        except Exception as e:
            print(dirname,filename)
            print(e)
        else:
            for i in filedata:
                title.append(filedata['snippet']['title'])
                publishAt.append(filedata['snippet']['publishAt'])
                country.append(filedata['snippet']['country'])
                subscriberCount.append(filedata['statistics']['subscriberCount'])
                videoCount.append(filedata['statistics']['videoCount'])
                viewCount.append(filedata['statistics']['viewCount'])
            data= zip(title,publishAt,country,subscriberCount,videoCount,viewCount)
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
        rf =ReadFiles()
        key = rf.dat_read_file('','key.dat')
        API_KEY=key
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
            member =member_id = list()

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
            self.make_csv(fdn,member)


    
        
    

    def doit(self):
        data =list()
        fdn =list()
        rf = ReadFiles()
        fdn = rf.dat_read_file_lines('foldername','foldername.dat')
        self.makedata(fdn)
        self.read_data(fdn,data)

    def test(self):
        rf = ReadFiles()
        fdn = rf.dat_read_file_lines('foldername','foldername.dat')
        key = rf.dat_read_file('','key.dat')
        API_KEY=key
        YOUTUBE_API_SERVICE_NAME='youtube'
        YOUTUBE_API_VERSION='v3'
        youtube=build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey = API_KEY)
        print('got the key')
        print(fdn)

if __name__ == '__main__':
    upd = Update()
    upd.test()