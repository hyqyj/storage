import pytube
import requests
from urllib import (parse)
import json
#html = pytube.YouTube("https://www.youtube.com/watch?v=0-q1KafFCLU&list=RD0-q1KafFCLU")
#print(html.vid_info)

#req = requests.get(url='https://www.youtube.com/watch?v=0-q1KafFCLU')
#print(req.content)

#url = 'https://www.youtube.com/youtubei/v1/player'

#query = {
#    'videoId':'0-q1KafFCLU',
#    'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
#    'contentCheckOk': True,
#    'racyCheckOk': True
#}
#base_data = {
#    'context':{
#            'client': {
#                'clientName': 'WEB',
#                'clientVersion': '2.20200720.00.02'
#           }
#        }
#}

#endpoint_url = f'{url}?{parse.urlencode(query=query)}'

#headers = {
#    'Content-Type':'application/json'
#}
#resposen = requests.post(url=endpoint_url,headers=headers)
#print(resposen)

url = 'https://www.youtube.com/youtubei/v1/player?videoId=0-q1KafFCLU&key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&contentCheckOk=True&racyCheckOk=True'
data = b'{"context": {"client": {"clientName": "ANDROID", "clientVersion": "16.20"}}}'
head = {'User-agent': 'Mozilla/5.0', 'Accept-language': 'en-US,en', 'Content-type': 'application/json'}
response = requests.post(url=url, data=data, headers=head)
print(json.loads(response.content.decode('utf-8')))
print(response.content)