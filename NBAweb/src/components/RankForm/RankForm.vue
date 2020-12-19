<template>
  <div>
      <el-table
    :data="rankList"
    stripe
    style="width: 100%">
    <el-table-column
      prop="rank"
      label="排名"
      width="60">
    </el-table-column>
    <el-table-column label="LOGO">
    <template slot-scope="scope">
      <img  :src="scope.row.teamLogo" alt="" style="width: 40px;height: 40px">
    </template>
    </el-table-column>
    <el-table-column
      prop="teamName"
      label="球队" >
    </el-table-column>
    <el-table-column
      prop="win"
      label="胜">
    </el-table-column>
    <el-table-column
      prop="lose"
      label="负">
    </el-table-column>
    <el-table-column
      prop="winDiffer" 
      label="胜场差">
    </el-table-column>
    <el-table-column
      prop="winRate"
      label="胜率">
    </el-table-column>
    <el-table-column
      prop="homeCourt"
      label="主场">
    </el-table-column>
    <el-table-column
      prop="groundCourt"
      label="客场">
    </el-table-column>
    <el-table-column
      prop="area"
      label="地区">
    </el-table-column>
    <el-table-column
      prop="winScore"
      label="得分">
    </el-table-column>
    <el-table-column
      prop="losePoint"
      label="得分">
    </el-table-column>
    <el-table-column
      prop="netVictory"
      label="净胜">
    </el-table-column>
    <el-table-column
      prop="winStreak"
      label="连胜/负">
    </el-table-column>

  </el-table>
  </div>
</template>

<script>
export default {
    props:{
        rankList:{
            type: Array,
            default(){
                return [
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
                    },
                    {
                    rank: '01',
                    teamName: '骑士',
                    teamLogo:"https://img1.gtimg.com/sports/pics/hv1/131/116/2220/144385211.png",
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
        }
    },

}
</script>

<style scoped>

</style>