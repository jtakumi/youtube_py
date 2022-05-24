import os
import hololive_graph
import datetime

hololive_graph.main()

add='git add call_hololive_graph.py hololive_graph.py'
os.system(add)

print('Do you want to commit?[y/n]')
dc=input()
if( dc=='y'):
    today=datetime.date.today()
    d1=today.strftime('%y/%m/%d')
    commit='git commit -m hololive' + d1
    os.system(commit)
    os.system('git push origin y2')
