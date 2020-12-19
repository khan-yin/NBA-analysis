<template>
    <div class="app-container">
        <div class="player-rank" v-for="(item,index) in playerRank" :key="index">
          <div class="top-five">
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>{{item.category}}</span>
                  <el-button style="float: right; padding: 3px 0" type="text">
                    <a class="detail" target="_blank" :href="item.detailUrl" bosszone="SJTJ_Detail">查看全部</a>
                  </el-button>
                </div>
                <div class="player-info" v-for="(player,id) in item.playerTop3" :key="id">
                    <div class="num">{{player.num}}</div>
                    <img class="playerImg" :src="player.playerImg">
                    <div>
                      <p class="playerName">{{player.playerName}}</p>
                    <p class="teamName">{{player.teamName}}</p>
                    </div>
                    <div class="score">{{player.score}}</div>
                </div>
            </el-card>
          </div>     
          
        </div>
    </div>
</template>

<script>
// 导入chart组件
import HighChartCmp from '@/components/HighChartCmp/HighChartCmp'
import EChartCmp from '@/components/EChartCmp/EChartCmp'
// import options from '@/chart-options/chartdemo'
import playerRank from '@/chart-options/playerRank'

export default {
  data() {
    return {
      playerRank
  }
},
components: {
    HighChartCmp,
    EChartCmp
  },
}
</script>  

<style scoped>
.player-main {
    width: 900px;
    height: 970px;
    display: flex;
    flex-flow: wrap;
    justify-content: space-around;
    font-family: "\5FAE\8F6F\96C5\9ED1",sans-serif;
    color: #606060;
    text-align: center;
}

.top-five {
    flex: 0 0 33%;
    position: relative;
    float: left;
    margin: 0 9px 20px 9px;
    width: 31%;
    border: 1px solid #e2e2e2;
    border-radius: 10px;
}

.player-info{
  display: flex;
  flex-direction: row;
  /* text-align: center; */
  align-items: center;
  justify-content: space-around;
  border-bottom: solid 1px #E2E2E2;
  padding: 5px 0;
}
.playerImg{
  width: 25%;
  height: 10%;
}

.el-card{
  border-radius: 10px;
}
.el-card /deep/ .el-card__body {
    padding: 5px;
    padding-bottom: 0;
  }

.el-card /deep/ .el-card__header{
  padding: 10px;
  background: #F3F3F3;
}
.num{
    font-size: 30px;
    font-weight: 700;
    text-align: center;
}

.score{
  font-size: 25px;
  font-weight: 600;
  text-align: center;
}
.box-card{
  /* background: #F3F3F3; */
  /* padding: 10px; */
}

.clearfix{
  margin: 0;
  padding: 0;
}
</style>