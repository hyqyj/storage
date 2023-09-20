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
input_witch_id = input()
url = f'https://www.youtube.com/youtubei/v1/player?videoId={input_witch_id}&key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&contentCheckOk=True&racyCheckOk=True'
data = b'{"context": {"client": {"clientName": "ANDROID", "clientVersion": "16.20"}}}'
head = {'User-agent': 'Mozilla/5.0', 'Accept-language': 'en-US,en', 'Content-type': 'application/json'}
response = requests.post(url=url, data=data, headers=head)
responseContext = json.loads(response.content.decode('utf-8'))
streamingData = responseContext["streamingData"]
#print(streamingData)
formats = streamingData["formats"]
data_len = len(formats)
cache = 0
itag = 0
print(data_len)
for i in range(data_len):
    if formats[i]["itag"] > itag:
        itag = formats[i]["itag"]
        cache = i

print('itag = '+str(itag), 'position = '+str(cache))
url = formats[cache]["url"]

with open(f"C:/Users/huang/Desktop/python/youtube/iu_video/{input_witch_id}.mp4", "wb") as file:
    reponse = requests.get(url=url, stream=True)
    for i in reponse.iter_content(1024):
        print(i)
        if i:
            file.write(i)
    file.close()
    
