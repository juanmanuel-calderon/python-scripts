from xlpython import *
import requests
import json

@xlfunc
def YGOPrice(s, n):
	if (not s) or (not n):
		return '-'
	setVal = s + '-' + n
	url = 'http://yugiohprices.com/api/price_for_print_tag/' + setVal
	myResponse = requests.get(url)
	if(myResponse.ok):
		jData = json.loads(myResponse.text)
		if(jData['status'] == 'success'):
			if(jData['data']['price_data']['price_data']['status'] == 'success'):
				return jData['data']['price_data']['price_data']['data']['prices']['average']
		return '-'
