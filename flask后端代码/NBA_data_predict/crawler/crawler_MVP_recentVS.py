import requests
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
url = 'https://ziliaoku.sports.qq.com/cube/index'

params = {
'cubeId': '13',
'dimId': '17,24,25',
'params': 't9:13',
'from': 'sportsdatabase'
}

teamName='湖人'


def crawl_MVP_recentVS():
    data = requests.get(url=url, params=params, headers=headers).json()['data']
    post = data['nbaTeamPostMatchLimit5Api']
    pre = data['nbaTeamPreMatchLimit5Api']
    info = []
    for detailData in post:
        newData = {}
        startTime = int(detailData['startTime'])
        timeArray = time.localtime(startTime)
        newData['time'] = time.strftime("%m-%d %H:%M", timeArray)
        homeName = detailData['homeName']
        awayName = detailData['awayName']
        homeGoal = detailData['homeGoal']
        awayGoal = detailData['awayGoal']
        if teamName == homeName:
            newData['compete'] = '主场-' + awayName
        else:
            newData['compete'] = homeName + '-客场'
        newData['result'] = homeGoal + '-' + awayGoal
        info.append(newData)

    for detailData in pre:
        newData = {}
        startTime = int(detailData['startTime'])
        timeArray = time.localtime(startTime)
        newData['time'] = time.strftime("%m-%d %H:%M", timeArray)
        homeName = detailData['homeName']
        awayName = detailData['awayName']
        if teamName == homeName:
            newData['compete'] = '主场-' + awayName
        else:
            newData['compete'] = homeName + '-客场'
        newData['result'] = '—'
        info.append(newData)
    # print(info)
    res = {
        'recentVS': info
    }
    return res


if __name__ == '__main__':
    crawl_MVP_recentVS()