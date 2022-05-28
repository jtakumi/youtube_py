import csv
from genericpath import isfile
import os
from os import listdir

dir='.\holo_csv'
for i in os.listdir(dir):
    path=os.path.join(dir,i)
    if isfile(path):
        with open(path,'a',encoding='utf-8-sig') as f:
            print(path,'open')
    else:
        dep=os.path.join(dir,i)
        for j in listdir(dep):
            dpath=os.path.join(dep,j)
            with open(dpath,'a',encoding='utf-8-sig') as df:
                print(dpath,' open')
        dep=dir