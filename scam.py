"""Send fake usernames and passwords to a scammer's phishing website.
Based off of Engineer Man's youtube video
https://www.youtube.com/watch?v=UtNYzv8gLbs
"""

import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://exclinicdigital.com/jhu/login.php'

names = json.loads(open('last_names.json').read())

for name in names:
	# make fake JHED
	name = random.choice(string.ascii_lowercase) + name[:6].lower()
	name_extra = str(random.randint(1,200))
	username = name + name_extra + '@jh.edu'

	# make fake password
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'wpName': username,
		'wpPassword': password,
		'wploginattempt': 'Log in',
		'wpEditToken': '+\\',
		'title': 'Special:UserLogin',
		'authAction': 'login',
		'force': '',
		'wpLoginToken': 'c4962199b43e7fe4295dcc0acbf6e0155ea1a65f+\\'
	})

	print('sending username %s and password %s' % (username, password))
