import os
from riot_client import Riot
RIOT_KEY = os.getenv('RIOT_API_KEY')
client = Riot(RIOT_KEY)


PLATFORM_ID = {'lan':'LA1', 'las':' LA2', 'br':'BR1',
				'eune':'EUN1', 'euw' : 'EUW1', 'jp':'JP1',
				'tr':'TR1', 'ru':'RU', 'oce':'OC1',
				'na':'NA1', 'kr':'KR' }

#Return a list contaning the free-week champions
def free_week(a_client):
	ids = []
	champ = []
	champions = a_client.get('api/lol/na/v1.2/champion')
	try:
		for i in champions['champions']:
			if i['freeToPlay'] is True:
				ids.append(i['id'])

		for i in ids:
			champ.append(a_client.get('api/lol/static-data/na/v1.2/champion/',i)['name'])
		return champ
	except:
		return -1

def mastery_level(champ,region,summoner,a_client):
	region = region.lower()
	champ = champ.lower().title()
	summoner = summoner.lower()
	region_id = PLATFORM_ID[region]
	try:
		player_id = client.get('/api/lol/lan/v1.4/summoner/by-name',summoner)[summoner]['id']
		champion_id = client.get('api/lol/static-data',region,'/v1.2/champion/')['data'][champ]['id']
		returned_value = a_client.get('championmastery/location',region_id,'/player',player_id,'/champion',champion_id)
		return returned_value
	except:
		return -1
