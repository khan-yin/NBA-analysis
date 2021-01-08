import requests

url = 'https://ziliaoku.sports.qq.com/cube/index'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}


def crawl_chart_Top10(TorP, bd):

    params = {}
    info = {}  # 结果集
    index = ''
    if bd == 'defen':
        info['name'] = '场均得分'
        params['order'] = 't70'
        index = 'pointsPG'
    elif bd == 'lanban':
        info['name'] = '场均篮板'
        params['order'] = 't71'
        index = 'reboundsPG'
    elif bd == 'zhugong':
        info['name'] = '场均助攻'
        params['order'] = 't68'
        index = 'assistsPG'
    elif bd == 'qiangduan':
        info['name'] = '场均抢断'
        params['order'] = 't72'
        index = 'stealsPG'
    elif bd == 'gaimao':
        info['name'] = '场均盖帽'
        params['order'] = 't69'
        index = 'blocksPG'
    else:
        info['name'] = '场均失误'
        params['order'] = 't74'
        index = 'turnovers'
    if TorP == 'player':
        params['cubeId'] = '10'
        params['dimId'] = '52'
        params['from'] = 'sportsdatabase'
        params['limit'] = '0,15'
        params['params'] = 't2:2019|t3:1|'
    else:
        params['cubeId'] = '12'
        params['dimId'] = '43'
        params['from'] = 'sportsdatabase'
        params['order'] = 't60'
        params['params'] = 't2:2019|t3:1|t64:west,east'
    data = requests.get(url=url, headers=headers, params=params).json()['data']
    d = []
    categories = []
    if TorP == 'team':
        nbTeamSeasonStatRank = data['nbTeamSeasonStatRank']
        for temp in nbTeamSeasonStatRank:
            if bd == 'shiwu':
                d.append(str(round(float(temp[index]) / int(temp['games']), 1)))
            else:
                d.append(temp[index])
            categories.append(temp['cnName'])
    else:
        nbaPlayerSeasonStatRank = data['nbaPlayerSeasonStatRank']
        for temp in nbaPlayerSeasonStatRank:
            if bd == 'shiwu':
                d.append(str(round(float(temp[index]) / int(temp['games']), 1)))
            else:
                d.append(temp[index])
            categories.append(temp['cnName'])
    info['categories'] = categories
    info['data'] = d
    if TorP == 'team':
        res = {
            'top10': sort(info)
        }
        return res
    else:
        res = {
            'top10': info
        }
        return res


def sort(info):
    categories = info['categories']
    data = info['data']
    length = len(data)
    for i in range(0, length):
        data[i] = float(data[i])
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if data[j] < data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                temp = categories[j]
                categories[j] = categories[j + 1]
                categories[j + 1] = temp
    for i in range(0, length):
        data[i] = str(data[i])
    info['data'] = data
    info['categories'] = categories
    return info

# if __name__ == '__main__':
#     print(crawl_chart_Top10('player', 'shiwu'))