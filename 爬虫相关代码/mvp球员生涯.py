import requests
def func(catagory):#catagoryÈ¡Öµ['after','normal','before']
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
        data.append(temp['points'])
        homeGoal=int(temp['homeGoal'])
        homeName=temp['homeName']
        awayGoal=int(temp['awayGoal'])
        awayName=temp['awayName']
        if homeName=='ºþÈË':
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
