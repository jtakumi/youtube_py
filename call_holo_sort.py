import imp
import os
import datetime
import hololive_sort

hololive_sort.main()
add='git add hololive_sort.py ./holo_csv/hololive_videoCount_sort.csv'
os.system(add)
print('Do you want to commit?[y/n]')
dc=input()
if dc=='y':
    today=datetime.date.today()
    d1=today.strftime('%y-%m-%d')
    commit='git commit -m day:' + d1
    os.system(commit)
