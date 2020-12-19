<template>
  <div class="app-container">
    <!-- <h2>东部联盟</h2> -->
    <rank-form :rankList="rankList"></rank-form>
    
      
  </div>
</template>

<script>
import RankForm from '@/components/RankForm/RankForm'
import {getAreaRank} from '@/api/getAreaRank'
export default {
  data() {
      return {
        rankList: []
      }
  },
  components:{
    RankForm
  },
  mounted(){
    getAreaRank("east").then(res=>{
      // console.log(res)
      this.rankList=res
    }).catch(err=>{

    })
  }
}
</script>

<style scoped>

</style>