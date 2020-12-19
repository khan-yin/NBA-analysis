<template>
  <div class="app-container">
     <div class="highchart-container" :id="id" :option="option"></div>
  </div>
</template>

<script>

import highcharts from 'highcharts'

export default {
    props:{
        id:{
            type: String,
        },
        datas:{
            type:Array,
            default(){
                return []
            }
        },
        name:{
            type:String,
            default: "test"
        }    
    },
    mounted(){
        const option ={
            title: {
                    text: '2010 ~ 2016 年太阳能行业就业人员发展情况'
            },
            subtitle: {
                    text: '数据来源：thesolarfoundation.com'
            },
            yAxis: {
                    title: {
                            text: '就业人数'
                    }
            },
            legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle'
            },
            plotOptions: {
                    series: {
                            label: {
                                    connectorAllowed: false
                            },
                            pointStart: 2010
                    }
            },
            series: [{
                    name: this.name,
                    data: this.datas
            }],
            responsive: {
                    rules: [{
                            condition: {
                                    maxWidth: 500
                            },
                            chartOptions: {
                                    legend: {
                                            layout: 'horizontal',
                                            align: 'center',
                                            verticalAlign: 'bottom'
                                    }
                            }
                    }]
            }
        }
        highcharts.chart("test", option)
    },
    methods:{
        update(){
            
        }
    }

}
</script>

<style scoped>

</style>