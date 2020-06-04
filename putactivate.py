import requests
import sys
sys.path.append('../lib')
from meli import Meli




headers = {
    'Content-Type': 'application/json',
}

params = (
    ('access_token', 'MY_ACCESS_TOKEN'),
)

data = '{"status":"paused"}'

response = requests.put('https://api.mercadolibre.com/items/MLM711228874', headers=headers, params=params, data=data)

print(response)



items_id = ["MLM715036437","MLM715036403"]


def active():
	meli = Meli(client_id=6586834806530948,client_secret='ml67hw3RbWcbQ6CQx3A3WXLdpf0hDyd5', access_token='APP_USR-385949866070932-051116-2a67a8e2c0732cf6d43ec2af7318a854-463010681',refresh_token='')
	# with open('playdoh3mltest.json') as file:
	# data = json.load(file)
	# for i in range(len(data)):
	# 	body=data[i]
	# 	response = meli.put("/items", body, {'access_token':meli.access_token})
	# 	print response.content


	headers = {
	    'Content-Type': 'application/json',
	}

	params = (
	    ('access_token', 'MY_ACCESS_TOKEN'),
	)

	data = '{"status":"paused"}'

	response = requests.put('https://api.mercadolibre.com/items/MLM711228874', headers=headers, params=params, data=data)

	print(response)



if __name__ == "__main__": 
    active()

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
