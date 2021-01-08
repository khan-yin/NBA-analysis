import requests
import datetime

url='https://matchweb.sports.qq.com/kbs/list'
headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / '
                        '87.0.4270.0Safari / 537.36 '
    }
params={
    'from': 'NBA_PC',
'columnId': '100000',
'startTime': '2020-12-28',
'endTime': '2021-01-03',
'from': 'sporthp'
    }
today=datetime.date.today()
formatted_today=today.strftime('%Y-%m-%d')
yesterday = today - datetime.timedelta(days=1)
formatted_yesterday=yesterday.strftime('%Y-%m-%d')
params['startTime']=formatted_yesterday
params['endTime']=formatted_yesterday

data=requests.get(url=url,headers=headers,params=params).json()['data'][formatted_yesterday]
s=set()#昨天比赛过的球队集合
for t in data:
    if t['matchType']=='2':
        s.add(t['leftName'].encode("utf-8").decode("utf-8"))
        s.add(t['rightName'].encode("utf-8").decode("utf-8"))

params['startTime']=formatted_today
params['endTime']=formatted_today
data=requests.get(url=url,headers=headers,params=params).json()['data'][formatted_today]
list=[] #当天所有比赛集合
for t in data:
    if t['matchType']=='2':
        newData={}
        newData['time']=t['startTime']
        leftName=t['leftName'].encode("utf-8").decode("utf-8")
        newData['team1']=leftName
        if leftName in s:
            newData['team1_tired']='1'
        else:
            newData['team1_tired']='0'
        rightName=t['rightName'].encode("utf-8").decode("utf-8")
        newData['team2']=rightName
        if rightName in s:
            newData['team2_tired']='1'
        else:
            newData['team2_tired']='0'
        newData['teamLogo1']=t['leftBadge']
        newData['teamLogo2']=t['rightBadge']
        leftGoal=int(t['leftGoal'])
        rightGoal=int(t['rightGoal'])
        newData['predictResult']='-'
        if t['ifHasPlayback']=='0':
            newData['trueResult']='-'
        else:
            if leftGoal>rightGoal:
                newData['trueResult']='1'
            else:
                newData['trueResult']='0'
        list.append(newData)
print(list)
