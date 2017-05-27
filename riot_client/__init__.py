import json
import urllib.parse
import urllib.request

BASE_URL = 'https://region.api.riotgames.com/'

class Riot:
	def __init__(self, riot_key=None):
		if riot_key is not None and not isinstance(riot_key, str):
			raise TypeError("riot_key must be str")
		self.riot_key = riot_key

	def get(self, *args,region=None):
		if region is None:
			raise ValueError("You must pass a valid region")
		url = resolve(region=region,*args, key=self.riot_key)
		req = urllib.request.Request(url)
		body = b''

		#resp = urllib.request.urlopen(req)
		with urllib.request.urlopen(req) as resp:
			while True:
				buf = resp.read()
				if not buf:
					break
				body += buf
		return json.loads(body.decode())

def resolve(*args, key=None,region=None):
	args = [urllib.parse.quote(str(x)) for x in args]
	temp = BASE_URL.replace('region',region)
	url = urllib.parse.urljoin(temp, '/'.join(args))
	if key != None:
		url = url + '?api_key=' + key
	return url
