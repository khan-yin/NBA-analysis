import requests
def func(category):#categoryȡֵ['after','normal','before']
   
    url='https://ziliaoku.sports.qq.com/cube/index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                      'Safari/537.36 '
    }
    params = {
        'cubeId': '10',
	    'dimId': '23',		
	    'from': 'sportsdatabase',
        'params':'t1:3704'
    }
    
    nbaPlayerCareer=requests.get(url=url,headers=headers,params=params).json()['data']['nbaPlayerCareer']
    info={}
    time=[]
    penaltyShot=[]
    scoreHit=[]
    threeHit=[]
    backBorad=[]
    getScore=[]
    assists=[]
    shotBlock=[]
    snatch=[]
    foul=[]
    flag=''
    if category=='before':
        flag='0';
    elif category=='normal':
        flag='1';
    else:
        flag='2';
    for temp in nbaPlayerCareer:
        if flag==temp['seasonType']:
            season=int(temp['seasonId'])-2000
            time.append(str(season)+'-'+str(season+1))
            penaltyShot.append(str(round(float(temp['ftPCT'])*100,1)))
            scoreHit.append(str(round(float(temp['fgPCT'])*100,1)))
            threeHit.append(str(round(float(temp['threesPCT'])*100,1)))
            backBorad.append(temp['reboundsPG'])
            getScore.append(temp['pointsPG'])
            assists.append(temp['assistsPG'])
            shotBlock.append(temp['blocksPG'])
            snatch.append(temp['stealsPG'])
            foul.append(temp['foulsPG'])
    info['time']=time
    info['penaltyShot']=penaltyShot
    info['scoreHit']=scoreHit
    info['threeHit']=threeHit
    info['backBorad']=backBorad
    info['getScore']=getScore
    info['assists']=assists
    info['shotBlock']=shotBlock
    info['snatch']=snatch
    info['foul']=foul
    return info
print(func('normal'))