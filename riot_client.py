import json
import urllib.parse
import urllib.request

#You can replace the 'na' with any region,
#it'll be the same result
BASE_URL = 'https://na.api.pvp.net/'

class Riot:
	def __init__(self, riot_key=None):
		if riot_key is not None and not isinstance(riot_key, str):
			raise TypeError("riot_key must be str")
		self.riot_key = riot_key

	def get(self, *args):
		url = resolve(*args, key=self.riot_key)
		req = urllib.request.Request(url)
		body = b''

		resp = urllib.request.urlopen(req)
		while True:
			buf = resp.read()
			if not buf:
				break
			body += buf
		return json.loads(body.decode())

def resolve(*args, key=None):
	args = [urllib.parse.quote(str(x)) for x in args]
	url = urllib.parse.urljoin(BASE_URL, '/'.join(args))
	if key != None:
		url = url + '?api_key=' + key
	return url