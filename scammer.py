# -------hoshmand------- make that scammer cry :v 
import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'scammer url paste between these single quote'

names = json.loads(open('randomname.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		# open scammer site and go to ispect and click on network after that login with the random username and password like type username for username and password for password then it should give you something like this 'auid2yjauysd2uasdasdasd': username,	'kjauysd6sAJSDhyui2yasd': password but dont forget to add ' ' 
	})

	print 'sending username %s and password %s' % (username, password)
