import requests
import csv

import os


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 '
                  'Safari/537.36'
}
url = "https://ziliaoku.sports.qq.com/cube/index"
#常规赛

param = {
    'cubeId': '12',
    'dimId': '43',
    'from': 'sportsdatabase',
    'order': 't60',  
}
head=['球队','得分','出手数','命中率','3分出手','3分命中率','总罚球次数','罚球命中率','篮板','前场篮板','后场篮板','助攻','抢断','盖帽','总失误','犯规','场次']


if not os.path.exists('./afterAllSeason'):
    os.mkdir('./afterAllSeason')

for i in range(2014,2020):
    #param['params']='t2:'+str(i)+'|t3:1|t64:west,east' 常规赛
    #param['params']='t2:'+str(i)+'|t3:0|t64:west,east' 季前
    param['params']='t2:'+str(i)+'|t3:2|t64:west,east'
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()

    listData=list_data['data']['nbTeamSeasonStatRank']

    newFile = open('./afterAllSeason/'+str(i)+'.csv', 'w')
    newWriter = csv.writer(newFile, lineterminator='\n')
    newWriter.writerow(head)

    for data in listData:
        d=[]
        d.append(data['cnName'])
        d.append(data['pointsPG'])
        d.append(data['fgAttemptedPG'])
        d.append(data['fgPCT'])
        d.append(data['threesAttemptedPG'])
        d.append(data['threesPCT'])
        d.append(data['ftAttempted'])
        d.append(data['ftPCT'])
        d.append(data['reboundsPG'])
        d.append(data['offensiveReboundsPG'])
        d.append(data['defensiveReboundsPG'])
        d.append(data['assistsPG'])
        d.append(data['stealsPG'])
        d.append(data['blocksPG'])
        d.append(data['turnovers'])
        d.append(data['foulsPG'])
        d.append(data['games'])
        newWriter.writerow(d)
    newFile.close();
        
 
        

