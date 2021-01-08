from flask import Flask, request
# from flask import jsonify
import json
from flask_cors import CORS

from crawler.crawler_team_data import crawl_team_data
from crawler.crawler_east_west import crawl_east_west
from crawler.crawler_scroll_image import crawl_scroll_img
from crawler.crawler_MVP_player import crawl_MVP_player
from crawler.crawler_news import crawl_news
from crawler.crawler_recent_match import crawl_recent_match
from crawler.crawler_chart_Top10 import crawl_chart_Top10
from crawler.crawler_MVP_data import crawl_MVP_data
from crawler.crawler_MVP_recentVS import crawl_MVP_recentVS
from crawler.crawler_MVP_career import crawl_MVP_career
from crawler.crawler_today_match import crawl_today_match
import EDA3

app = Flask(__name__)
# 解决前后端跨域问题
CORS(app, supports_credentials=True)


# 测试
@app.route('/')
def hello_world():
    return 'NBA数据预测'


# 请求球员/球队排行榜
@app.route('/getTeamData', methods=['GET'])
def get_team_data():
    # 获取爬取的数据
    res = crawl_team_data()
    # 获取请求参数
    # types取值为['team','player']
    types = request.args.get('type')
    # order取值为['defen', 'lanban', 'zhugong', 'qiangduan', 'gaima', 'shiwu']
    order = request.args.get('order')

    # 如果参数对应球员模块
    # if types == 'player':
    #     role = res.get('player')
    #     # data = {}
    #     # 场均得分
    #     # if order == 'defen':
    #     #     data = role.get('nbaPlayerSeasonPointsRank')
    #         # print(data)
    #         # return jsonify(data) 出现乱码，放弃使用
    #         # 改用此方式避免乱码
    #         # return json.dumps(data, ensure_ascii=False)
    #
    #     # elif order == 'lanban':
    #     #     data = role.get('nbaPlayerSeasonReboundsRank')
    #     # elif order == 'zhugong':
    #     #     data = role.get('nbaPlayerSeasonAssistsRank')
    #     # elif order == 'qiangduan':
    #     #     data = role.get('nbaPlayerSeasonAssistsRank')
    #     # elif order == 'gaimao':
    #     #     data = role.get('nbaPlayerSeasonAssistsRank')
    #     # elif order == 'shiwu':
    #     #     data = role.get('nbaPlayerSeasonAssistsRank')
    #
    #
    #
    # # 如果参数对应球队模块
    # elif types == 'team':
    #     # 场均得分
    #     if order == 'defen':
    #         data = res.get('team').get('nbaTeamSeasonPointsTop5')
    #         # print(data)
    #         # return jsonify(data) 出现乱码，放弃使用
    #         # 改用此方式避免乱码
    #         return json.dumps(data, ensure_ascii=False)
    #         data = role.get(order)
    #         return json.dumps(data, ensure_ascii=False)

    role = res.get(types)
    data = role.get(order)
    return json.dumps(data, ensure_ascii=False)


# 请求东西部排名
@app.route('/getEastAndWest', methods=['GET'])
def get_east_west():
    # 获取爬取数据
    res = crawl_east_west()
    # 获取请求参数，part取值为['east','west']
    part = request.args.get('part')
    data = res.get(part)
    return json.dumps(data, ensure_ascii=False)


# 请求轮播图
@app.route('/getScrollImg', methods=['GET'])
def get_scroll_img():
    # 获取爬取数据
    res = crawl_scroll_img()
    return json.dumps(res, ensure_ascii=False)


# 请求MVP球员信息
@app.route('/getMVPlayer', methods=['GET'])
def get_MVP_palyer():
    # 获取爬取的数据
    res = crawl_MVP_player()
    return json.dumps(res, ensure_ascii=False)


# 请求动态新闻
@app.route('/getNews', methods=["GET"])
def get_news():
    res = crawl_news()
    return json.dumps(res, ensure_ascii=False)


# 请求最近比赛
@app.route('/getRecentMatch', methods=['GET'])
def get_recent_match():
    # 获取时间参数
    # 开始时间，格式2020-12-18
    startTime = request.args.get('startTime')
    # 结束时间，格式2020-12-18
    endTime = request.args.get('endTime')
    # print(startTime + '-->' + endTime)
    res = crawl_recent_match(startTime, endTime)
    return json.dumps(res, ensure_ascii=False)


# 请求图表的Top10数据
@app.route('/getChartTop10', methods=['GET'])
def get_chart_data():
    # 获取请求的参数
    # types取值为['team','player']
    types = request.args.get('types')
    # order取值为['defen','lanban','zhugong','qiangduan','gaimao','shiwu']
    order = request.args.get('order')
    res = crawl_chart_Top10(types, order)
    return json.dumps(res, ensure_ascii=False)


# 请求MVP球员数据
@app.route('/getMVPData', methods=['GET'])
def get_MVP_data():
    # 获取请求参数，category取值['after','normal','before']
    # FIXME: normal 打错，导致请求出现问题
    types = request.args.get('types')
    # categoryParams取值['defen','mingzhong3','lanban','zhugong','qiangduan','gaimao','shiwu','faci']
    order = request.args.get('order')
    res = crawl_MVP_data(types, order)
    return json.dumps(res, ensure_ascii=False)


# 请求MVP球队近期对战
@app.route('/getMVPRecentVS', methods={'GET'})
def get_MVP_recentVS():
    res = crawl_MVP_recentVS();
    return json.dumps(res, ensure_ascii=False)


# 请求MVP生涯数据
@app.route('/getMVPCareer', methods=['GET'])
def get_MVP_career():
    # types去追为['after','normal','before']
    types = request.args.get('types')
    res = crawl_MVP_career(types)
    return json.dumps(res, ensure_ascii=False)


# 请求当日球队比赛数据
@app.route('/getTodayMatch', methods=['GET'])
def get_today_match():
    res = crawl_today_match()
    return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
