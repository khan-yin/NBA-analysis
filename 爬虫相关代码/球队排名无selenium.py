import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
url = 'https://matchweb.sports.qq.com/rank/team'
params = {
    'from': 'sporthp',
    'competitionId': '100000',
    'from': 'NBA_PC'    
}
reqData = requests.get(url=url, params=params, headers=headers).json()[1]
rankListEast=[]
rankListWest=[]
eastData=reqData['east']
westData=reqData['west']
for i in range(0,15):
    data1=eastData[i]
    data2=eastData[i]
    newData1={}
    newData2={}
    if i < 9:
        newData1['rank']='0'+str(i+1)
        newData2['rank']='0'+str(i+1)
    else:
        newData1['rank']=str(i+1)
        newData2['rank']=str(i+1)
    newData1['teamName']=data1['name'].encode("utf-8").decode("utf-8")
    newData2['teamName']=data2['name'].encode("utf-8").decode("utf-8")
    newData1['teamLogo']=data1['badge']
    newData2['teamLogo']=data2['badge']
    newData1['win']=data1['wins']
    newData2['win']=data2['wins']
    newData1['lose']=data1['losses']
    newData2['lose']=data2['losses']
    newData1['winDiffer']=data1['games-back']
    newData2['winDiffer']=data2['games-back']
    newData1['winRate']=data1['wining-percentage']+'%'
    newData2['winRate']=data2['wining-percentage']+'%'
    newData1['homeCourt']=data1['homeWins']+'-'+data1['homeLosses']
    newData2['homeCourt']=data2['homeWins']+'-'+data2['homeLosses']
    newData1['groundCourt']=data1['awayWins']+'-'+data1['awayLosses']
    newData2['groundCourt']=data2['awayWins']+'-'+data2['awayLosses']
    newData1['area']=data1['conferenceWins']+'-'+data1['conferenceLosses']
    newData2['area']=data2['conferenceWins']+'-'+data2['conferenceLosses']
    newData1['winScore']=data1['points']
    newData2['winScore']=data2['points']
    newData1['losePoint']=data1['lossPoints']
    newData2['losePoint']=data2['lossPoints']
    newData1['netVictory']=data1['pointsDifference']
    newData2['netVictory']=data2['pointsDifference']
    streak1=int(data1['streak'])
    if streak1>0:
        newData1['winStreak']=str(streak1)+'连胜'
    else:
        newData1['winStreak']=str(-1*streak1)+'连负'
    streak2=int(data2['streak'])
    if streak2>0:
        newData2['winStreak']=str(streak2)+'连胜'
    else:
        newData2['winStreak']=str(-1*streak2)+'连负'
    rankListEast.append(newData1)
    rankListWest.append(newData2)
print(rankListEast)
print(rankListWest)