import requests
import json
import pprint
class ListCoin(object):
	def __init__(self, *args, **kwargs):
		self.endpoint = 'https://api.coinpaprika.com/v1/'

	def get_list(self):
		response = requests.get(self.endpoint + 'coins')
		if response.status_code == 200:
			coins = json.loads(response.text)
			return coins
		return None

class RetrieveCoin(object):

	def __init__(self, coin_id, *args, **kwargs):
		self.coin_id = coin_id
		self.endpoint = 'https://api.coinpaprika.com/v1/'
		self.get_object()

	def get_object(self, *args, **kwargs):
		response = requests.get('{endpoint}/coins/{coin_id}'.format(endpoint=self.endpoint, coin_id=self.coin_id))
		if response.status_code == 200:
			coin = json.loads(response.text)
			self.coin = coin
		

coin = RetrieveCoin()
pprint.pprint(coin.get_object(coin_id='btc-bitcoin'))
