#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary lib
# get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
from DB import conn_db
# import seaborn as sns
import warnings
import os
# import datetime
from tqdm import tqdm
# from collections import defaultdict
# import time
import networkx as nx
from pygraph.classes.digraph import digraph
from datetime import datetime, date, timedelta
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
# from xgboost import XGBClassifier
# import torch
# import torch.nn as nn
# import torch.nn.functional as F

warnings.filterwarnings('ignore')

def out_from_sql(sql):
    conn = create_engine('mysql+mysqldb://root:whlg201898.@localhost:3306/nba?charset=utf8')
    df = pd.read_sql(sql,conn)
    return df
# In[2]:


def transform_format_match(file_path, team1, team2, date):
    data = pd.read_csv(file_path, encoding='ansi', skiprows=1)
    idx = data[data['球员'] == '球员'].index.values[0]
    data['主队/客队'] = '客队'
    data['主队/客队'].iloc[0:idx - 1] = '主队'
    data['队伍'] = team2
    data['队伍'].iloc[0:idx - 1] = team1
    data.dropna(inplace=True)
    data = data[data['球员'] != '球员']
    data['篮板'] = data['篮板'].apply(lambda x: x.split('\n')[1])
    data['助攻'] = data['助攻'].apply(lambda x: x.split('\n')[1])
    data['得分'] = data['得分'].apply(lambda x: x.split('\n')[1])
    data['投篮命中'] = data['投篮'].apply(lambda x: x.split('-')[0])
    data['投篮'] = data['投篮'].apply(lambda x: x.split('-')[1])
    data['3分命中'] = data['3分'].apply(lambda x: x.split('-')[0])
    data['3分'] = data['3分'].apply(lambda x: x.split('-')[1])
    data['罚球命中'] = data['罚球'].apply(lambda x: x.split('-')[0])
    data['罚球'] = data['罚球'].apply(lambda x: x.split('-')[1])
    data.drop(['时间', '+/-', '位置'], axis=1, inplace=True)
    num_cols = list(set(data.columns) - set(['球员', '主队/客队', '队伍']))
    data[num_cols] = data[num_cols].astype('int8')
    data = data[data['得分'] != 0]
    data['日期'] = date
    data['日期'] = pd.to_datetime(data['日期'])
    data.reset_index(drop=True, inplace=True)
    return data


# In[3]:


def get_main_player_mean_socre(all_format_team, player_name, time, team):
    player_record = all_format_team[(all_format_team['球员'] == player_name) & (all_format_team['日期'] <= time)]
    length = player_record.shape[0]
    # print(length)#长度是否>14
    if length > 14:
        return player_record.tail(14)['得分'].mean()
    else:
        return player_record['得分'].mean()


# In[4]:


def get_single_match(df, all_format_team):  # 加了个参数 all_format_team
    cols = ['日期', '主队', '客队', '主队主力', '客队主力', '主队队员', '客队队员', '主队得分', '客队得分']
    match_series = pd.Series(index=cols)
    match_series['日期'] = df['日期'][0]

    home = df[df['主队/客队'] == '主队']
    guest = df[df['主队/客队'] == '客队']

    match_series['主队'] = home['队伍'].iloc[0]
    match_series['客队'] = guest['队伍'].iloc[0]

    # all_format_team = get_all_format_team()#这个地方其实可以变成全局变量当参数传进来会更省时间
    # TODO: 重新计算每场比赛中的每个球队的主力队员  #前两周的平均得分<本场得分为主力
    home_player_mean = home['球员'].apply(
        lambda x: get_main_player_mean_socre(all_format_team, x, df['日期'][0], match_series['主队']))
    guest_player_mean = guest['球员'].apply(
        lambda x: get_main_player_mean_socre(all_format_team, x, df['日期'][0], match_series['客队']))
    match_series['主队主力'] = home[home_player_mean
                                < home_player_mean.mean()]['球员'].values
    match_series['客队主力'] = guest[guest_player_mean
                                 < guest_player_mean.mean()]['球员'].values

    match_series['主队队员'] = home['球员'].values
    match_series['客队队员'] = guest['球员'].values

    match_series['主队得分'] = home['得分'].sum()
    match_series['客队得分'] = guest['得分'].sum()

    return pd.DataFrame(match_series).T


# In[5]:


def get_all_info(all_format_team):  # 加了个参数 all_format_team
    all_info = pd.DataFrame(columns=['日期', '主队', '客队', '主队主力', '客队主力', '主队队员', '客队队员', '主队得分', '客队得分'])
    dir_path = r'./matches'
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            date = name.split(' ')[0].replace('年', '-').replace('月', '-').replace('日', '')
            team1 = name.split(' ')[1]
            team2 = name.split(' ')[2].split('.')[0]
            all_info = all_info.append(
                get_single_match(transform_format_match(os.path.join(root, name), team1, team2, date), all_format_team))
            all_info[['主队得分', '客队得分']] = all_info[['主队得分', '客队得分']].astype('int')
    return all_info.reset_index(drop=True)


# In[6]:


def get_tired_status(df):  # 求疲劳状态

    def F(x):
        today = x['日期']
        yesterday = today + timedelta(days=-1)
        yesterday_teams = set(df[df['日期'] == yesterday]['主队'].values) | set(df[df['日期'] == yesterday]['客队'].values)
        return 1 if x['主队'] in yesterday_teams else 0

    def G(x):
        today = x['日期']
        yesterday = today + timedelta(days=-1)
        yesterday_teams = set(df[df['日期'] == yesterday]['主队'].values) | set(df[df['日期'] == yesterday]['客队'].values)
        return 1 if x['客队'] in yesterday_teams else 0

    df['主队疲劳'] = df.apply(lambda x: F(x), axis=1)

    df['客队疲劳'] = df.apply(lambda x: G(x), axis=1)
    df = df[(df['主队'] != '字母哥队') & (df['主队'] != '美国队')]
    df = df[(df['客队'] != '字母哥队') & (df['客队'] != '美国队')]
    return df


# In[7]:


def get_all_format_team():
    all_format_team = pd.DataFrame(columns=['球员', '投篮', '3分', '罚球', '前场', '后场', '篮板', '助攻', '犯规',
                                            '抢断', '失误', '封盖', '得分', '主队/客队', '队伍', '投篮命中', '3分命中',
                                            '罚球命中', '日期'])
    dir_path = r'./matches'
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            date = name.split(' ')[0].replace('年', '-').replace('月', '-').replace('日', '')
            team1 = name.split(' ')[1]
            team2 = name.split(' ')[2].split('.')[0]
            all_format_team = all_format_team.append(
                transform_format_match(os.path.join(root, name), team1, team2, date))
    return all_format_team.reset_index(drop=True)


# In[8]:


def get_player_score(all_format_team, player, time):
    return all_format_team[(all_format_team['球员'] == player) & (all_format_team['日期'] == time)]['得分'].iloc[0]


# In[9]:


def get_different_player(before, now):
    droped_player = list(filter(None, [player if ((now == player).any() == False) else None for player in before]))
    new_player = list(filter(None, [player if ((before == player).any() == False) else None for player in now]))
    return droped_player, new_player


# In[10]:


def get_update_score(team_name, one_match, today_match):
    pk_one = one_match
    today = today_match.iloc[0]
    beforetime = one_match['日期'].to_datetime64()
    nowtime = today['日期']
    if (team_name == pk_one['主队']) & (team_name == today['主队']):
        before = pk_one['主队主力']
        now = today['主队主力']
    elif (team_name == pk_one['主队']) & (team_name == today['客队']):
        before = pk_one['主队主力']
        now = today['客队主力']
    elif (team_name == pk_one['客队']) & (team_name == today['主队']):
        before = pk_one['客队主力']
        now = today['主队主力']
    else:
        before = pk_one['客队主力']
        now = today['客队主力']
    droped_player, new_player = get_different_player(before, now)
    total = 0
    drop_total = sum(
        [get_main_player_mean_socre(all_format_team, player, beforetime, team_name) for player in droped_player])
    new_total = sum([get_main_player_mean_socre(all_format_team, player, nowtime, team_name) for player in new_player])
    total = new_total - drop_total
    return total


# In[11]:


def modify_score(team1, team2, time):
    today_match = modified_info[((modified_info['主队'] == team1) & (modified_info['客队'] == team2) | (
                modified_info['主队'] == team2) & (modified_info['客队'] == team1)) & (modified_info['日期'] == time)]
    before_match_list = (modified_info[((modified_info['主队'] == team1) & (modified_info['客队'] == team2) | (
                modified_info['主队'] == team2) & (modified_info['客队'] == team1)) & (
                                                   modified_info['日期'] < time)]).reset_index(drop=True)
    team1_score = 0
    team2_score = 0
    if before_match_list.shape[0] > 0:
        for i in range(before_match_list.shape[0]):
            team1_score = get_update_score(team1, before_match_list.loc[i], today_match)
            team2_score = get_update_score(team2, before_match_list.loc[i], today_match)
            if team1 == today_match['主队'].iloc[0]:
                modified_info.loc[(modified_info['日期'] == time) & (modified_info['主队'] == team1), '主队得分'] += team1_score
                modified_info.loc[(modified_info['日期'] == time) & (modified_info['客队'] == team2), '客队得分'] += team2_score
            elif team1 == today_match['客队'].iloc[0]:
                modified_info.loc[(modified_info['日期'] == time) & (modified_info['主队'] == team2), '主队得分'] += team2_score
                modified_info.loc[(modified_info['日期'] == time) & (modified_info['客队'] == team1), '客队得分'] += team1_score


# In[12]:


def compute_true_ability(init_matrix):
    # 构建转移矩阵P
    S = init_matrix.sum(axis=1).reshape(30, 1)
    P = init_matrix / S

    class PRIterator:
        __doc__ = '''计算一张图中的PR值'''

        def __init__(self, dg):
            self.damping_factor = 0.85  # 阻尼系数,即α
            self.max_iterations = 100  # 最大迭代次数
            self.min_delta = 0.00001  # 确定迭代是否结束的参数,即ϵ
            self.graph = dg

        def page_rank(self):
            #  先将图中没有出链的节点改为对所有节点都有出链
            for node in self.graph.nodes():
                if len(self.graph.neighbors(node)) == 0:
                    for node2 in self.graph.nodes():
                        digraph.add_edge(self.graph, (node, node2))

            nodes = self.graph.nodes()
            graph_size = len(nodes)

            if graph_size == 0:
                return {}
            page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
            damping_value = (1.0 - self.damping_factor) / graph_size  # 公式中的(1−α)/N部分

            flag = False
            for i in range(self.max_iterations):
                change = 0
                for node in nodes:
                    rank = 0
                    total = S[team_df[node]]
                    for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
                        rank += self.damping_factor * page_rank[incident_page] / (
                            len(self.graph.neighbors(incident_page)))
                        # rank += self.damping_factor * (page_rank[incident_page]*(init_matrix[team_df[node] ][ team_df[incident_page] ]+init_matrix[team_df[incident_page] ][ team_df[node] ])/total /(len(self.graph.neighbors(incident_page))))
                        # 这个效果也还行
                        # rank += self.damping_factor * page_rank[incident_page]*(np.exp(P[team_df[node] ][ team_df[incident_page] ])+np.exp(P[team_df[incident_page] ][ team_df[node] ])) / len(self.graph.neighbors(incident_page))
                    rank += damping_value
                    change += abs(page_rank[node] - rank)  # 绝对值
                    page_rank[node] = rank
                if change < self.min_delta:
                    flag = True
                    break
            return page_rank

    dg = digraph()
    G = nx.DiGraph()
    dg.add_nodes(['国王', '步行者', '篮网', '勇士', '爵士', '马刺', '凯尔特人', '快船', '灰熊', '公牛',
                  '奇才', '活塞', '老鹰', '骑士', '76人', '太阳', '开拓者', '热火', '雷霆', '雄鹿', '黄蜂',
                  '尼克斯', '独行侠', '魔术', '鹈鹕', '森林狼', '猛龙', '湖人', '掘金', '火箭'])
    for i in range(len(team_list)):
        for j in range(len(team_list)):
            if init_matrix[i][j] > 0:
                G.add_edge(team_list[i], team_list[j])
                dg.add_edge((team_list[i], team_list[j]))
    pr = PRIterator(dg)
    page_ranks = pr.page_rank()

    team_ability = pd.DataFrame.from_dict(page_ranks, orient='index', columns=['球队实力'])
    team_ability = team_ability['球队实力']
    return team_ability


# In[13]:


# 比如说我这个时候想要预测当前这场比赛, 那么, 我就要计算这场比赛开始之前, 所有队伍的真实实力, 然后加入疲劳状态的特征去预测当前的胜负
# 参数要有这场比赛的时间
# 必须要有一个自动更新的功能, 即来一场比赛, 我就自动更新一次队伍实力

def compute_teams_true_ability(modified_info, team_list, team_df):
    true_ability_df = pd.DataFrame()
    for index, row in modified_info.iterrows():
        modify_score(row['主队'], row['客队'], row['日期'])

    init_matrix = np.zeros((30, 30))
    bad_rows = 0  # 非常规队伍

    # modified_info = modified_info[modified_info['日期'] < date_time]
    for index, row in tqdm(modified_info.iterrows()):
        home = row['主队']
        guest = row['客队']
        if home not in team_list or guest not in team_list:
            bad_rows += 1
            continue
        if row['主队得分'] < row['客队得分']:
            init_matrix[team_df[home]][team_df[guest]] += 1
        else:
            init_matrix[team_df[guest]][team_df[home]] += 1
        true_ab = compute_true_ability(init_matrix)
        true_ability_df[row['日期']] = true_ab
    return true_ability_df


# In[14]:


def get_train_matrix(modified_info, team_list, team_df, team_ab_df):
    # 暂时取消了主客场的特征
    # 构建矩阵

    train_data = pd.DataFrame(columns=['team1_tired', 'team2_tired', 'team1_ability', 'team2_ability', 'label'])

    train_data['team1_tired'] = modified_info['主队疲劳'].values
    train_data['team2_tired'] = modified_info['客队疲劳'].values

    def H(x):
        if x['主队得分'] >= x['客队得分']:
            return 1
        else:
            return 0

    train_data['label'] = modified_info.apply(lambda x: H(x), axis=1)

    # train_data['日期'] = modified_info['日期'].values
    # train_data['主队'] = modified_info['主队'].values
    # train_data['客队'] = modified_info['客队'].values
    def F(x):
        # print(team_ab_df[x['日期']][x['主队']])
        return team_ab_df[x['日期']][x['主队']]

    def G(x):
        # print(team_ab_df[x['日期']][x['客队']])
        return team_ab_df[x['日期']][x['客队']]

    train_data['team1_ability'] = modified_info.apply(lambda x: F(x), axis=1)
    train_data['team2_ability'] = modified_info.apply(lambda x: G(x), axis=1)

    return train_data


def predict_match_result(model,today_match):
    y_pred = model.predict(today_match)
    return y_pred


# In[15]:

# start
# 得到所有初始csv表经过格式修改后的拼接
print('all_format_team')
all_format_team = get_all_format_team()
all_format_team_gp = all_format_team.groupby('球员').apply(lambda x: x.sort_values(by=['日期']))
all_format_team = all_format_team_gp.reset_index(drop=True)
# 计算每一场比赛的情况
all_info = get_all_info(all_format_team)
all_info = get_tired_status(all_info)
print('all_info')
# 得分修正
modified_info = all_info.copy()

# page_rank
team_list = all_info['主队'].unique()
modified_info = modified_info[modified_info['客队'].isin(team_list)]
team_dict = {}
for index, team in enumerate(team_list):
    team_dict[team] = index
team_df = pd.Series(team_dict)


#
# team_ab_df = compute_teams_true_ability(modified_info, team_list, team_df)
# modified_info.reset_index(drop=True, inplace=True)
# print('modified_info')
# #存入mysql team_ab
# conn_db.delecte_all()
# team_ab_sql=team_ab_df.T.reset_index()
# team_ab_sql.rename(columns={'index': '时间'}, inplace=True)
# conn = create_engine('mysql+mysqldb://root:whlg201898.@localhost:3306/nba?charset=utf8')
# pd.io.sql.to_sql(team_ab_sql,'team_ab_record',con=conn,schema='nba',if_exists = 'append',index=None)
# print('team_ab_sql')
#
#
# modified_info.head()
#
# modified_info.to_csv('./modified_info.csv',index=False)
#
#
# # conn = create_engine('mysql+mysqldb://root:whlg201898.@localhost:3306/nba?charset=utf8')
# # #     df = pd.read_csv('all_info.csv',names = ['日期','主队','客队','主队主力','客队主力','主队队员','客队队员','主队得分','客队得分','主队疲劳','客队疲劳'])
# # #     df=df[1:]
# # pd.io.sql.to_sql(modified_info,'modified_info',con=conn,schema='nba',if_exists = 'replace',index=None)
# # print('modified_info_sql')
#
#
# data = get_train_matrix(modified_info, team_list, team_df, team_ab_df)
# print('get_train_matrix')
# # In[17]:
#
#
# label = data['label']
# data.drop('label', axis=1, inplace=True)
#
# # In[18]:
#
#
#
# X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=42)
# model = RandomForestClassifier()
# model.fit(X_train, y_train)
#
#
# import pickle
# with open("model.pkl", "wb") as f:
#     pickle.dump(model, f)
# print('over')
# y_pred = model.predict(X_test)
# y_pred = predict_match_result(model,X_test)
# print(y_pred)
# # In[20]:
#
#
# sum(y_pred == y_test) / len(y_test)

# # 深度学习学P

# In[21]:

#
# class LogisticRegression(nn.Module):
#     def __init__(self):
#         super(LogisticRegression,self).__init__()
#         self.lr = nn.Linear(4,1)
#         self.sm = nn.Sigmoid()
#
#     def forward(self,x):
#         x = x.float()
#         x = self.lr(x)
#         x = self.sm(x)
#         return x
#
#
# logistic_model = LogisticRegression()
#
#
# # In[22]:
#
#
# from torch.autograd import Variable
# # 定义损失函数和优化器
# criterion = nn.BCELoss()
# optimizer = torch.optim.SGD(logistic_model.parameters(),lr=1e-3,momentum=0.9)
#
# start = time.time()
# for epoch in range(50000):
#     x = Variable(torch.tensor(X_train.values, dtype=torch.float64))
#     y = Variable(torch.tensor(y_train.values, dtype=torch.float64)).unsqueeze(1)
#    # forward
#     output = logistic_model(x)
#     y = y.float()
#     loss = criterion(output,y)
#
#     print_loss = loss.data.item()
#     mask = output.ge(0.5).float()
#     correct = (mask == y).sum()
#
#     accuracy = correct.item() / x.size(0)
#
#     # backward
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
#     if (epoch+1) % 1000 == 0:
#         print('epoch {} loss is {:.4f} accuracy is {:.4f}\n'.format(epoch+1 , print_loss,accuracy))
#         print('*'*53)
# during = time.time() - start
# print('During time {:.2f}'.format(during))
#
