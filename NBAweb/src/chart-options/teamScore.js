module.exports ={
    chart: {
        type: 'column'
    },
    title: {
        text: '球队各项得分'
    },
    xAxis: {
        categories: ['雄鹿', '火箭', '独行侠', '快船', '鹈鹕']
    },
    series: [{
        name: '场均得分',
        data: [118.7, 117.8, 117.0, 116.3, 115.8]
    }, {
        name: '场均篮板',
        data: [51.7, 47.9, 47.7, 46.9, 46.5]
    }, {
        name: '场均助攻',
        data: [27.2, 26.9, 26.8, 26.7, 25.9]
    },{
        name: '场均抢断',
        data: [10.0,8.8,8.7,8.7,8.6]
    },{
        name: '场均盖帽',
        data: [6.6,6.1,5.9,5.7,5.6]
    },{
        name: '场均失误',
        data: [16.5,16.4,16.2,15.5,15.3]
    }]
}