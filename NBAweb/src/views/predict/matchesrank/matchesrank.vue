<template>
  <div class="app-container">排名预测
    <rank-form :rankList="rankList"></rank-form>
  </div>
</template>

<script>
import RankForm from '@/components/RankForm/RankForm'

export default {
  components:{
    RankForm,
  },
  data(){
    return {
      rankList:[
          {
          rank: '01',
          teamName: '勇士',
          teamLogo:"https://mat1.gtimg.com/sports/nba/logo/1602/9.png",
          win: '56',
          lose:'17',
          winDiffer:'0.0',
          winRate:'76%',
          homeCourt:'30-5',
          groundCourt:'26-12',
          area:'37-7', 
          winScore:'118.7',
          losePoint:'108.6',
          netVictory:'10.1',
          winStreak:'1连负'
          },
          {
          rank: '01',
          teamName: '勇士',
          teamLogo:"https://mat1.gtimg.com/sports/nba/logo/1602/9.png",
          win: '56',
          lose:'17',
          winDiffer:'0.0',
          winRate:'76%',
          homeCourt:'30-5',
          groundCourt:'26-12',
          area:'37-7', 
          winScore:'118.7',
          losePoint:'108.6',
          netVictory:'10.1',
          winStreak:'1连负'
          },
          {
          rank: '01',
          teamName: '雄鹿',
          teamLogo:"https://mat1.gtimg.com/sports/nba/logo/1602/15.png",
          win: '56',
          lose:'17',
          winDiffer:'0.0',
          winRate:'76%',
          homeCourt:'30-5',
          groundCourt:'26-12',
          area:'37-7', 
          winScore:'118.7',
          losePoint:'108.6',
          netVictory:'10.1',
          winStreak:'1连负'
          }
        ]
    }
  },
}
</script>

<style scoped>

</style>