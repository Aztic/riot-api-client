import os
from riot_client import Riot
RIOT_KEY = os.getenv('RIOT_API_KEY')
client = Riot(RIOT_KEY)


PLATFORM_ID = {'lan':'LA1', 'las':'LA2', 'br':'BR1','eune':'EUN1', 'euw' : 'EUW1', 'jp':'JP1','tr':'TR1', 'ru':'RU', 'oce':'OC1','na':'NA1', 'kr':'KR' }

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
		#client.get('api/lol',region,'v1.4/summoner/by-name',summoner)[summoner]
		player_id = _summoner_by_name(summoner,region,a_client)['id']
		champion_id = client.get('api/lol/static-data',region,'/v1.2/champion/')['data'][champ]['id']
		returned_value = a_client.get('championmastery/location',region_id,'/player',player_id,'/champion',champion_id)
		return returned_value
	except:
		return -1

def get_division(region,summoner,a_client):
	region = region.lower()
	summoner = summoner.replace(" ", "").lower()
	try:
		sum_id = str(_summoner_by_name(summoner,region,a_client)['id'])
		#dictionary of list
		information = client.get('api/lol',region,'/v2.5/league/by-summoner',sum_id)[sum_id][0]
		tier = information['tier'].lower().title()
		division = information['entries'][0]['division']
		return tier + ' ' + division
	except:
		return -1

#### SEPARATE FOR TEAM ID  #####
def game_information(region,summoner,a_client):
	ret_dict = {'100':{}, '200':{}}
	game_participants = _current_game_participants(region,summoner,a_client)
	if game_participants == -1:
		return -1
	for player in game_participants:
		teamid = str(player['teamId'])
		ret_dict[teamid][player['summonerName']] = get_division(region,player['summonerName'],a_client)
	return ret_dict



def _summoner_by_name(summoner, region, a_client):
	summoner = summoner.lower()
	region = region.lower()
	try:
		return_info = client.get('api/lol',region,'v1.4/summoner/by-name',summoner)[summoner]
		return return_info
	except:
		return -1

def _summoner_by_id(id, a_client):
	try:
		return_info = client.get('api/lol',region,'/v1.4/summoner',id)[summoner]
		return return_info
	except:
		return -1

def _current_game_participants(region,summoner,a_client):
	summoner = summoner.lower()
	region = region.lower()
	region_id = PLATFORM_ID[region]
	try:
		sum_id = str(_summoner_by_name(summoner,region,a_client)['id'])
		return_info = a_client.get('observer-mode/rest/consumer/getSpectatorGameInfo',region_id,sum_id)['participants']
		return return_info
	except:
		print("FAILED HERE!")
		return -1
