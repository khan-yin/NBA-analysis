<template>
  <div class="app-container">
      <div ref="main" class="echart-container">
  </div>
</div>
</template>

<script>
// 引入基本模板
const echarts = require('echarts');
// 引入提示框和图例组件
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/legend'

// const doption = { //创建图表配置数据
//     tooltip: {},
//     radar: {
//      indicator: [{name: '体育', max: '100'}, {name: '数学', max: '100'}, {name: '化学', max: '100'}, {name: '劳动', max: '100'}, {name: '物理', max: '100'}],
//      center: ['50%', '51%']
//     },
//     series: [{
//      type: 'radar',
//      itemStyle: {normal: {areaStyle: {type: 'default'}}},
//      data: [
//       {
//        value: [58,56,78,64,98],
//        name: '各项得分',
//        itemStyle: {normal: {color: '#f0ad4e'}}
//       }
//      ]
//     }]
// }

export default {
    // 验证类型
    props: {
        option: {
            type: Object,
            default(){
                return doption
            }
        }
    },
    mounted() {
        
        this.chartInit()
    },
    methods:{
        chartInit(){
            let bar_dv = this.$refs.main
            if(bar_dv){
                let myChart = echarts.init(this.$refs.main)
                console.log(this.option)
                myChart.setOption(this.option)
            }
            else{
                console.log("还没准备好")
            }
        }
    }
}
</script>

<style scoped>
.echart-container{width: 400px;height: 400px;}
</style>