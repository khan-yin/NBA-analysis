// import HighCharts from 'highcharts'

module.exports ={
    id: 'test',
    getScore:{
        chart: {
            type: 'line'
        },
        title: {
            text: '2010 ~ 2016 年太阳能行业就业人员发展情况'
        },
        subtitle: {
                text: '数据来源：thesolarfoundation.com'
        },
        yAxis: {
                title: {
                        text: '就业人数'
                }
        },
        legend: {
                layout: 'horizontal',
                align: 'center',
                verticalAlign: 'bottom'
        },
        plotOptions: {
                series: {
                        label: {
                                connectorAllowed: false
                        },
                        pointStart: 2010
                }
        },
        series: [{
                name: '安装，实施人员',
                data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
        }, {
                name: '工人',
                data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
        }, {
                name: '销售',
                data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
        }, {
                name: '项目开发',
                data: [null, null, 7988, 12169, 15112, 22452, 34400, 34227]
        }, {
                name: '其他',
                data: [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
        }],
        responsive: {
                rules: [{
                        condition: {
                                maxWidth: 500
                        },
                        chartOptions: {
                                legend: {
                                        layout: 'horizontal',
                                        align: 'center',
                                        verticalAlign: 'bottom'
                                }
                        }
                }]
        }
    },
    threeScore: {
        chart: {
            type: 'column'
        },
        title: {
            text: '场均得分统计'
        },
        xAxis: {
            categories: [
                '雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士'
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: '得分'
            }
        },
        tooltip: {
            // head + 每个 point + footer 拼接成完整的 table
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                borderWidth: 0
            }
        },
        series: [{
            name: '场均得分',
            data: [118.7, 117.8, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 118.7, 117.8, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 118.7, 117.8, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1]
        }]
    },
    loseScore: {
        chart: {
            type: 'column'
        },
        title: {
          text: "2010 ~ 2016 年太阳能行业就业人员发展情况"
        },
        subtitle: {
          text: "数据来源：thesolarfoundation.com"
        },
        yAxis: {
          title: {
            text: "就业人数"
          }
        },
        legend: {
          layout: "horizontal",
          align: "center",
          verticalAlign: "bottom"
        },
        plotOptions: {
          series: {
            label: {
              connectorAllowed: false
            },
            pointStart: 2010
          }
        },
        series: [
          {
            name: "安装，实施人员",
            data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
          },
          {
            name: "工人",
            data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
          },
          {
            name: "销售",
            data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
          },
          {
            name: "项目开发",
            data: [null, null, 7988, 12169, 15112, 22452, 34400, 34227]
          },
          {
            name: "其他",
            data: [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
          }
        ],
        responsive: {
          rules: [
            {
              condition: {
                maxWidth: 500
              },
              chartOptions: {
                legend: {
                  layout: "horizontal",
                  align: "center",
                  verticalAlign: "bottom"
                }
              }
            }
          ]
        }
    },
    yearData:{
        angleAxis: {
        },
        radiusAxis: {
            type: 'category',
            data: ['16-17', '17-18', '18-19', '19-20'],
            z: 800
        },
        polar: {
        },
        series: [{
            type: 'bar',
            data: [67.4,73.1,66.5,69.3],
            coordinateSystem: 'polar',
            name: '罚球%',
            stack: 'a'
        }, {
            type: 'bar',
            data: [44,44.9,44.2,44.4],
            coordinateSystem: 'polar',
            name: '命中%',
            stack: 'a'
        }, {
            type: 'bar',
            data: [34.7,36.7,36.8,35.5],
            coordinateSystem: 'polar',
            name: '三分%',
            stack: 'a'
        }],
        legend: {
            show: true,
            data: ['罚球%', '命中%', '三分%']
        }
    },
    oop:{
      name: '场均得分',
      data: [118.7, 117.8, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 118.7, 117.8, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 118.7, 117.8, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1],                                              
      categories: [
          '雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士','雄鹿','凯尔特人','勇士'],
    },
    mvpp:{
      time: ['7-26','7-24','10-17','10-12','10-10','10-06'],
      data: [20,12,18,6,320,15],
      result: [1,1,1,1,0,0]
    },
    MatchOption:{
      title: {
        text: '本赛季数据'
      },
      xAxis: {
        categories: ["2020-08-19", "2020-08-21", "2020-08-23", "2020-08-25", "2020-08-30", "2020-09-05", "2020-09-07", "2020-09-09", "2020-09-11", "2020-09-17", "2020-09-19", "2020-09-21", "2020-09-23", "2020-09-25", "2020-09-27", "2020-10-01", "2020-10-03", "2020-10-05", "2020-10-07", "2020-10-10", "2020-10-12"]
      },
      plotOptions: {
        series: {
          stacking: 'normal'
        }
      },
      series: [
        {
          type: 'spline',
          name: '平均值',
          data: [23, 10, 38, 30, 36, 20, 28, 36, 16, 29, 15, 26, 30, 26, 38, 25, 33, 25, 28, 40, 28],
          marker: {
            lineWidth: 2,
            lineColor:'#F15C80',
            fillColor: 'white',
          },
        }]
    },
    m2:{
      title: {
        text: '混合图表'
      },
      xAxis: {
        categories: ['苹果', ' 橙', '梨', '香蕉', '李子']
      },
      plotOptions: {
        series: {
          stacking: 'normal'
        }
      },
      series: [
        {
          type: 'column',
          name: '小张',
          data: [3, 2, 1, 3, 4],
          colorByPoint: true
        },{
          type: 'spline',
          name: '平均值',
          data: [3, 2.67, 3, 6.33, 3.33],
          marker: {
            lineWidth: 2,
            lineColor: '#F15C80',
            fillColor: 'white',
          },
        }]
    },
    se1:{
      title: {
        text: '混合图表'
      },
      xAxis: {
        categories: ['14-15','15-16','16-17','17-18','18-19','19-20']
      },
      plotOptions: {
        series: {
          stacking: 'normal'
        }
      },
      yAxis:[{
        title: {
          text: '坐标一',
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth : 0,
        stackLabels : {
          style : {
            color : '#fff'
          }
        }
      },{
        title: {
          text: '坐标2',
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth : 0,
        stackLabels : {
          style : {
            color : '#fff'
          }
        },
        opposite : true 
      }],
      series: [{
        type: 'column',
        name: '篮板',
        data: [6.0, 7.4, 8.6, 8.6, 8.5, 7.8],
      }, {
        type: 'column',
        name: '助攻',
        data: [7.4, 6.8, 8.7, 9.1, 8.3, 10.2],
      }, {
        type: 'column',
        name: '抢断',
        data: [1.6, 1.4, 1.2, 1.4, 1.3, 1.2],
      },{
        type: 'column',
        name: '抢断',
        data: [0.7, 0.6, 0.6, 0.9, 0.6, 0.5],
      },{
        type: 'column',
        name: '犯规',
        data: [2.0,1.9,1.8,1.7,1.7,1.8],
      },{
        type: 'spline',
        name: '得分',
        data: [25.3, 25.3, 26.4, 27.5, 27.4,25.3],
        marker: {
          lineWidth: 2,
          lineColor: '#F15C80',
          fillColor: 'white'
        },
        tooltip: {
          valueSuffix: ' mm'
        },
        yAxis: 1
      }
          ]
    },
    se2:{
      chart: {
        type: 'column'
      },
      title: {
        text: '职业生涯数据'
      },
      xAxis: {
        categories: [
          '14-15','15-16','16-17','17-18','18-19','19-20'
        ],
      },
      yAxis: [{ // Primary yAxis
        min: 0,
        labels: {
          format: '{value}',
          style: {
            // color: Highcharts.getOptions().colors[1]
          }
        },
        title: {
          text: '各指标得分占比',
          style: {
            // color: Highcharts.getOptions().colors[1]
          }
        }
      }, { 
        min:25,// Secondary yAxis
        title: {
          text: '得分',
          style: {
            // color: Highcharts.getOptions().colors[0]
          }
        },
        labels: {
          format: '{value}',
          style: {
            // color: Highcharts.getOptions().colors[0]
          }
        },
        opposite: true
      }],
      // tooltip: {
      // 	formatter: function () {
      // 		return '<b>' + this.x + '</b><br/>' +
      // 			this.series.name + ': ' + this.y + '<br/>' +
      // 			'总量: ' + this.point.stackTotal;
      // 	}
      // },
      plotOptions: {
        column: {
          stacking: 'normal'
        }
      },
      series: [{
        type: 'column',
        name: '篮板',
        data: [6.0, 7.4, 8.6, 8.6, 8.5, 7.8],
        stack: 'lanban'
      }, {
        type: 'column',
        name: '助攻',
        data: [7.4, 6.8, 8.7, 9.1, 8.3, 10.2],
        stack: 'zhugong'
      }, {
        type: 'column',
        name: '抢断',
        data: [1.6, 1.4, 1.2, 1.4, 1.3, 1.2],
        stack: 'other'
      },{
        type: 'column',
        name: '抢断',
        data: [0.7, 0.6, 0.6, 0.9, 0.6, 0.5],
        stack: 'other'
      },{
        type: 'column',
        name: '犯规',
        data: [2.0,1.9,1.8,1.7,1.7,1.8],
        stack: 'other'
      }, {
        type: 'spline',
        name: '得分',
        data: [25.3, 25.3, 26.4, 27.5, 27.4,25.3],
        marker: {
          lineWidth: 2,
          lineColor: '#F15C80',
          fillColor: 'white'
        },
        // tooltip: {
        // 	// valueSuffix: ' mm'
        // },
        yAxis: 1
      }]
    },
    mmd:{
      time: ['14-15','15-16','16-17', '17-18', '18-19', '19-20'],
      penaltyShot: [71,73.1,67.4,73.1,66.5,69.3], //罚球%
      scoreHit: [48.8,52,44,44.9,44.2,44.4], //命中%
      threeHit: [35.4,30.9,34.7,36.7,36.8,35.5], //三分%
      backBorad: [6.0, 7.4, 8.6, 8.6, 8.5, 7.8], //篮板
      getScore: [25.3, 25.3, 26.4, 27.5, 27.4,25.3], //得分
      assists: [7.4, 6.8, 8.7, 9.1, 8.3, 10.2], //助攻
      shotBlock: [0.7, 0.6, 0.6, 0.9, 0.6, 0.5], //盖帽
      snatch: [1.6, 1.4, 1.2, 1.4, 1.3, 1.2],//抢断
      foul: [2.0,1.9,1.8,1.7,1.7,1.8]//犯规
    }
}