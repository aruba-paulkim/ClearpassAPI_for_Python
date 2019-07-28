# pip install requests
# -*- coding: utf-8 -*-
import requests, json, base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CPPM_HOST="https://{CLEARPASS URL}"
CPPM_ID="YOUR_CPPM_ID"
CPPM_PW="YOUR_CPPM_PW"

"""
# 1. COA list
MAC = "587F57608C76"
API_QUERY = "/async_netd/cmdctrl/query"
payload = {"content": {"mac_address": MAC}, "id": 1, "name": "cnc_query_request"}
headers = {'Content-Type':'application/json', 'Authorization': 'Basic '+base64.b64encode(CPPM_ID+':'+CPPM_PW)}
try:
	r = requests.post(CPPM_HOST+API_QUERY, headers=headers, json=payload, verify=False)
	print r.status_code
	json_response = json.loads(r.text)
	print json_response
except Exception as e:
	print(e)
	exit(1)
"""



# 2. COA request
"""
MAC = "587F57608C76"
API_REQUEST = "/async_netd/cmdctrl/request"
payload = {"id": 1, "name": "cnc_request", "content": {"mac_address": MAC, "cnc_actions" : [{"id" : 1, "name" : "Terminate-Session-Aruba", "display_name" : "Terminate Session by API", "type" : "RADIUS", "params" : [{"name": "Calling-Station-Id", "value":MAC}] }] } }
headers = {'Content-Type':'application/json', 'Authorization': 'Basic '+base64.b64encode(CPPM_ID+':'+CPPM_PW)}
try:
	r = requests.post(CPPM_HOST+API_REQUEST, headers=headers, json=payload, verify=False)
	print r.status_code
	json_response = json.loads(r.text)
	print json_response
except Exception as e:
	print(e)
	exit(1)
"""



# 3. COA request
#MACs = ["587F57608C76", "00259C042DCF"]
MACs = ["587F57608C76"]

# Query - No supported actions
API_REQUEST_MULTI = "/async_netd/cmdctrl/apply_coaprof_clntlist"
payload = {"id": 1, "name": "apply_coaprof_clntlist_request", "content": {"macaddr_list" : MACs, "enf_profile_name" : "[Aruba Terminate Session]" } }
headers = {'Content-Type':'application/json', 'Authorization': 'Basic '+base64.b64encode(CPPM_ID+':'+CPPM_PW)}
try:
	r = requests.post(CPPM_HOST+API_REQUEST_MULTI, headers=headers, json=payload, verify=False)
	#r.raise_for_status()
	print r.status_code
	json_response = json.loads(r.text)
	print json_response
except Exception as e:
	print(e)
	exit(1)


"""
for MAC in MACs:
	API_REQUEST = "/async_netd/cmdctrl/request"
	payload = {"id": 1, "name": "cnc_request", "content": {"mac_address": MAC, "cnc_actions" : [{"id" : 1, "name" : "Terminate-Session-Aruba", "display_name" : "Terminate Session by API", "type" : "RADIUS", "params" : [{"name": "Calling-Station-Id", "value":MAC}] }] } }
	headers = {'Content-Type':'application/json', 'Authorization': 'Basic '+base64.b64encode(CPPM_ID+':'+CPPM_PW)}
	try:
		r = requests.post(CPPM_HOST+API_REQUEST, headers=headers, json=payload, verify=False)
		print r.status_code
		json_response = json.loads(r.text)
		print json_response
	except Exception as e:
		print(e)
		exit(1)
"""











