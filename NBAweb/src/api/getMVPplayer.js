import {request} from '@/utils/myrequest'

// http://duing.site:8888/getScrollImg

export function getMVPlayerInfo() {
    return request({
      url: '/getMVPlayer',
      method: 'get'
    })
}

/*
{
	"MVP_player": {
		"avatarUrl": "https://nba.sports.qq.com/media/img/players/head/260x190/2544.png",
		"playerName": "勒布朗-詹姆斯",
		"record": "25.3分 | 7.8篮板 | 10.2助攻",
		"teamLogo": "http://mat1.gtimg.com/sports/nba/logo/black/13.png",
		"number": "# 23",
		"role": "前锋",
		"height": "205CM",
		"weight": "113.4KG",
		"birthday": "1984-12-30",
		"teamName": "湖人",
		"firstYear": "2003",
		"playerRadar": [{
			"name": "场均得分",
			"value": "25.3",
			"max": "34.3"
		}, {
			"name": "场均盖帽",
			"value": "0.5",
			"max": "2.9"
		}, {
			"name": "场均抢断",
			"value": "1.2",
			"max": "2.1"
		}, {
			"name": "场均篮板",
			"value": "7.8",
			"max": "15.8"
		}, {
			"name": "场均助攻",
			"value": "10.2",
			"max": "10.2"
		}]
	}
}
*/