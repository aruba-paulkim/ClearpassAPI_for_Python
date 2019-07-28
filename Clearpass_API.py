# pip install requests
# -*- coding: utf-8 -*-
import requests, json

from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

API_BASE = "https://{CLEARPASS URL}/api/"
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

payload = {"grant_type": "client_credentials","client_id":CLIENT_ID,"client_secret": CLIENT_SECRET}
headers = {'Content-Type':'application/json'}
try:
	r = requests.post(API_BASE+"oauth", headers=headers, json=payload, verify=False)
	r.raise_for_status()
except Exception as e:
	print(e)
	exit(1)

json_response = json.loads(r.text)
print("1. get access token : " + json_response['token_type']+" "+json_response['access_token'])
auth = json_response['token_type']+" "+json_response['access_token']


#user_id = raw_input('Enter user_id:')
user_id = "paul"
headers = {'Content-Type':'application/json','Authorization': auth}
try:
	r = requests.get(API_BASE+"local-user/user-id/"+user_id, headers=headers, verify=False)
	r.raise_for_status()
except Exception as e:
	print(e)
	exit(1)

json_response = json.loads(r.text)
print("2. get local user ")
print(" - id : " + str(json_response['id']))
print(" - user_id : " + json_response['user_id'])
print(" - username : " + json_response['username'])
print(" - role_name : " + json_response['role_name'])
print(" - enabled : " + str(json_response['enabled']))
