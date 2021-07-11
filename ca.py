import requests
import json as json2

url = 'https://www.safekorea.go.kr/idsiSFK/bbs/user/selectBbsList.do'

headers = {'Content-Type': 'application/json; charset=utf-8'}

data = {
	"bbs_searchInfo": {
		"bbs_no": "63",
		"bbs_ordr": "",
		"firstIndex": "1",
		"lastIndex": "1",
		"opCode": "",
		"pageIndex": "1",
		"pageSize": "10",
		"pageUnit": "10",
		"recordCountPerPage": "10",
		"search_amendment": "",
		"search_date_limit": "20210606",
		"search_disaster_a": "",
		"search_disaster_b": "",
		"search_end": "20210706",
		"search_key_n": "",
		"search_notice": "",
		"search_permits": "",
		"search_start": "20210606",
		"search_type_v": "",
		"search_use": "",
		"search_val_v": "",
		"use": ""
	}
}


json = requests.post(url, headers=headers, data=json2.dumps(data)).json()

pa = json['rtnResult']['pageSize']

alist = []

for a in range(1, int(pa)):

    url = 'https://www.safekorea.go.kr/idsiSFK/bbs/user/selectBbsList.do'

    headers = {'Content-Type': 'application/json; charset=utf-8'}

    data1 = {
        "bbs_searchInfo": {
            "bbs_no": "63",
            "bbs_ordr": "",
            "firstIndex": "1",
            "lastIndex": "1",
            "opCode": "",
            "pageIndex": pa,
            "pageSize": "10",
            "pageUnit": "10",
            "recordCountPerPage": "10",
            "search_amendment": "",
            "search_date_limit": "20210606",
            "search_disaster_a": "",
            "search_disaster_b": "",
            "search_end": "20210706",
            "search_key_n": "",
            "search_notice": "",
            "search_permits": "",
            "search_start": "20210606",
            "search_type_v": "",
            "search_use": "",
            "search_val_v": "",
            "use": ""
        }
    }

    

    json = requests.post(url, headers=headers, data=json2.dumps(data1)).json()

    for i in json['bbsList']:
        alist.append(i['BBS_ORDR'])

print(alist)
