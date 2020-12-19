<template>
  <div class="app-container">
    <div class="card" >
      <div id="triangle-topleft">
        </div>
    <el-row type="flex" class="row-bg" justify="space-around" >
      <el-col :span="6" class="card-item">
        <div class="player">
          <div class="avatar">
            <img  :src="playerInfo.avatarUrl" alt="" mode="widthFix">
          </div>
          <h2>{{playerInfo.playerName}}</h2>
          <span>{{playerInfo.record}}</span>
        </div>
        </el-col>
      <el-col :span="6" class="card-item">
        <div class="player-info">
          <div>
          <h2>球员信息</h2>
          <p>号码：{{playerInfo.number}}</p>
          <p>位置：{{playerInfo.role}}</p>
          <p>身高：{{playerInfo.height}}</p>
          <p>体重：{{playerInfo.weight}}</p>
          <p>生日：{{playerInfo.birthday}}</p>
          <p>球队：{{playerInfo.teamName}}</p>
          <p>选秀年：{{playerInfo.firstYear}}</p>
          </div>
          <img class="logo" :src="playerInfo.teamLogo" alt="">
          
        </div>
        </el-col>
      <el-col :span="6" class="card-item">
        <h2>球员实力</h2>
        <div class="player-radar" style="width: 320px;height: 320px">
          <radar-chart :items="playerInfo.playerRadar" style="width: 320px;height: 250px" ></radar-chart>
        </div>
        </el-col>
  </el-row>
</div>

<div class="record-data-chart">
  <!-- <p>本赛季数据</p> -->
  <div class="mvp-data-chart">
    <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="季前赛" name="0">
      <el-radio-group v-for="(item,index) in checkBox" v-model="checkedItem" @change="updateChart" size="middle" :key="index">
      <el-radio-button :label="item"></el-radio-button>
    </el-radio-group>
    <div class="chart-style">
      <highcharts :options="chartOptions" :callback="myCallback"></highcharts>
    </div>
    </el-tab-pane>
    
    <el-tab-pane label="常规赛" name="1">
      <el-radio-group v-for="(item,index) in checkBox" v-model="checkedItem" @change="updateChart" size="middle" :key="index">
      <el-radio-button :label="item"></el-radio-button>
    </el-radio-group>
    <div class="chart-style">
      <highcharts :options="chartOptions" :callback="myCallback"></highcharts>
    </div>
    </el-tab-pane>
    <el-tab-pane label="季后赛" name="2">
      <el-radio-group v-for="(item,index) in checkBox" v-model="checkedItem" @change="updateChart" size="middle" :key="index">
      <el-radio-button :label="item"></el-radio-button>
    </el-radio-group>
    <div class="chart-style">
      <highcharts :options="chartOptions" :callback="myCallback"></highcharts>
    </div>
    </el-tab-pane>
  </el-tabs>
    <!-- <p>本赛季数据</p> -->
    
    
    </div>

  <div class="other-info">
   <div class="recent-match">
      <div style="border-bottom: solid 1px #E2E2E2">
      <h2 style="margin-top: 2px; margin-bottom: 2px; color: grey">近期赛程</h2>
    </div>
    <div>
      <el-table
    :data="recentMatch"
    stripe
    style="width: 100%;" :show-header="false">
    <el-table-column
      prop="time"
      label="时间">
          </el-table-column>
    <el-table-column
      prop="compete"
      label="比赛">
    </el-table-column>
    <el-table-column
      prop="result"
      label="结果">
    </el-table-column>
  </el-table>
    </div>
   </div>

   
  </div>

  
</div>

<div class="career-data">
    <div class="year-data">
      <h2 style="margin-top: 2px; margin-bottom: 2px; color: grey">年度数据</h2>
     <e-chart-cmp :option="HitOption" ref="myEchartChild"></e-chart-cmp>
   </div>

   <div class="career-chart">
     <h2 style="margin-top: 2px; margin-bottom: 2px; color: grey">职业生涯</h2>
     <highcharts :options="careerOption" :callback="myCallback"></highcharts>
   </div>
  </div>

  </div>
</template>

<script>
import RadarChart from '@/components/RadarChart/RadarChart'
import HighChartCmp from '@/components/HighChartCmp/HighChartCmp'
import EChartCmp from '@/components/EChartCmp/EChartCmp'
import mvpData from '@/chart-options/mvpData'
import {Chart} from 'highcharts-vue'
import {getMVPlayerInfo} from '@/api/getMVPplayer'
import {getMVPPlayerVS} from '@/api/getMVPRecentVS'
import {getMVPData} from '@/api/getMVPData'
import {getMVPCareer} from '@/api/getMVPCareer'

const matchOption={
      title: {
        text: '本赛季数据'
      },
      xAxis: {
        categories: []
      },
      yAxis: {
            min: 0,
            title: {
                text: '得分'
            }
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
          data: [],
          marker: {
            lineWidth: 2,
            // lineColor: HighCharts.getOptions().colors[5],
            lineColor:'#fba845',
            fillColor: '#FFFFFF',
          },
        }]
}


const yearOption={
        angleAxis: {
        },
        radiusAxis: {
            type: 'category',
            data: [],
            z: 800
        },
        polar: {
        },
        series: [{
            type: 'bar',
            data: [],
            coordinateSystem: 'polar',
            name: '罚球%',
            stack: 'a'
        }, {
            type: 'bar',
            data: [],
            coordinateSystem: 'polar',
            name: '命中%',
            stack: 'a'
        }, {
            type: 'bar',
            data: [],
            coordinateSystem: 'polar',
            name: '三分%',
            stack: 'a'
        }],
        legend: {
            show: true,
            data: ['罚球%', '命中%', '三分%']
        }
}

const careerPlayerOption={
      chart: {
        type: 'column'
      },
      title: {
        text: '职业生涯数据'
      },
      xAxis: {
        categories: []
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
      plotOptions: {
        column: {
          stacking: 'normal'
        }
      },
      series: [{
        type: 'column',
        name: '篮板',
        data: [],
        stack: 'lanban'
      }, {
        type: 'column',
        name: '助攻',
        data: [],
        stack: 'zhugong'
      }, {
        type: 'column',
        name: '抢断',
        data: [],
        stack: 'other'
      },{
        type: 'column',
        name: '盖帽',
        data: [],
        stack: 'other'
      },{
        type: 'column',
        name: '犯规',
        data: [],
        stack: 'other'
      }, {
        type: 'spline',
        name: '得分',
        data: [],
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
}

export default {
  data(){
    return{
      playerInfo: {},
      currentItem: 1,
      checkedItem:'得分',
      activeName: '1',
      checkBox:['得分','三分球%','篮板','助攻','抢断','盖帽','失误','罚球%'],
      mvpData:mvpData,
      chartOptions:{},
      recentMatch:[],
      HitOption: yearOption,
      careerOption: {},
    }
  },
  components:{
    RadarChart,
    HighChartCmp,
    highcharts: Chart,
    EChartCmp
  },
  mounted(){
    this.getPlayerInfo()
    this.getRecentMatch()
    const categoryList = ["before","normal","after"]
    let category=categoryList[this.activeName]
    console.log(category)
    console.log(this.activeName)
    let label=this.checkedItem
    this.getPlayerRecord(category,label)
    this.getCareerRecord()
  },
  methods:{
    handleClick(tab, event) {
        // console.log(tab, event)
        console.log(this.activeName)
        const categoryList = ["before","normal","after"]
        let category=categoryList[this.activeName]
        let label=this.checkedItem
        this.getPlayerRecord(category,label)
    },
    updateChart(label){
      const categoryParams=['defen','mingzhong3','lanban','zhugong','qiangduan','gaimao','shiwu','faci']
      console.log(label)
      let index=this.checkBox.indexOf(label)
      
      let order=categoryParams[index]
      console.log(order)
      const categoryList = ["before","normal","after"]
      let category=categoryList[this.activeName]
      this.getPlayerRecord(category,label)
      // if(section==='三分球')
      //   this.chartOptions=mvpData.threeScore
      // else if (section==='得分')
      //   this.chartOptions=mvpData.getScore
      // else
      //   this.chartOptions=mvpData.loseScore

      
      // console.log(mvpData.threeScore)
      // console.log(this.option)
      
    },
    myCallback(){
      console.log("this is callback function");
      // console.log(checkedItem)
    },
    getPlayerInfo(){
      getMVPlayerInfo().then(res =>{
        // console.log(res)
        console.log(res['MVP_player'])
        this.playerInfo=res['MVP_player']
      }).catch(err =>{
        console.log(err)
      })
    },
    getRecentMatch(){
      getMVPPlayerVS().then(res =>{
        console.log(res['recentVS'])
        this.recentMatch=res['recentVS']
      }).then(err =>{
        console.log(err)
      })
    },
    getPlayerRecord(category,label){
      const categoryParams=['defen','mingzhong3','lanban','zhugong','qiangduan','gaimao','shiwu','faci']
      // console.log(label)
      let index=this.checkBox.indexOf(label)
      
      let order=categoryParams[index]
      // console.log(order)
      getMVPData(category,order).then(res =>{
        console.log(res['MVP_data'])
        let response =res['MVP_data']
        matchOption['xAxis'].categories=response['time']
        let dataIntArr = response['data'].map(item => {return +item})
        console.log(dataIntArr)
        matchOption['series'][0].data=dataIntArr
        matchOption['series'][0].name=label
        this.chartOptions=matchOption
        console.log(matchOption)
        // this.chartOptions
      }).catch(err =>{
        console.log(err)
      })
    },
    getCareerRecord(){
      getMVPCareer().then(res =>{
        console.log(res['MVP_career'])
        let careerData=res['MVP_career']
        yearOption['radiusAxis'].data=careerData.time
        yearOption['series'][0].data=careerData.penaltyShot
        yearOption['series'][1].data=careerData.scoreHit
        yearOption['series'][2].data=careerData.threeHit
        this.HitOption=yearOption
        this.$refs.myEchartChild.chartInit()
        careerPlayerOption['xAxis'].categories=careerData.time
        careerPlayerOption['series'][0].data=careerData.backBorad.map(item => {return +item})
        careerPlayerOption['series'][1].data=careerData.assists.map(item => {return +item})
        careerPlayerOption['series'][2].data=careerData.snatch.map(item => {return +item})
        careerPlayerOption['series'][3].data=careerData.shotBlock.map(item => {return +item})
        careerPlayerOption['series'][4].data=careerData.foul.map(item => {return +item})
        careerPlayerOption['series'][5].data=careerData.getScore.map(item => {return +item})
        this.careerOption=careerPlayerOption
      }).catch(err =>{
        console.log(err)
      })
      // yearOption['radiusAxis'].data=mvpData.mmd.time
      // yearOption['series'][0].data=mvpData.mmd.penaltyShot
      // yearOption['series'][1].data=mvpData.mmd.scoreHit
      // yearOption['series'][2].data=mvpData.mmd.threeHit
      // this.HitOption=yearOption
      // this.$refs.myEchartChild.chartInit()
      // careerPlayerOption['xAxis'].categories=mvpData.mmd.time
      // careerPlayerOption['series'][0].data=mvpData.mmd.backBorad
      // careerPlayerOption['series'][1].data=mvpData.mmd.assists
      // careerPlayerOption['series'][2].data=mvpData.mmd.snatch
      // careerPlayerOption['series'][3].data=mvpData.mmd.shotBlock
      // careerPlayerOption['series'][4].data=mvpData.mmd.foul
      // careerPlayerOption['series'][5].data=mvpData.mmd.getScore
      // this.careerOption=careerPlayerOption
    }
  }
}
</script>

<style scoped>
.player{
  display: flex;
  flex-direction: column;
  text-align: center;
  align-items: center;
}

#triangle-topleft {
    width: 0;
    height: 0;
    border-top: 100px solid #005896;
    border-right: 100px solid transparent;
    position: absolute;
}
.logo{
  width: 140px;
  height: 140px;
}

.avatar{
  margin-top: 15px;
  width: 260px;
  height: 190px;
  /* border: solid 1px gainsboro; */
  border-radius: 10px;
  overflow: hidden;
  
}

.player-info{
  display: flex;
  flex-direction: row;
}

.card{
  background-color: #f8f8f8;
  border-bottom: 1px solid #f1f1f1;
  min-height: 300px;
  /* border: solid 1px grey; */
  padding: 14,0;
  border-radius: 10px;
  box-shadow:0px 0px 5px 2px grey;
}

.player-radar{
  display: flex;
  flex-direction: column;
  align-items: center;
  /* border: solid 1px; */

}

.card-item{
  width: 400px;
  height: 350px;
  margin: 15px;
  padding: 20px;
  /* border-top: solid 2px skyblue; */
  box-shadow:0px 0px 5px 2px grey;
}

.chart-style{
  /* width: 650px; */
  width: 100%;
  height: 400px;
  border: solid 1px grey;
  border-radius: 10px;
  /* box-shadow: 0px 0px 5px 2px grey; */
  padding: 10px;
  margin-top: 10px;
  overflow: hidden;
}

.record-data-chart{
  /* margin-top: 10px; */
  /* border: solid 1px grey; */
  padding: 5px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.mvp-data-chart{
  /* margin-top: 20px; */
  /* border: solid 1px blue; */
  padding: 10px;
  /* height: 400px; */
  width: 80%;
}

.other-info{
  display: flex;
  flex-direction: column;
  align-items: center;
  /* border: solid 1px black; */
  width: 380px;
  padding: 10px;
}

.recent-match{
  width: 100%;
  border-radius: 5px;
  box-shadow: 0px 0px 5px 2px grey;
}

.year-data{
  margin-top: 10px;
  box-shadow: 0px 0px 5px 2px grey;
  border-radius: 10px;
  width: 420px;
  height: 430px;
}
.career-chart{
  width: 100%;
  box-shadow: 0px 0px 5px 2px grey;
  margin: 10px;
  height: 430px;
}

.career-data{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 100%;
  /* box-shadow: 0px 0px 5px 2px grey; */
}
</style>