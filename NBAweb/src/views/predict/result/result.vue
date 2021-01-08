<template>
  <div class="app-container">
     <!-- <video style="background-color: rgb(0, 0, 0); width: 100%; height: 100%; display: block;" webkit-playsinline="" x-webkit-airplay="" preload="auto" muted="" data-role="txp_video_tag" src="blob:https://sports.qq.com/aa8648a9-7334-43c1-9c7d-00b741c1c0b6"></video> -->
     <predict-form :predictList="predictList"></predict-form>
  </div>
</template>

<script>
import PredictForm from '@/components/PredictForm/PredictForm'
import {getTodayPredict} from '@/api/getTodayPredict'
export default {
   data(){
      return{
         predictList:[],
      }
   },
   components:{
      PredictForm
   },
   mounted(){
      getTodayPredict().then(res=>{
      // console.log(res)
      this.predictList=res['list']
    }).catch(err=>{
       console.log(err)
    })
   },
   methods:{

   }
}
</script>

<style scoped>

</style>