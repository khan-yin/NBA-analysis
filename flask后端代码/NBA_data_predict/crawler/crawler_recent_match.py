import requests
import datetime

url = 'https://matchweb.sports.qq.com/kbs/list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
params = {
    'from': 'NBA_PC',
    'columnId': '100000',
    'from': 'sporthp'
}


def crawl_recent_match(startTime, endTime):
    # 统计当日的比赛
    today_nums = 0

    params['startTime'] = startTime
    params['endTime'] = endTime
    data = requests.get(url=url, params=params, headers=headers).json()['data']

    info = []  # 全部赛程
    fiveInfo = []
    i = 0
    for key, val in data.items():
        for v in val:
            newData = {}
            newData['time'] = v['startTime']

            # TODO: 统计当日比赛数
            date = v['startTime'].split()[0] # 取出日期
            # print(date)
            today = datetime.datetime.now().strftime('%Y-%m-%d') # 当日的日期
            # print(today)
            if date == today:
                today_nums += 1

            newData['leftTeamLogo'] = v['leftBadge']
            newData['leftTeamName'] = v['leftName'].encode("utf-8").decode("utf-8")
            newData['leftTeamScore'] = v['leftGoal']
            newData['rightTeamLogo'] = v['rightBadge']
            newData['rightTeamName'] = v['rightName'].encode("utf-8").decode("utf-8")
            newData['rightTeamScore'] = v['rightGoal']
            livePeriod = v['livePeriod']
            matchPeriod = v['matchPeriod']

            mid = v['mid']
            mid2 = mid.split(':')[1]
            # newData['data']='https://nba.stats.qq.com/nbascore/?mid='+mid2

            if livePeriod == '0':
                newData['data'] = ''
                newData['video'] = ''
                newData['live'] = v['webUrl']
                newData['status'] = '未开始'
            elif livePeriod == '1':
                newData['data'] = 'https://nba.stats.qq.com/nbascore/?mid=' + mid2
                newData['live'] = v['webUrl']
                newData['video'] = ''
                newData['status'] = '正进行'
            else:
                newData['data'] = 'https://nba.stats.qq.com/nbascore/?mid=' + mid2
                newData['live'] = ''
                newData['video'] = v['webUrl']
                newData['status'] = '已结束'
            fiveInfo.append(newData)
            i = i + 1
            if i % 5 == 0:
                info.append(fiveInfo)
                fiveInfo = []

    # print(info)
    res = {
        'recentMatches': info,
        'today_nums': today_nums
    }
    return res


if __name__ == '__main__':
    res = crawl_recent_match('2020-12-18', '2020-12-24')