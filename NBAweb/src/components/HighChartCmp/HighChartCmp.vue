<template>
    <div class="app-container">
        <div class="highchart-container" :id="id" :option="option"></div>
    </div>
</template>
<script>
    import HighCharts from 'highcharts'
    import 'highcharts/modules/exporting'
    import 'highcharts/modules/offline-exporting'
    export default {
        // 验证类型
        props: {
            id: {
                type: String
            },
            option: {
                type: Object
            }
        },
        mounted() {
            HighCharts.chart(this.id, this.option)
        }
    }
</script>
<style scoped>
.highchart-container{
    height: 300px;
    width: 600px;
}
</style>