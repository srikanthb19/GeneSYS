#Python program to read exchange rates from currencylayer
#input parameters:
#api_url
#key
#filepath
#extendable: soruce currency
import requests
import json
import datetime
import os
filepath='/home/srikb881690/cur.txt'
# File Handling
if not os.path.exists(filepath):
        fh = open(filepath, 'w+')
else:
        fh = open(filepath, 'w')
#Send the request to API
resp = requests.get('http://www.apilayer.net/api/live?access_key=61ce973ce74e40090ab0c7b1f305522e')
#Exception Handling
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
#Load the data to File
data = resp.json()
cur_date=datetime.datetime.fromtimestamp(data["timestamp"]).strftime('%Y-%m-%d %H:00')
src_cur=data["source"]
for cur in data["quotes"].items():
	       fh.write(cur_date+','+src_cur+','+cur[0][3:]+','+str(cur[1])+'\n')
fh.close()
