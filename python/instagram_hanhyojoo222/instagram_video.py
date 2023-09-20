import requests
import json
import os
import random
import time

head = {
	'x-ig-app-id':'936619743392459',
	'cookie': 'dpr=1.25; ig_did=9C216138-00F4-4021-9EC0-A0C537183235; datr=Hl8pZPTptmf47NhngemoFqAs; ig_nrcb=1; mid=ZClfIAALAAEBQ54Gf3apK_fd9c4D; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=53152873087; sessionid=53152873087:WxZmDXAI0KaAFo:18:AYdo4lXT9SNzcTJB6o0BD9T3pg-h9hunggU90rh8FQ; csrftoken=WkZg0pqQOcKgdGvFHI9Yb8pKZn4p1OWC; fbsr_124024574287414=zX9qomVMERCKM_j73nu9RQjYtim17WYoynKpsseLCLM.eyJ1c2VyX2lkIjoiMTAwMDgwNTA0ODQ3MzM4IiwiY29kZSI6IkFRQVU1MEVWeE1ZTFktV3EzTGFfZzJES0VCUmx5VkNmUWg4RnVHWkc2dmZIMFpUUVJ1Mmc0VkE3VGM3YWRyejQ1bWJKdi1wS2VfbGI2SlJIUG9ub1dFRXVISXhwZDN1YVVvVC1OTWM4QlBrbjdwTlhUSnIyZXNpcjlZMWhlU1V2WnhhZUF6ZVpwdnBqTXFya3k2T3E2QlloZE9lY1c4alV6RzB5T0N1STJ3WXVRaDF2RHl6TFZTWTNtVkFIbW9Cb3NOYmNmd1UyUTYyX0xjcDRRZlQ1RTVTWF9CcXoxcy00SDVadmU0a0ZkTXpGMFhvUGtpMVJ3X1ZNcHI3NXpLS3B0dkVyOXlpSzEtX25nWnZfM3NmYVdoWm9qQThTR1pTTlE2NVVLc3YydHlCZXRZWkdzYjQ2REFPcUZORWstcHVnVWEyMnpIbFFwN2VKOEkwRTg5LXVqdi1zIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUI5WkFpZDNtcEZlb0FDdU9tSDIwRWdrQ25qcktidmVsZXNnUVREdlRZS3BqMjVjUmd3STFxdVZaQVpDQ0lpckp6SWZuelpCMGpaQTIweHJ4ZGxMNDBRWkNaQ0g5WkFMSjY0SGpaQlZNNHAxNGZmaDh2MUM4OXlpSnhXeGxRelpCVEtVVHZwcWI5SGc3eXpMbm5EY2RZOHFETDQ1R1J1NEZNam9qYkc3T1RETEZ4bGdqUGZzYzc4MW9aRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTE3NjE5fQ; rur="EAG\05453152873087\0541712053643:01f77cf861c1643388e29072443d983e44876642aeca25618707855b31a0e75a710b36aa"',
	'referer':'https://www.instagram.com/hanhyojoo222/',
	'x-ig-www-claim':'hmac.AR0Rgsa8T2FqNy2ignkezjrUCmOmMkL4TwKmMkN1QP4NU2fK',
	'x-csrftoken':'WkZg0pqQOcKgdGvFHI9Yb8pKZn4p1OWC',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
	'x-asbd-id':'198387',
	'x-requested-with':'XMLHttpRequest',
	'content-type': 'application/x-www-form-urlencoded',
	'origin':'https://www.instagram.com'
}
data = {
	'page_size':'12',
	'target_user_id':'6096149550',
	'include_feed_video':'true'
}

#def instagram():
#	path = 'C:/Users/huang/Desktop/python/instagram_hanhyojoo222/picturs_vid'
#	if not os.path.exists(path):
#		os.mkdir(path)

	#url = 'https://www.instagram.com/api/v1/clips/user/'

	#res = requests.post(url=url,headers=head,data=data)
	#with open ('C:/Users/huang/Desktop/video.txt', 'wb') as f:
	#	f.write(res.content)
	#	f.close()

#instagram()
url = 'https://www.instagram.com/api/v1/clips/user/'
path = 'C:/Users/huang/Desktop/python/instagram_hanhyojoo222/picturs_vid/'
new_value = ''
loop = True
x = 1
while loop:
	content = requests.post(url=url, headers=head, data=data).content
	js = json.loads(content)
	try:
		max_id = js['paging_info']['max_id']
		include_feed_video = js['paging_info']['more_available']
		data['max_id']=max_id
		loop = include_feed_video
	except:
		print('over page')
	for i in range(len(js['items'])):
		video = vido = js['items'][i]['media']['video_versions'][0]['url']
		with open (f'{path}hanhyojoo_{x}_{i}.mp4', 'wb') as f:
			f.write(requests.get(url=video).content)
			f.close()
	loop = 
	x += 1

"""
content = requests.post(url=url,headers=head,data=data).content
#content = open('C:/Users/huang/Desktop/video.txt', 'rb').read()
js = json.loads(content)
vido = js['items'][0]['media']['video_versions'][0]['url']
max_id = js['paging_info']['max_id']
include_feed_video = js['paging_info']['more_available']
print(max_id , include_feed_video)
#print(vido)
data['max_id']=max_id
content = requests.post(url=url,headers=head,data=data).content
js = json.loads(content)
max_id = js['paging_info']['max_id']
include_feed_video = js['paging_info']['more_available']
print(max_id , include_feed_video)
"""