<template>
    <div class="top-five">
        <el-card class="box-card">
        <div slot="header" class="clearfix">
            <span>{{category}}</span>
            <el-button style="float: right; padding: 3px 0" type="text">
            <a class="detail" target="_blank" :href="detailUrl" bosszone="SJTJ_Detail">查看全部</a>
            </el-button>
        </div>
        <div class="player-info" v-for="(item,id) in TopItemList" :key="id">
            <div class="num">{{item.num}}</div>
            <img class="Img" :src="item.img">
            <div class="name">{{item.name}}</div>
            <div class="score">{{item.score}}</div>
        </div>
    </el-card>
</div>  
</template>

<script>
export default {
    props:{
        category:{
            type: String,
        },
        detailUrl:{
            type:String,
        },
        TopItemList:{
            type: Array,
            default(){
                return []
            }
        }
    },

}
</script>

<style scoped>


.top-five {
  width: 400px;
    /* flex: 0 0 33%;
    position: relative;
    float: left;
    margin: 0 9px 20px 9px;
    width: 31%; */
    border: 1px solid #e2e2e2;
    border-radius: 10px;
}

.player-info{
  display: flex;
  flex-direction: row;
  text-align: center;
  align-items: center;
  justify-content: space-around;
  border-bottom: solid 1px #E2E2E2;
  padding: 5px 0;
}
.Img{
  width: 20%;
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

.name{
  width: 120px;
}

/* .box-card{
  background: #F3F3F3;
  padding: 10px;
}  */

.clearfix{
  margin: 0;
  padding: 0;
}
</style>