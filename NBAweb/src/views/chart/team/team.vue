<template>
  <div class="app-container">
    <div class="all-items">
      <el-button-group v-for="(item,index) in categoryList" :key="index">
        <el-button :type="index===clickeditem?'primary':'default'"  icon="el-icon-edit" @click.native="clickItem(index)">{{item}}</el-button>
      </el-button-group>
    </div>
      <div class="category-dashboard">
        <el-collapse v-model="activeName" accordion>
  <el-collapse-item title="球员信息 Player Data" name="1">
    <div class="player-dashboard">
      <div class="rank-style">
        <top-rank :category="playerRankData.category" :detailUrl="playerRankData.detailUrl" :TopItemList="playerRankData.playerList"></top-rank>
      </div>
      <div class="chart-style">
        <highcharts :options="playerOption" :callback="myCallback"></highcharts>
      </div>
    </div>
  </el-collapse-item>
  <el-collapse-item title="球队信息 Team Data" name="2">
    <div class="team-dashboard">
          <div class="rank-style">
            <top-rank :category="teamRankData.category" :detailUrl="teamRankData.detailUrl" :TopItemList="teamRankData.teamList"></top-rank>
          </div>
          <div class="chart-style">
            <highcharts  :options="teamOption" :callback="myCallback"></highcharts>
          </div>
        </div>
  </el-collapse-item>
</el-collapse>
        
        
      </div>
  </div>
</template>

<script>
import TopRank from '@/components/TopRank/TopRank'
import EChartCmp from '@/components/EChartCmp/EChartCmp'
import {Chart} from 'highcharts-vue'
import mvpData from '@/chart-options/mvpData'
import {getTopRank} from '@/api/topdata'
import {getTopChart} from '@/api/getTopChart'
// /getTeamData?model=defen /getPlayerData?model=defen

const barPlayerOption ={
        chart: {
            type: 'column'
        },
        title: {
            text: '得分统计'
        },
        xAxis: {
            categories: [],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: '得分'
            },
            plotLines:[{
                zIndex: 10,
                color:'red',            //线的颜色，定义为红色
                dashStyle:'longdash',//标示线的样式，默认是solid（实线），这里定义为长虚线
                value:0,                //定义在哪个值上显示标示线，这里是在x轴上刻度为3的值处垂直化一条线
                width:4,                //标示线的宽度，2px
                label:{
                  text:'平均值',     //标签的内容
                  align:'right',                //标签的水平位置，水平居左,默认是水平居中center
                  // x:10,                         //标签相对于被定位的位置水平偏移的像素，重新定位，水平居左10px
                  width:10
              }
            }]
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
                // borderWidth: 0,
                colorByPoint:true
            }
        },
        series: [{
            name: '',
            data: []
        }]
    }

const barTeamOption ={
        chart: {
            type: 'column'
        },
        title: {
            text: '得分统计'
        },
        xAxis: {
            categories: [],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: '得分'
            },
            plotLines:[{
                zIndex: 10,
                color:'red',            //线的颜色，定义为红色
                dashStyle:'longdash',//标示线的样式，默认是solid（实线），这里定义为长虚线
                value:0,                //定义在哪个值上显示标示线，这里是在x轴上刻度为3的值处垂直化一条线
                width:4,                //标示线的宽度，2px
                label:{
                  text:'平均值',     //标签的内容
                  align:'right',                //标签的水平位置，水平居左,默认是水平居中center
                  // x:10,                         //标签相对于被定位的位置水平偏移的像素，重新定位，水平居左10px
                  width:10
              }
            }]
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
                // borderWidth: 0,
                colorByPoint:true
            }
        },
        series: [{
            name: '',
            data: []
        }]
    }

export default {
  data() { 
    return {
      activeName: '2', 
      categoryList:['场均得分','场均篮板','场均助攻','场均抢断','场均盖帽','场均失误'],
      clickeditem:0,
      playerOption: {},
      teamOption: {},
      playerRankData:{},
      teamRankData:{}
    }
  },
  mounted(){
    this.fetchTopData("defen")
  },
  components: {
    highcharts: Chart,
    EChartCmp,
    TopRank
  },
  methods:{
    myCallback(){
      console.log("this is callback function");
      // console.log(checkedItem)
    },
    fetchTopData(order){
      console.log(order)
      //player
      getTopRank("player",order).then(res => {
        // console.log("player")
        // console.log(res)
        this.playerRankData=res
      }).catch(err=>{
        console.log(err)
      })

      //teamData
      getTopRank("team",order).then(res=>{
        // console.log("team")
        this.teamRankData=res
      }).catch(err=>{
        console.log(err)
      })

      //playerChart
      getTopChart("player",order).then(res =>{
        console.log(res['top10'])
        let response=res['top10']
        barPlayerOption['xAxis']['categories']=response['categories']
        let dataIntArr=response['data'].map( data=> {return +data;} ); //字符串数组转int数组
        // dataIntArr=dataIntArr.slice(0,10)
        barPlayerOption['series']=[{
            name: response['name'],
            data: dataIntArr
        }]
        let avg=dataIntArr.reduce((temp,item,index)=>index==dataIntArr.length-1?(temp+item)/dataIntArr.length:temp+item) //求平均值
        console.log(avg)
        barPlayerOption['yAxis'].plotLines[0].value=avg
        barPlayerOption['yAxis'].min=(dataIntArr[dataIntArr.length-1]-5)>=0? dataIntArr[dataIntArr.length-1]-5:0
        this.playerOption=barPlayerOption
      }).catch(err=>{
        console.log(err)
      })


      //teamChart
      getTopChart("team",order).then(res =>{
        console.log(res['top10'])
        let response=res['top10']
        barTeamOption['xAxis']['categories']=response['categories']
        let dataIntArr=response['data'].map( data=> {return +data;} ); //字符串数组转int数组
        dataIntArr=dataIntArr.slice(0,10)
        barTeamOption['series']=[{
            name: response['name'],
            data: dataIntArr
        }]
        let avg=dataIntArr.reduce((temp,item,index)=>index==dataIntArr.length-1?(temp+item)/dataIntArr.length:temp+item) //求平均值
        console.log(avg)
        barTeamOption['yAxis'].plotLines[0].value=avg
        barTeamOption['yAxis'].min=(dataIntArr[dataIntArr.length-1]-5)>=0? dataIntArr[dataIntArr.length-1]-5:0
        this.teamOption=barTeamOption
      }).catch(err=>{
        console.log(err)
      })

    },
    clickItem(index){
      const categoryParmas=['defen','lanban','zhugong','qiangduan','gaima','shiwu']
      this.clickeditem=index
      console.log(index)
      // console.log(categoryParmas[index])
      // console.log(this.categoryList[index])
      console.log(categoryParmas[index])
      // this.playerOption= mvpData.threeScore
      // this.teamOption=mvpData.getScore
      this.fetchTopData(categoryParmas[index])
      
    }
  }
}
</script>

<style scoped>

.all-items{
  padding: 10px;
  /* position: relative; */
}
.category-dashboard{
  display: flex;
  flex-direction: column;
}

.player-dashboard{
  height: 500px;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}

.team-dashboard{
  height: 500px;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
/* .player-dashboard{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}

.team-dashboard{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
} */

/* .rank-style{
  width: 100%;
} */
/* .chart-style{
  width: 200px;
  height: 200px;
  border: solid 1px pink;
  border-radius: 10px;
  box-shadow: 0px 0px 5px 2px grey;
  padding: 10px;
  margin-top: 10px;
} */

.chart-style{
  width: 650px;
  height: 90%;
  border: solid 1px pink;
  border-radius: 10px;
  box-shadow: 0px 0px 5px 2px grey;
  padding: 10px;
}
</style>