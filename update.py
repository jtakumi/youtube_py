from googleapiclient.discovery import build
import csv,json,datetime,os
from read_files import ReadFiles
from os import listdir

class Update:

    """
    this is program which is update vtuber groups data.
    """
    def subscriber(self):
        pass

    def videocount(self):
        pass

    def makedata(self,fdn):
        td = datetime.datetime.today()
        tdr = td.strftime("%Y-%m-%d")
        operate = "mkdir " + fdn + tdr
        os.system(operate)

    def load_id(self,path):
        try:
            with open(path,'r',encoding='utf-8') as f:
                filedata = json.load(f)
        except Exception as e:
            print(path)
            print(e)
        else:
            id = filedata['id']
            return id
        
    def read_data(self,path,data,wana_get):
        try:
            with open(path,'r',encoding='utf-8') as f:
                filedata = json.load(f)
        except Exception as e:
            print(path)
            print(e)
        else:
            for h in range(2):
                for i in range(3):
                    data.append(filedata[wana_get[h,0]][wana_get[h,i+1]])
            

    def doit(self):
        data =list()
        wana_get=[['snippet','title','publishedAt','country'],['statitics','subscriberCount','videoCount','viewCount']]
        rf = ReadFiles()
        fdn = rf.dat_read_file('foldername','foldername.dat')
        self.makedata(fdn)
        self.read_data(fdn,data,wana_get)

if __name__ == '__main__':
    upd = Update()
    upd.doit()