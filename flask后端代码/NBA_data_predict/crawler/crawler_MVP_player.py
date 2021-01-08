import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
url = 'https://ziliaoku.sports.qq.com/cube/index'

params1 = {
    'cubeId': '8',
    'dimId': '5',
    'params': 't1:3704',
    'from': 'sportsdatabase'
}
params2={
    'cubeId': '1',
    'dimId': '1',
    'params': 't1:13',
    'from': 'sportsdatabase'
}
params3={
    'cubeId': '10',
    'dimId':'9,10',
    'params': 't2:2019|t3:1|t1:3704',
    'from': 'sportsdatabase'
}


def crawl_MVP_player():
    dataPlayer = requests.get(url=url, params=params1, headers=headers).json()['data']['playerBaseInfo']
    dataTeam = requests.get(url=url, params=params2, headers=headers).json()['data']['baseInfo']
    dataData = requests.get(url=url, params=params3, headers=headers).json()['data']
    dataDataMax = dataData['nbaPlayerLeagueSeasonStat']
    dataDataP = dataData['nbaPlayerSeasonStat']
    info = {}

    info['avatarUrl'] = dataPlayer['picFromSIB']
    info['playerName'] = dataPlayer['cnName']
    info['record'] = dataDataP['pointsPG'] + '分 | ' + dataDataP['reboundsPG'] + '篮板 | ' + dataDataP['assistsPG'] + '助攻'
    info['teamLogo'] = dataTeam['logoBlack']
    info['number'] = '# ' + dataPlayer['jerseyNum']
    info['role'] = dataPlayer['position']
    info['height'] = dataPlayer['height']
    info['weight'] = dataPlayer['weight']
    info['birthday'] = dataPlayer['birthDate']
    info['teamName'] = dataTeam['cnName']
    info['firstYear'] = dataPlayer['draftYear']
    info['playerRadar'] = []
    defen = {}
    defen['name'] = '场均得分'
    defen['value'] = dataDataP['pointsPG']
    defen['max'] = dataDataMax['pointsLeagueMax']
    info['playerRadar'].append(defen)

    gaimao = {}
    gaimao['name'] = '场均盖帽'
    gaimao['value'] = dataDataP['blocksPG']
    gaimao['max'] = dataDataMax['blockedLeagueMax']
    info['playerRadar'].append(gaimao)

    qiangduan = {}
    qiangduan['name'] = '场均抢断'
    qiangduan['value'] = dataDataP['stealsPG']
    qiangduan['max'] = dataDataMax['stealsLeagueMax']
    info['playerRadar'].append(qiangduan)

    lanban = {}
    lanban['name'] = '场均篮板'
    lanban['value'] = dataDataP['reboundsPG']
    lanban['max'] = dataDataMax['reboundsLeagueMax']
    info['playerRadar'].append(lanban)

    zhugong = {}
    zhugong['name'] = '场均助攻'
    zhugong['value'] = dataDataP['assistsPG']
    zhugong['max'] = dataDataMax['assistsLeagueMax']
    info['playerRadar'].append(zhugong)
    # print(info)
    res = {
        'MVP_player': info
    }
    return res


if __name__ == '__main__':
    crawl_MVP_player()