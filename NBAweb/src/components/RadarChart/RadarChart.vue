//radar-chart.vue （子组件）

<template>
    <div ref="main" class="container">
    </div>
</template>

<script>
 // 引入基本模板
 import echarts from 'echarts/lib/echarts'
 // 引入雷达图组件
 import 'echarts/lib/chart/radar'
 // 引入提示框和图例组件
 import 'echarts/lib/component/tooltip'
 import 'echarts/lib/component/legend'
 export default {
  name: "radar-chart",
  props: {        //接受父组件传递来的数据
   items: {
    type: Array,
    default () {    //默认数据，没有数剧的情况下启用
     return [{name: '场均得分', value: 25.3, max: '35'},   {name: '场均盖帽', value: 0.5, max: '2.5'},{name: '场均抢断', value: 1.2, max: '2'}, {name: '场均篮板', value: 7.8, max: '15'},{name: '场均助攻', value: 10.2, max: '10'}]
    }
   },
  },
  mounted(){
   let values = [] //提炼接收到的数据
   this.items.forEach(el => {
    values.push(el.value)  
   })            
   const option = { //覆盖配置数据option
    tooltip: {},
    radar: {
        indicator: this.items, 
        center: ['50%', '51%']
    },
    series: [{
     type: 'radar',
     itemStyle: {normal: {areaStyle: {type: 'default'}}},
     data: [
      {
       value: values, 
       name: '各项得分',
       itemStyle: {normal: {color: '#2AB1FF'}}
      }
     ]
    }]
   }
   //初始化
//    const chartObj = echarts.init(document.getElementById('radar'))
const chartObj = echarts.init(this.$refs.main)
   chartObj.setOption(option)
  }
 }
</script>
<style scoped>
 .container{width: 250px;height: 250px;}
</style>