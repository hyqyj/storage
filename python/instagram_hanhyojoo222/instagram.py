import requests
import json
import os
import random
import time

head = {
	'x-ig-app-id':'936619743392459',
	'cookie':'mid=ZIbKTwALAAHLeA_RSg6vu4xvAXde; ig_did=DC1BE3CD-A169-46E0-BAC7-D11972DE3A47; ig_nrcb=1; datr=TMqGZLKyyYue3DPbIS3jonKI; csrftoken=PvocaSkMLoFmqw0UbMl7hXaiL9auAlos; ds_user_id=55449658354; dpr=1.25; sessionid=55449658354%3AKkqAjN2gY8bcvF%3A1%3AAYcuMI5VCo_SkLrTtVUUNsqbDsB6dCDyW_UiOqyRYg; rur="NHA\05455449658354\0541721091286:01f7f48b619b3cf7ffd1b6f7bd0e233ae3afe88da56711e34e0c51083e481b4273048d1b',
	'referer':'https://www.instagram.com/hanhyojoo222/',
	'x-ig-www-claim':'hmac.AR0Rgsa8T2FqNy2ignkezjrUCmOmMkL4TwKmMkN1QP4NU2fK',
	'x-csrftoken':'WkZg0pqQOcKgdGvFHI9Yb8pKZn4p1OWC',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
	'x-asbd-id':'198387',
	'x-requested-with':'XMLHttpRequest'
}

def instagram():
	path = 'C:/Users/huang/Desktop/python/instagram_hanhyojoo222/picturstt'
	if not os.path.exists(path):
		os.mkdir(path)
	loop = True
	user = input()
	url = f'https://www.instagram.com/api/v1/feed/user/{ user }/username/?count=12'
	cache_url = url
	video = 1
	new_value = ''
	count = 1
	while loop:
		print(url)
		
		res = requests.get(url=url, headers=head)
		data = json.loads(res.content)
		next_max_id = data['next_max_id']
		loop = data['more_available']
		print(loop)
		img = data['items']
		
		for i in range(len(img)):
			current = True
			try:
				new_value = img[i]['carousel_media']
			except:
				with open (f'{ path }/{ video }.mp4', 'wb') as f:
					try:
						f.write(requests.get(url=img[i]['video_versions'][0]['url']).content)
						f.close()
						current = False
					except:
						with open (f'{ path }/{ video }.jpg', 'wb') as file:
							file.write(requests.get(url=img[i]['image_versions2']['candidates'][0]['url']).content)
							file.close()
						current = False
					video += 1

			for j in range(len(new_value)):
				if not current:
					break
				else:
					img_url = new_value[j]['image_versions2']['candidates'][0]['url']
					with open (f'{ path }/{ user }_{count}_{j}.jpg', 'wb') as f:
						f.write(requests.get(url=img_url).content)
						f.close()
						time.sleep(random.randint(1,2))
			count += 1
		url = f'{ cache_url }&max_id={next_max_id}'

instagram()

'''
							
					except:
						with open(f'{ path }/{video}.jpg', 'wb') as f:
							f.write(requests.get(url=img[i]['image_versions2'][0]['url']).content)
							f.close()
							video += 1
				except:
					with open(f'{ path }/{video}.jpg', 'wb') as f:
						f.write(requests.get(url=img[i]['image_versions2']['candidates'][0]['url']).content)
						f.close()
						video += 1
'''	