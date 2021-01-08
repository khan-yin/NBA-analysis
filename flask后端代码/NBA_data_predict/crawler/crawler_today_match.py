import requests
import datetime
from DB import conn_db
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle

url='https://matchweb.sports.qq.com/kbs/list'
headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / '
                        '87.0.4270.0Safari / 537.36 '
    }
params={
    'from': 'NBA_PC',
    'columnId': '100000',
    'startTime': '2020-12-28',
    'endTime': '2021-01-03',
    'from': 'sporthp'
    }


def crawl_today_match():

    db_data = conn_db.get_team_ability()

    today = datetime.date.today()
    formatted_today = today.strftime('%Y-%m-%d')
    yesterday = today - datetime.timedelta(days=1)
    formatted_yesterday = yesterday.strftime('%Y-%m-%d')
    params['startTime'] = formatted_yesterday
    params['endTime'] = formatted_yesterday

    data = requests.get(url=url, headers=headers, params=params).json()['data'][formatted_yesterday]
    s = set()  # 昨天比赛过的球队集合
    for t in data:
        if t['matchType'] == '2':
            s.add(t['leftName'].encode("utf-8").decode("utf-8"))
            s.add(t['rightName'].encode("utf-8").decode("utf-8"))

    params['startTime'] = formatted_today
    params['endTime'] = formatted_today
    data = requests.get(url=url, headers=headers, params=params).json()['data'][formatted_today]
    list = []  # 当天所有比赛集合
    for t in data:
        if t['matchType'] == '2':
            newData = {}
            newData['time'] = t['startTime']
            leftName = t['leftName'].encode("utf-8").decode("utf-8")
            newData['team1'] = leftName
            if leftName in s:
                newData['team1Tired'] = '1'
            else:
                newData['team1Tired'] = '0'
            rightName = t['rightName'].encode("utf-8").decode("utf-8")
            newData['team2'] = rightName
            if rightName in s:
                newData['team2Tired'] = '1'
            else:
                newData['team2Tired'] = '0'
            newData['teamLogo1'] = t['leftBadge']
            newData['teamLogo2'] = t['rightBadge']
            leftGoal = int(t['leftGoal'])
            rightGoal = int(t['rightGoal'])
            newData['predictResult'] = '-'

            newData['team1Ability'] = format(db_data[leftName], '.5f')
            newData['team2Ability'] = format(db_data[rightName], '.5f')
            if t['ifHasPlayback'] == '0':
                newData['trueResult'] = '-'
            else:
                if leftGoal > rightGoal:
                    newData['trueResult'] = '1'
                else:
                    newData['trueResult'] = '0'
            list.append(newData)

    mypred = pd.DataFrame(columns=['team1_tired', 'team2_tired', 'team1_ability', 'team2_ability'])
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    for dic in list:
        new = pd.DataFrame({'team1_tired': dic["team1Tired"],
                            'team2_tired': dic["team2Tired"],
                            'team1_ability': dic['team1Ability'],
                            'team2_ability': dic['team2Ability']}, index=[1])  # 自定义索引为：1 ，这里也可以不设置index
        y_pred = model.predict(new)
        # print(type(y_pred))
        # print(y_pred[0])
        dic['predictResult'] = str(y_pred[0])
        # print(dic['predictResult'] == dic['trueResult'])

    # print(list)
    return {
        'list': list
    }


if __name__ == '__main__':
    crawl_today_match()