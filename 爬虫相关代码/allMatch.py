import requests
import csv
url = 'https://matchweb.sports.qq.com/kbs/list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
params = {
    'from': 'NBA_PC',
'columnId': '100000',
'startTime': '2019-10-01',
'endTime': '2020-10-13',
'from': 'sporthp'
}
data=requests.get(url=url,params=params,headers=headers).json()['data']
newFile = open('allMatches.csv', 'w')
newWriter = csv.writer(newFile, lineterminator='\n')
newWriter.writerow(['日期','主队','客队','主队得分','客队得分'])
teams=['湖人','76人','步行者','独行侠','公牛','国王','黄蜂','灰熊','活塞','火箭','掘金','爵士','开拓者','凯尔特人','快船','篮网','老鹰','雷霆','马刺','猛龙','魔术','尼克斯','奇才','骑士','热火','森林狼','太阳','鹈鹕','雄鹿','勇士']
for key, val in data.items():
    for v in val:
        if v['matchType']!='2':
            continue

        newData=[]
        newData.append(v['startTime'])
        leftName=v['leftName'].encode("utf-8").decode("utf-8")
        rightName=v['rightName'].encode("utf-8").decode("utf-8")

        if leftName not in teams or rightName not in teams:
            continue
        newData.append(v['rightName'].encode("utf-8").decode("utf-8"))
        newData.append(v['leftName'].encode("utf-8").decode("utf-8"))
        newData.append(v['rightGoal'])
        newData.append(v['leftGoal'])
        
        newWriter.writerow(newData)
newFile.close()
    