import os
import re
import requests
import json
import time
import random
ajaxhead = {
	#"referer":"https://www.pixiv.net/",
	#"cookie" :"first_visit_datetime_pc=2023-03-31+22:59:57; p_ab_id=4; p_ab_id_2=8; p_ab_d_id=423662814; yuid_b=JQhAZzI; _gcl_au=1.1.227250030.1680271207; __utma=235335808.396267000.1680271208.1680271211.1680271211.1; __utmz=235335808.1680271211.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login ever=no=1^9=p_ab_id=4=1^10=p_ab_id_2=8=1^11=lang=zh=1; privacy_policy_agreement=5; _fbp=fb.1.1680416852027.777877507; _gid=GA1.2.548170190.1680416853; PHPSESSID=64488273_y6Y14trzM8725Gz1YIViTF9SGJc3FTWK; device_token=516bae41234c2e9a6b9acf30a7eeaab6; _ga_MZ1NL4PHH0=GS1.1.1680416854.1.1.1680416876.0.0.0; c_type=30; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01GX0ADGN8JHHXFA1A0H7F730N; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; tag_view_ranking=0xsDLqCEW6~bnY9G94VGN~_9k7MDZPuI~0nfArfZSOn~Hxb2_pjbHV~9Gbahmahac~jEfylbrgQX~v5c7ZJVCc0~vx2LU80BxG; adr_id=xPOx9aXTlAeJ9W17Ym1bzbOSosfRmVytXM5JQQ0nUh5DQxTA; cto_bundle=cEEYel9ORHFFJTJCU2JyRVNWJTJGeFZQNk44RUF0VDJWQnRSTVI0VXpXbE1weDladVpmRk1hVExBOTYyWmlvNU1LUzJPeVM3SjZoaTBoVU04aWluOGRRZjIwUmtaT3UydFhPOXU1TXNYSWtxTmJmRFhvJTJGNnV1T0VrTkNwVUFMZ1NJc1JnOTRWNnRqcUtkb3I2R0dWdWdPZlNyYUdRemclM0QlM0Q; _ga_75BBYNYN9J=GS1.1.1680416851.2.1.1680417825.0.0.0; _ga=GA1.2.396267000.1680271208; __cf_bm=msrfAiOoRU5vyhQE_64978NijSi6XfACCHmqzKN3ETA-1680417866-0-AaC9qhw2M9YvFDL41Hkipxbwk1C/XJoF2RnBkDuNAIBec/Fu+EkIh/i6G27579b76j8MtOD4zkCwKNuQKJo5r2oGgvhQ3lFA+DyExLUMtMGn"
	"cookie":"first_visit_datetime_pc=2023-03-31+22%3A59%3A57; p_ab_id=4; p_ab_id_2=8; p_ab_d_id=423662814; yuid_b=JQhAZzI; _gcl_au=1.1.227250030.1680271207; __utma=235335808.396267000.1680271208.1680271211.1680271211.1; __utmz=235335808.1680271211.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login%20ever=no=1^9=p_ab_id=4=1^10=p_ab_id_2=8=1^11=lang=zh=1; privacy_policy_agreement=5; _fbp=fb.1.1680416852027.777877507; _gid=GA1.2.548170190.1680416853; device_token=516bae41234c2e9a6b9acf30a7eeaab6; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01GX0ADGN8JHHXFA1A0H7F730N; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; adr_id=xPOx9aXTlAeJ9W17Ym1bzbOSosfRmVytXM5JQQ0nUh5DQxTA; tag_view_ranking=4QveACRzn3~nIjJS15KLN~Ie2c51_4Sp~faHcYIP1U0~tgP8r-gOe_~KN7uxuR89w~5oPIfUbtd6~qkC-JF_MXY~Yw6zHqltKg~azESOjmQSV~0xsDLqCEW6~bnY9G94VGN~_9k7MDZPuI~0nfArfZSOn~Hxb2_pjbHV~9Gbahmahac~jEfylbrgQX~v5c7ZJVCc0~vx2LU80BxG; _gat_UA-1830249-3=1; _gat_gtag_UA_76252338_1=1; PHPSESSID=64488937_MVFa1cBKWJL4KeUsjKCYP7FrTbQ697HH; _ga_MZ1NL4PHH0=GS1.1.1680416854.1.1.1680418302.0.0.0; c_type=29; _ga=GA1.2.396267000.1680271208; __cf_bm=9PbmAGipEpB61m4aI2aCix56hXL_VS_oH4t1NowhHiY-1680418306-0-AQ9MMR10iQzpmw9t03chiyGVCI2etKDjgs4c42lIA1L4g+dBI+BhBviWDrpRk7nxKBsLAPHov2c485XoGyyCfk+25iq+TL1QeF6WeJb+9ljw; _ga_75BBYNYN9J=GS1.1.1680416851.2.1.1680418336.0.0.0; cto_bundle=PCBx6l85YiUyQnhKaEM4ckJSS3lwM1Q5eVNnMmw5SkFrWk1VTjdDNTV5OHRYQlV6Q3VlV3g0RlltUTlPbGxBMU9WNjRwTTBYNSUyRmYlMkZCYlluMXl4b09LTngxeDhHUlZienlqSEtuS3BCRUJyTDNhQjZ3QiUyQkFRYzY3cnlaJTJCRTlWaVRpcFhRU2EwaXdJMnY2OWZGTWhRZHFIanFCVklRJTNEJTNE",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
}
username = 'wlop'
def Url(index=0):
	artwork = []
	print("URL:",end='')	
	url = input()

	if url != '':
		url = f"https://www.pixiv.net/ajax/user/{ url }/profile/all?lang=zh"
	print(url)
	url1='https://i.pximg.net/c/360x360_70/custom-thumb/img/2023/03/27/18/02/45/106611983_p0_custom1200.jpg'
	res = requests.get(url=url,headers=ajaxhead)
	content = json.loads(res.content)["body"]["illusts"]
	for artwork_id in content:
		artwork.append(artwork_id)
	#username = json.loads(res.content)["body"]["pickup"][0]["userName"]
	data = [artwork[index:],username]
	return data



def download_img(artwork_id,username, path='C:/Users/huang/Desktop/python/pixiv/picture'):
	dhead = {
	"referer":"https://www.pixiv.net/",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
	"cookie":"first_visit_datetime_pc=2023-03-31+22%3A59%3A57; p_ab_id=4; p_ab_id_2=8; p_ab_d_id=423662814; yuid_b=JQhAZzI; _gcl_au=1.1.227250030.1680271207; __utma=235335808.396267000.1680271208.1680271211.1680271211.1; __utmz=235335808.1680271211.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login%20ever=no=1^9=p_ab_id=4=1^10=p_ab_id_2=8=1^11=lang=zh=1; privacy_policy_agreement=5; _fbp=fb.1.1680416852027.777877507; _gid=GA1.2.548170190.1680416853; device_token=516bae41234c2e9a6b9acf30a7eeaab6; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01GX0ADGN8JHHXFA1A0H7F730N; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; adr_id=xPOx9aXTlAeJ9W17Ym1bzbOSosfRmVytXM5JQQ0nUh5DQxTA; tag_view_ranking=4QveACRzn3~nIjJS15KLN~Ie2c51_4Sp~faHcYIP1U0~tgP8r-gOe_~KN7uxuR89w~5oPIfUbtd6~qkC-JF_MXY~Yw6zHqltKg~azESOjmQSV~0xsDLqCEW6~bnY9G94VGN~_9k7MDZPuI~0nfArfZSOn~Hxb2_pjbHV~9Gbahmahac~jEfylbrgQX~v5c7ZJVCc0~vx2LU80BxG; _gat_UA-1830249-3=1; _gat_gtag_UA_76252338_1=1; PHPSESSID=64488937_MVFa1cBKWJL4KeUsjKCYP7FrTbQ697HH; _ga_MZ1NL4PHH0=GS1.1.1680416854.1.1.1680418302.0.0.0; c_type=29; _ga=GA1.2.396267000.1680271208; __cf_bm=9PbmAGipEpB61m4aI2aCix56hXL_VS_oH4t1NowhHiY-1680418306-0-AQ9MMR10iQzpmw9t03chiyGVCI2etKDjgs4c42lIA1L4g+dBI+BhBviWDrpRk7nxKBsLAPHov2c485XoGyyCfk+25iq+TL1QeF6WeJb+9ljw; _ga_75BBYNYN9J=GS1.1.1680416851.2.1.1680418336.0.0.0; cto_bundle=PCBx6l85YiUyQnhKaEM4ckJSS3lwM1Q5eVNnMmw5SkFrWk1VTjdDNTV5OHRYQlV6Q3VlV3g0RlltUTlPbGxBMU9WNjRwTTBYNSUyRmYlMkZCYlluMXl4b09LTngxeDhHUlZienlqSEtuS3BCRUJyTDNhQjZ3QiUyQkFRYzY3cnlaJTJCRTlWaVRpcFhRU2EwaXdJMnY2OWZGTWhRZHFIanFCVklRJTNEJTNE",
}



	url = f"https://www.pixiv.net/artworks/{ artwork_id }"
	if not os.path.exists(path):
		os.mkdir(path)
	res = requests.get(url=url, headers=dhead)
	rcon = res.content.decode('utf-8')
	cimg = re.findall('"url":"(.*?)",',rcon)
	img = ''
	for i in cimg:
		if len(i) >= 80 and len(i) <=200:
			if artwork_id in i:
				img = i
	#print(res.content.decode('utf-8'))
	imgdate = str(img).split('/')
	date = [imgdate[i] for i in range(7,13)]
	print(date)
	number = 0
	code = 200
	while code == 200:
		#https://i.pximg.net/img-original/img/2022/09/10/00/00/24/101113298_p0.jpg
		imgurl = f"https://i.pximg.net/img-original/img/{ '/'.join(date) }/{ artwork_id }_p{ number }.jpg"
		#imgurl ='https://i.pximg.net/img-master/img/2022/01/30/21/24/37/95885026_p0_master1200.jpg'
		#imgurl = f"https://i.pximg.net/img-master/img/{ '/'.join(date) }/{ artwork_id }_p{ number }_master1200.jpg"
		print(imgurl)
		res = requests.get(url=imgurl, headers=dhead)
		code = res.status_code
		print(code)
		number += 1
		if code == 200:
			with open(f"{ path }/{ username }_{ artwork_id }_{ number }.jpg", 'wb') as f:
				f.write(res.content)
				f.close()
		time.sleep(random.randint(3,8))

data = Url()

list_id = data[0]
username = data[1]

for i in list_id:
	download_img(artwork_id=i,username=username)
