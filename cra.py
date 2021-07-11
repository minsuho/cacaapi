from datetime import date, timedelta
import requests
import xmltodict
import json



def api1(startCreateDt, endCreateDt):

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'

    params = {
        "serviceKey" : "N2TgJ8nBy9uNBRnlVVEkVsf8r1r1HUTqzufZKo+/xQcAcjEYEsCJJfCwvj85f1IkEJgD6Uk22ZTf19TijGS5MQ==",
        "pageNo" : "1",
        "numOfRows" : 10,
        "startCreateDt" : startCreateDt,
        "endCreateDt" : endCreateDt
    }

    res = requests.get(url, params=params)

    dt = xmltodict.parse(res.text)
    jo = json.dumps(dt)
    data1 = json.loads(jo)
    if data1['response']['body']['totalCount'] == "0":
        return False
    data2 = data1['response']['body']['items']['item']
    # print(data2)
    return data2

    # gubun 위치
    # defCnt 확진자
    # localOccCnt 신규 확지자
    # deathCnt 사망
    # isolClearCnt 완치


def api2(startCreateDt, endCreateDt):

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

    params = {
        "serviceKey" : "N2TgJ8nBy9uNBRnlVVEkVsf8r1r1HUTqzufZKo+/xQcAcjEYEsCJJfCwvj85f1IkEJgD6Uk22ZTf19TijGS5MQ==",
        "pageNo" : "1",
        "numOfRows" : 10,
        "startCreateDt" : startCreateDt,
        "endCreateDt" : endCreateDt
    }

    res = requests.get(url, params=params)

    dt = xmltodict.parse(res.text)
    jo = json.dumps(dt)
    data1 = json.loads(jo)
    if data1['response']['body']['totalCount'] == "0":
        return False
    data2 = data1['response']['body']['items']['item']
    # print(data2)
    return data2

    # gubun 위치
    # defCnt 확진자
    # localOccCnt 신규 확지자
    # deathCnt 사망
    # isolClearCnt 완치


def now_get1():
    now = date.today()
    now_str = now.strftime("%Y%m%d")
    # print(now_str)
    data = api1(now_str, now_str)

    if not data:
        yday = now - timedelta(days=1)
        yday_str = yday.strftime("%Y%m%d")
        data = api1(yday_str, yday_str)
        # print(data)
    return data

def now_get2():
    now = date.today()
    now_str = now.strftime("%Y%m%d")
    # print(now_str)
    data = api2(now_str, now_str)

    if not data:
        yday = now - timedelta(days=1)
        yday_str = yday.strftime("%Y%m%d")
        data = api2(yday_str, yday_str)
        # print(data)
    return data




if __name__ == '__main__':
    print(get())