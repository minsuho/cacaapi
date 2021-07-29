from datetime import date, timedelta
from random import randint
import requests
import xmltodict
import json
import time
import lxml
from bs4 import BeautifulSoup



def api1():
    # 코로나 데이터 가져오기

    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='

    html = requests.get(url).text

    bs = BeautifulSoup(html, 'lxml')

    총확진자 = int(float(bs.select_one('#content > div > div.caseTable > div:nth-child(1) > ul > li:nth-child(1) > dl > dd').text.replace(',','')))
    확진자 = int(float(bs.select_one('#content > div > div.caseTable > div:nth-child(1) > ul > li:nth-child(2) > dl > dd > ul > li:nth-child(1) > p').text.replace('+','').replace(' ','').replace(',','')))
    총완치자 = int(float(bs.select_one('#content > div > div.caseTable > div:nth-child(2) > ul > li:nth-child(1) > dl > dd').text.replace(',','')))
    완치자 = int(float(bs.select_one('#content > div > div.caseTable > div:nth-child(2) > ul > li:nth-child(2) > dl > dd > span').text.replace('+','').replace(' ','').replace(',','')))
    총검사자 = int(float(bs.select_one('#content > div > div.data_table.mgt16.mini > table > tbody > tr > td:nth-child(8)').text.replace(',','')))
    검사자 = int(float(bs.select_one('#content > div > div:nth-child(12) > table > tbody > tr > td:nth-child(1) > span').text.replace(',','')))
    총사망자 = int(float(bs.select_one('#content > div > div.caseTable > div:nth-child(4) > ul > li:nth-child(1) > dl > dd').text.replace(',','')))
    사망자 = int(float(bs.select_one('#content > div > div.caseTable > div:nth-child(3) > ul > li:nth-child(2) > dl > dd > span').text.replace('+','').replace(' ','').replace(',','')))

    ndayca = {
        '확진자수':총확진자,
        '신규확진자수':확진자,
        '격리해제수':총완치자,
        '신규격리해제수':완치자,
        '검사진행수':총검사자,
        '신규검사진행수':검사자,
        '사망자수':총사망자,
        '신규사망자수':사망자,
    }
    
    file_path = 'cadata1.json'
    with open(file_path, 'w') as outfile:
        json.dump(ndayca, outfile, indent=4)

    return ndayca

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
    else:
        data = data1['response']['body']['items']['item']

    if not data:
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
            data = False
        else:
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
    else:
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
    print(api1())
    print(api2())