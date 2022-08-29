from operator import index
from urllib import response
import requests
import json
url="https://jsonplaceholder.typicode.com/posts"
data=requests.get(url)
convert=data.json()
index=0
for i in convert:
    print(index+1,i["title"],i["id"])
    index+=1
