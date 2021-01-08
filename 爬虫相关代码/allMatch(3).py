import requests
import time
import csv
from time import sleep
headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
       'Safari/537.36 '
}
url='https://nba.hupu.com/api/v3/match'
params={
    'nba': '1'
}
date1=1570118400
gap=86400
date2=1602518400
date3=1586620800
newFile = open('allMatches.csv', 'w')
newWriter = csv.writer(newFile, lineterminator='\n')
newWriter.writerow(['日期','主队','客队','主队得分','客队得分'])

for i in range(date1,date3,gap):
    date=str(i)+'000'
    params['date']=date
    matchList=requests.get(url=url,headers=headers,params=params).json()['data']['today']['list']
    for temp in matchList:
        beginTime = temp['beginTime']/1000
        timeArray=time.localtime(beginTime)
        otherStyleTime=time.strftime("%Y-%m-%d", timeArray)
        print(otherStyleTime)
        matchData = temp['matchData']
        homeName=matchData[0]['name']
        homeGoal=matchData[0]['rate']
        awayName=matchData[1]['name']
        awayGoal=matchData[1]['rate']
        newWriter.writerow([otherStyleTime,homeName,awayName,homeGoal,awayGoal])
    sleep(3)
newFile.close()

