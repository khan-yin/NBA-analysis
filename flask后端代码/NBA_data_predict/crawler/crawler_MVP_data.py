import requests

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


def crawl_MVP_data(category,categoryParams):#category取值['after','normal','before']
    #categoryParams取值['defen','mingzhong3','lanban','zhugong','qiangduan','gaimao','shiwu','faci']
    #['得分','三分球','篮板','助攻','抢断','盖帽','失误','罚球']
    if category=='normal':
        params['params']='t27:2019|t28:1|t1:3704'
    elif category=='before':
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
        if categoryParams=='defen':
            data.append(temp['points'])
        elif categoryParams=='mingzhong3':
            threePointGoals=int(temp['threePointGoals'])*100
            threePointAttempted=int(temp['threePointAttempted'])
            data.append(str(round(threePointGoals/threePointAttempted,1)))
        elif categoryParams=='lanban':
            data.append(temp['rebounds'])
        elif categoryParams=='zhugong':
            data.append(temp['assists'])
        elif categoryParams=='qiangduan':
            data.append(temp['steals'])
        elif categoryParams=='gaimao':
            data.append(temp['blocked'])
        elif categoryParams=='shiwu':
            data.append(temp['turnovers'])
        elif categoryParams=='fangui':
            data.append(temp['turnovers'])
        elif categoryParams=='faci':
            freeThrows=int(temp['freeThrows'])*100
            freeThrowsAttempted=int(temp['freeThrowsAttempted'])
            if freeThrows != 0:
                data.append(str(round(freeThrows / freeThrowsAttempted, 1)) + '%')
            else:
                data.append(str(0) + '%')  # 球员罚球次数可能是零，不能直接除，要先判断

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
    # print(info)
    res = {
        'MVP_data': info
    }
    return res


if __name__ == '__main__':
    crawl_MVP_data('normal', 'faci')