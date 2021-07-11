from datetime import date, timedelta
from random import randint
import requests
import xmltodict
import json
import time


def api1():
    # 오늘 코로나 데이터 가져오기
    now = date.today()
    now_str = now.strftime("%Y%m%d")

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

    params = {
        "serviceKey" : "zD0l/q+zOqlqv7br6BYklo1jxWZqyzg3BO1lS/p7loirhUlVFFGXt299tnoRFi78ThzPQP4qTZOKPMTmQwst3A==",
        "pageNo" : "1",
        "numOfRows" : 10,
        "startCreateDt" : now_str,
        "endCreateDt" : now_str
    }

    res = requests.get(url, params=params)

    dt = xmltodict.parse(res.text)
    jo = json.dumps(dt)
    data1 = json.loads(jo)
    if data1['response']['body']['totalCount'] == "0":
        data = False
    data = data1['response']['body']['items']['item']

    if not data:
        yday = now - timedelta(days=1)
        yday_str = yday.strftime("%Y%m%d")

        url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

        params = {
            "serviceKey" : "zD0l/q+zOqlqv7br6BYklo1jxWZqyzg3BO1lS/p7loirhUlVFFGXt299tnoRFi78ThzPQP4qTZOKPMTmQwst3A==",
            "pageNo" : "1",
            "numOfRows" : 10,
            "startCreateDt" : now_str,
            "endCreateDt" : now_str
        }

        res = requests.get(url, params=params)

        dt = xmltodict.parse(res.text)
        jo = json.dumps(dt)
        data1 = json.loads(jo)
        if data1['response']['body']['totalCount'] == "0":
            data = False
        data = data1['response']['body']['items']['item']

    # 어제 코로나 데이터 가져오기
    yday = now - timedelta(days=1)
    yday_str = yday.strftime("%Y%m%d")

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

    params = {
        "serviceKey" : "zD0l/q+zOqlqv7br6BYklo1jxWZqyzg3BO1lS/p7loirhUlVFFGXt299tnoRFi78ThzPQP4qTZOKPMTmQwst3A==",
        "pageNo" : "1",
        "numOfRows" : 10,
        "startCreateDt" : yday_str,
        "endCreateDt" : yday_str
    }

    res = requests.get(url, params=params)

    dt = xmltodict.parse(res.text)
    jo = json.dumps(dt)
    data1 = json.loads(jo)
    if data1['response']['body']['totalCount'] == "0":
        data2 = False
    data2 = data1['response']['body']['items']['item']

    #어제,오늘 데이터 가공
    ndayca1 = {
        '확진자수':data['decideCnt'],
        '격리해제수':data['clearCnt'],
        '검사진행수':data['examCnt'],
        '사망자수':data['deathCnt'],
    }
    ydayca = {
        '확진자수':data2['decideCnt'],
        '격리해제수':data2['clearCnt'],
        '검사진행수':data2['examCnt'],
        '사망자수':data2['deathCnt'],
    }

    ndayca = {
        '확진자수':data['decideCnt'],
        '신규확진자수':int(ndayca1['확진자수']) - int(ydayca['확진자수']),
        '격리해제수':data['clearCnt'],
        '신규격리해제수':int(ndayca1['격리해제수']) - int(ydayca['격리해제수']),
        '검사진행수':data['examCnt'],
        '신규검사진행수':int(ndayca1['검사진행수']) - int(ydayca['검사진행수']),
        '사망자수':data['deathCnt'],
        '신규사망자수':int(ndayca1['사망자수']) - int(ydayca['사망자수']),
    }
    
    file_path = 'cadata1.json'
    with open(file_path, 'w') as outfile:
        json.dump(ndayca, outfile, indent=4)

def api2():
    # 오늘 코로나 데이터 가져오기
    now = date.today()
    now_str = now.strftime("%Y%m%d")

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'

    params = {
        "serviceKey" : "zD0l/q+zOqlqv7br6BYklo1jxWZqyzg3BO1lS/p7loirhUlVFFGXt299tnoRFi78ThzPQP4qTZOKPMTmQwst3A==",
        "pageNo" : "1",
        "numOfRows" : 10,
        "startCreateDt" : now_str,
        "endCreateDt" : now_str
    }

    res = requests.get(url, params=params)

    dt = xmltodict.parse(res.text)
    jo = json.dumps(dt)
    data1 = json.loads(jo)
    if data1['response']['body']['totalCount'] == "0":
        data = False
    data = data1['response']['body']['items']['item']

    if not data:
        yday = now - timedelta(days=1)
        yday_str = yday.strftime("%Y%m%d")

        url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'

        params = {
            "serviceKey" : "zD0l/q+zOqlqv7br6BYklo1jxWZqyzg3BO1lS/p7loirhUlVFFGXt299tnoRFi78ThzPQP4qTZOKPMTmQwst3A==",
            "pageNo" : "1",
            "numOfRows" : 10,
            "startCreateDt" : now_str,
            "endCreateDt" : now_str
        }

        res = requests.get(url, params=params)

        dt = xmltodict.parse(res.text)
        jo = json.dumps(dt)
        data1 = json.loads(jo)
        if data1['response']['body']['totalCount'] == "0":
            data = False
        data = data1['response']['body']['items']['item']

    # 어제 코로나 데이터 가져오기
    yday = now - timedelta(days=1)
    yday_str = yday.strftime("%Y%m%d")

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'

    params = {
        "serviceKey" : "zD0l/q+zOqlqv7br6BYklo1jxWZqyzg3BO1lS/p7loirhUlVFFGXt299tnoRFi78ThzPQP4qTZOKPMTmQwst3A==",
        "pageNo" : "1",
        "numOfRows" : 10,
        "startCreateDt" : yday_str,
        "endCreateDt" : yday_str
    }

    res = requests.get(url, params=params)

    dt = xmltodict.parse(res.text)
    jo = json.dumps(dt)
    data1 = json.loads(jo)
    if data1['response']['body']['totalCount'] == "0":
        data2 = False
    data2 = data1['response']['body']['items']['item']

    #어제,오늘 데이터 가공
    ndayca = []
    for a in range(1, 18):
        ndayca1 = {
        '확진자수':data[a]['defCnt'],
        '격리해제수':data[a]['isolClearCnt'],
        '사망자수':data[a]['deathCnt'],
        }

        ydayca = {
            '확진자수':data2[a]['defCnt'],
            '격리해제수':data2[a]['isolClearCnt'],
            '사망자수':data2[a]['deathCnt'],
        }

        ndayca.append({
            '지역':data[a]['gubun'],
            '확진자수':data[a]['defCnt'],
            '신규확진자수':int(ndayca1['확진자수']) - int(ydayca['확진자수']),
            '격리해제수':data[a]['isolClearCnt'],
            '신규격리해제수':int(ndayca1['격리해제수']) - int(ydayca['격리해제수']),
            '사망자수':data[a]['deathCnt'],
            '신규사망자수':int(ndayca1['사망자수']) - int(ydayca['사망자수']),
        })

    file_path = 'cadata2.json'
    with open(file_path, 'w') as outfile:
        json.dump(ndayca, outfile, indent=4)

    return ndayca

    
if __name__ == '__main__':
    while(1):
        api2()
        api1()
        print(1)
        time.sleep(1800)