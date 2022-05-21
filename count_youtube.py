import json
import os

c=0
dir='./hololive'

for i in os.listdir(dir):
    c+=1

print("member count=",c)