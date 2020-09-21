

# twitter bot

import requests
from bs4 import BeautifulSoup as bs
import os

# website with images
url = 'http://www.ebonyinlove.com'

# download pafe for parsing
page = requests.get(url)
soup = bs(page.text,'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for images
if not os.path.exists('xtra2'):
	os.makedirs('xtra2')

# move to new directory
os.chdir('xtra2')

# image file name variable
x = 0

# writing images
for image in image_tags:
	try:
		url = image['src']
		source = requests.get(url)
		if source.status_code == 200:
			with open('xtra2 -'+ str(x) + '.jpg','wb') as f:
				f.write(requests.get(url).content)
				f.close()
				x +=1
	except:
		pass


#--- another file for twitter bot code need twitter aoo account
'''

# twitter bot code

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# iterates over pictures of images in folder
os.chdir('xtra2')
for model_image in os.listdir('.'):
	api.update_with_media(model_image)
	time.sleep(3)  						# pauses 3 seconds

'''















