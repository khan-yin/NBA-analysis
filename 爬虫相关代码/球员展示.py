import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
#球员
params1={    
'cubeId': '10',
'dimId': '53,54,55,56,57,58',
'from': 'sportsdatabase',
'limit': '5',
'params': 't2:2019|t3:1'
}
#球队
params2={    
'cubeId': '12',
'dimId': '45,46,47,49,50,51',
'from': 'sportsdatabase',
'limit': '5',
'params': 't2:2019|t3:1'
}

url = 'https://ziliaoku.sports.qq.com/cube/index'


data1 = requests.get(url=url, params=params1, headers=headers).json()['data']
data2 = requests.get(url=url, params=params2, headers=headers).json()['data']
detailUrl1=['http://nba.stats.qq.com/stats/detail/?order=defen&type=player',
          'http://nba.stats.qq.com/stats/detail/?order=lanban&type=player',
          'http://nba.stats.qq.com/stats/detail/?order=zhugong&type=player',
          'http://nba.stats.qq.com/stats/detail/?order=qiangduan&type=player',
          'http://nba.stats.qq.com/stats/detail/?order=gaimao&type=player',
          'http://nba.stats.qq.com/stats/detail/?order=shiwu&type=player']
detailUrl2=['http://nba.stats.qq.com/stats/detail/?order=defen&type=team',
            'http://nba.stats.qq.com/stats/detail/?order=lanban&type=team',
            'http://nba.stats.qq.com/stats/detail/?order=zhugong&type=team',
            'http://nba.stats.qq.com/stats/detail/?order=qiangduan&type=team',
            'http://nba.stats.qq.com/stats/detail/?order=gaimao&type=team',
            'http://nba.stats.qq.com/stats/detail/?order=shiwu&type=team']


bangdan1=['nbaPlayerSeasonPointsRank','nbaPlayerSeasonReboundsRank','nbaPlayerSeasonAssistsRank','nbaPlayerSeasonStealsRank','nbaPlayerSeasonBlocksRank','nbaPlayerSeasonTurnoversRank']
ct=['pointsPG','reboundsPG','assistsPG','stealsPG','blocksPG','turnoversPG']
bangdan2=['nbaTeamSeasonPointsTop5','nbaTeamSeasonReboundTop5','nbaTeamSeasonAssitsTop5','nbaTeamSeasonStealTop5','nbaTeamSeasonBlockTop5','nbaTeamSeasonTurnoverTop5']
categorys=['场均得分','场均篮板','场均助攻','场均抢断','场均能盖帽','场均失误']
result1={}
for i in range(0,6):
    data={}   
    playerList=[]
    t=data1[bangdan1[i]]
    for j in range(0,5):
        temp={}
        temp['num']=j+1
        temp['img']=t[j]['pic']
        temp['name']=t[j]['cnName']
        temp['score']=t[j][ct[i]]
        playerList.append(temp)
    data['category']=categorys[i]
    data['detailUrl']=detailUrl1[i]
    data['playerList']=playerList
    result1[bangdan1[i]]=data
print(result1)

result2={}
for i in range(0,6):
    data={}   
    teamList=[]
    t=data2[bangdan2[i]]
    for j in range(0,5):
        temp={}
        temp['num']=j+1
        temp['img']=t[j]['logo']
        temp['name']=t[j]['cnName']
        temp['score']=t[j][ct[i]]
        teamList.append(temp)
    data['category']=categorys[i]
    data['detailUrl']=detailUrl2[i]
    data['teamList']=teamList
    result2[bangdan2[i]]=data
print(result2)