import requests
def func(catagory,catagoryParams):#catagory取值['after','normal','before']
    #catagoryParams取值['defen','mingzhong3','lanban','zhugong','qiangduan','gaimao','shiwu','faci']
    #['得分','三分球','篮板','助攻','抢断','盖帽','失误','罚球']
    url='https://ziliaoku.sports.qq.com/cube/index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                      'Safari/537.36 '
    }
    params = {
        'cubeId': '9',
	    'dimId': '7,8',		
	    'from': 'sportsdatabase'
    }
    if catagory=='normal':
        params['params']='t27:2019|t28:1|t1:3704'
    elif catagory=='before':
        params['params']='t27:2019|t28:0|t1:3704'
    else:
        params['params']='t27:2019|t28:2|t1:3704'
    nbaPlayerMatch=requests.get(url=url,headers=headers,params=params).json()['data']['nbaPlayerMatch']
    info={}
    time=[]
    data=[]
    result=[]
    for temp in nbaPlayerMatch:
        time.append(temp['startTime'].split()[0])
        if catagoryParams=='defen':
            data.append(temp['points'])
        elif catagoryParams=='mingzhong3':
            threePointGoals=int(temp['threePointGoals'])*100
            threePointAttempted=int(temp['threePointAttempted'])
            data.append(str(round(threePointGoals/threePointAttempted,1))+'%')
        elif catagoryParams=='lanban':
            data.append(temp['rebounds'])
        elif catagoryParams=='zhugong':
            data.append(temp['assists'])
        elif catagoryParams=='qiangduan':
            data.append(temp['steals'])
        elif catagoryParams=='gaimao':
            data.append(temp['blocked'])
        elif catagoryParams=='shiwu':
            data.append(temp['turnovers'])
        elif catagoryParams=='fangui':
            data.append(temp['turnovers'])
        elif catagoryParams=='faci':
            freeThrows=int(temp['freeThrows'])*100
            freeThrowsAttempted=int(temp['freeThrowsAttempted'])
            if freeThrows!=0:
                data.append(str(round(freeThrows/freeThrowsAttempted,1))+'%')
            else:
                data.append(str(0)+'%')#球员罚球次数可能是零，不能直接除，要先判断

        homeGoal=int(temp['homeGoal'])
        homeName=temp['homeName']
        awayGoal=int(temp['awayGoal'])
        awayName=temp['awayName']
        if homeName=='湖人':
            if homeGoal>awayGoal:
                result.append('1')
            else:
                result.append('0')
        else:
            if homeGoal>awayGoal:
                result.append('0')
            else:
                result.append('1')
    info['time']=time
    info['data']=data
    info['result']=result
    return info
print(func('normal','faci'))