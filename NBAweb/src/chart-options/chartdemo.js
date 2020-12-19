module.exports = {
    bar: {
        chart: {
            type:'column'//指定图表的类型，默认是折线图（line）
        },
        credits: {
            enabled:false
        },//去掉地址
        title: {
            text: '我的第一个图表' //指定图表标题
        },
        colors: ['#058DC7', '#50B432', '#ED561B', '#DDDF00','#24CBE5'],
        xAxis: {
                categories: ['1号', '2号', '3号','3号','3号'] //指定x轴分组
            },
        yAxis: {
            title: {
                text: '最近七天', //指定y轴的标题
            },
        },
        plotOptions: {
            column: {
                colorByPoint:true
            },
        },
        series: [{ //指定数据列
                name: '小明',
                data: [
                    {
                        y:1000,
                        color:"red"
                    }, 
                    5000, 
                    4000,
                    5000,
                    2000
                ]//数据
            }]
    },
    echartd:{
        title: {
        text: 'ECharts 入门示例'
        },
        tooltip: {},
        xAxis: {
        data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
        },
        yAxis: {},
        series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
        }]
    },
    radar:{ //创建图表配置数据
        tooltip: {},
        radar: {
         indicator: [{name: '体育', max: '100'}, {name: '数学', max: '100'}, {name: '化学', max: '100'}, {name: '劳动', max: '100'}, {name: '物理', max: '100'}],
         center: ['50%', '51%']
        },
        series: [{
         type: 'radar',
         itemStyle: {normal: {areaStyle: {type: 'default'}}},
         data: [
          {
           value: [58,56,78,64,98],
           name: '各项得分',
           itemStyle: {normal: {color: '#f0ad4e'}}
          }
         ]
        }]
    }
}

