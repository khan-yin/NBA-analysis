<template>
  <div>
      <el-table
    :data="predictList"
    stripe
    style="width: 100%">
    <el-table-column
      prop="time"
      label="时间">
    </el-table-column>
    
    <el-table-column label="LOGO">
    <template slot-scope="scope">
      <img  :src="scope.row.teamLogo1" alt="" style="width: 40px;height: 40px">
    </template>
    </el-table-column>

    <el-table-column
      prop="team1"
      label="客队">
    </el-table-column>
    <el-table-column
      prop="team1Tired"
      label="疲劳状态" >
    </el-table-column>
    <el-table-column
      prop="team1Ability"
      label="实力指数" >
    </el-table-column>
    
    
    
    <el-table-column label="LOGO">
    <template slot-scope="scope">
      <img  :src="scope.row.teamLogo2" alt="" style="width: 40px;height: 40px">
    </template>
    </el-table-column>
    <el-table-column
      prop="team2"
      label="主队">
    </el-table-column>
    <el-table-column
      prop="team2Tired"
      label="疲劳状态" >
    </el-table-column>
    <el-table-column
      prop="team2Ability"
      label="实力指数" >
    </el-table-column>
    <el-table-column
      prop="predictResult"
      label="结果预测">
    </el-table-column>
    <el-table-column
      prop="trueResult"
      label="真实结果">
    </el-table-column>
  </el-table>
  </div>
</template>

<script>
export default {
    props:{
        predictList:{
            type: Array,
            default(){
                return [
                    {
                    time: '2021-01-03 09:00:00',
                    team1: '雄鹿',
                    teamLogo1:"https://mat1.gtimg.com/sports/nba/logo/1602/15.png",
                    team1Tired: '0',
                    team1Ability: '0.0234',
                    team2:'雄鹿',
                    teamLogo2:"https://mat1.gtimg.com/sports/nba/logo/1602/20.png",
                    team2Tired:'1',
                    team2Ability: '0.0234',
                    predictResult: "胜",
                    trueResult:"负"
                    },
                    {
                    time: '2021-01-03 09:00:00',
                    team1: '雄鹿',
                    teamLogo1:"https://mat1.gtimg.com/sports/nba/logo/1602/15.png",
                    team1Tired: '56',
                    team2:'雄鹿',
                    teamLogo2:"https://mat1.gtimg.com/sports/nba/logo/1602/15.png",
                    team2Tired:'76%',
                    predictResult: "胜",
                    trueResult:"负"
                    },
                    {
                    time: '2021-01-03 09:00:00',
                    team1: '雄鹿',
                    teamLogo1:"https://mat1.gtimg.com/sports/nba/logo/1602/15.png",
                    team1Tired: '56',
                    team2:'17',
                    teamLogo2:"https://mat1.gtimg.com/sports/nba/logo/1602/15.png",
                    team2Tired:'76%',
                    predictResult: "胜",
                    trueResult:"负"
                    }
                ]
            }
        }
    },

}
</script>

<style scoped>

</style>