import requests
import json
import os
import random
import time
"""head = {
	'x-ig-app-id':'936619743392459',
	'cookie': 'dpr=1.25; ig_did=9C216138-00F4-4021-9EC0-A0C537183235; datr=Hl8pZPTptmf47NhngemoFqAs; ig_nrcb=1; mid=ZClfIAALAAEBQ54Gf3apK_fd9c4D; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=53152873087; sessionid=53152873087:WxZmDXAI0KaAFo:18:AYdo4lXT9SNzcTJB6o0BD9T3pg-h9hunggU90rh8FQ; csrftoken=WkZg0pqQOcKgdGvFHI9Yb8pKZn4p1OWC; fbsr_124024574287414=zX9qomVMERCKM_j73nu9RQjYtim17WYoynKpsseLCLM.eyJ1c2VyX2lkIjoiMTAwMDgwNTA0ODQ3MzM4IiwiY29kZSI6IkFRQVU1MEVWeE1ZTFktV3EzTGFfZzJES0VCUmx5VkNmUWg4RnVHWkc2dmZIMFpUUVJ1Mmc0VkE3VGM3YWRyejQ1bWJKdi1wS2VfbGI2SlJIUG9ub1dFRXVISXhwZDN1YVVvVC1OTWM4QlBrbjdwTlhUSnIyZXNpcjlZMWhlU1V2WnhhZUF6ZVpwdnBqTXFya3k2T3E2QlloZE9lY1c4alV6RzB5T0N1STJ3WXVRaDF2RHl6TFZTWTNtVkFIbW9Cb3NOYmNmd1UyUTYyX0xjcDRRZlQ1RTVTWF9CcXoxcy00SDVadmU0a0ZkTXpGMFhvUGtpMVJ3X1ZNcHI3NXpLS3B0dkVyOXlpSzEtX25nWnZfM3NmYVdoWm9qQThTR1pTTlE2NVVLc3YydHlCZXRZWkdzYjQ2REFPcUZORWstcHVnVWEyMnpIbFFwN2VKOEkwRTg5LXVqdi1zIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUI5WkFpZDNtcEZlb0FDdU9tSDIwRWdrQ25qcktidmVsZXNnUVREdlRZS3BqMjVjUmd3STFxdVZaQVpDQ0lpckp6SWZuelpCMGpaQTIweHJ4ZGxMNDBRWkNaQ0g5WkFMSjY0SGpaQlZNNHAxNGZmaDh2MUM4OXlpSnhXeGxRelpCVEtVVHZwcWI5SGc3eXpMbm5EY2RZOHFETDQ1R1J1NEZNam9qYkc3T1RETEZ4bGdqUGZzYzc4MW9aRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTE3NjE5fQ; rur="EAG\05453152873087\0541712053643:01f77cf861c1643388e29072443d983e44876642aeca25618707855b31a0e75a710b36aa"',
	'referer':'https://www.instagram.com/hanhyojoo222/',
	'x-ig-www-claim':'hmac.AR0Rgsa8T2FqNy2ignkezjrUCmOmMkL4TwKmMkN1QP4NU2fK',
	'x-csrftoken':'WkZg0pqQOcKgdGvFHI9Yb8pKZn4p1OWC',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
	'x-asbd-id':'198387',
	'x-requested-with':'XMLHttpRequest'
}

url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=hanhyojoo222'
next_url = 'https://www.instagram.com/api/v1/feed/user/hanhyojoo222/username/?count=12'
next_url = 'https://www.instagram.com/api/v1/feed/user/hanhyojoo222/username/?count=12&max_id=2813820258525027963_6096149550'
res = requests.get(url=url,headers=head)
print(res.status_code)
"""
if not os.path.exists('C:/Users/huang/Desktop/python/instagram_hanhyojoo222/picture'):
	os.mkdir('C:/Users/huang/Desktop/python/instagram_hanhyojoo222/picture')

html_path = 'C:/Users/huang/Desktop/python/instagram_hanhyojoo222/html_data.txt'

content = open(html_path, 'rb').read()
js_content = json.loads(content)
count = js_content['data']['user']['edge_owner_to_timeline_media']['count']
current_conut = len(js_content['data']['user']['edge_owner_to_timeline_media']['edges'])
loop = js_content['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
print(loop)
new_content = js_content['data']['user']['edge_owner_to_timeline_media']['edges']
id_user='Hanhyojoo'
for i in range(current_conut):
	for j in range(len(new_content[i]['node']['edge_sidecar_to_children']['edges'])):
		img_url = new_content[i]['node']['edge_sidecar_to_children']['edges'][j]['node']['display_url']
		with open(f'C:/Users/huang/Desktop/python/instagram_hanhyojoo222/picture/${id_user}_{i}_{j}.jpg', 'wb') as f:
			f.write(requests.get(url=img_url).content)
			f.close()
		time.sleep(random.randint(3,6))


