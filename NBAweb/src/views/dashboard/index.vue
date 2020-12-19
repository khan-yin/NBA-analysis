<template>
  <div class="dashboard-container">
    <div class="index-container">
      <!-- 近期赛程 -->
        <div class="match-container">
          <div class="section">
            <div class="time-info">
              <el-button type="text" icon="el-icon-arrow-left" style="font-size: 20px; color:#fff;"></el-button>
              <!-- <div style="margin-top: 9px; margin-bottom: 9px">《 </div> -->
              <div>
                <span >{{currentDate.getMonth()+1}}月{{currentDate.getDate()}}</span>
                <span >{{weekday[currentDate.getDay()]}}</span>
              </div>
              <el-button type="text" icon="el-icon-arrow-right" style="font-size: 20px; color:#fff;"></el-button>
              <!-- <div style="margin-top: 9px; margin-bottom: 9px"> 》 </div> -->
            </div>
            <p>今日{{todayMatchCnt}}场比赛</p>
            <a href="https://nba.stats.qq.com/schedule/" target="_blank">
              <div class="detail-match">全部赛程</div>
            </a>

          </div>
          <div>
            
          </div>
          <div>
            <el-button @click="setActiveMatchList(0)"  type="text" icon="el-icon-arrow-left" class="slide-button" :disabled="curMatchIndex===0"></el-button>
          </div>
          
          <div class="recent-match">
          <el-carousel :initial-index="Math.ceil(this.matchList.length/2)" indicator-position="none" arrow="never" height="138px" :loop="false" :autoplay="false" ref="matchslide" @change="getActiveItem">
        <el-carousel-item v-for="(oneList,index) in matchList" :key="index">
          <div class="block-container">
            <div class="block-item" v-for="(item,index) in oneList" :key="index">
              <div class="info">
              <div class="head">
              <span :class="{ activeMatch: item.status==='正进行',fultureMatch: item.status==='未开始' }">{{item.time}}</span> 
              <span :class="{ activeMatch: item.status==='正进行',fultureMatch: item.status==='未开始' }">{{item.status}}</span>
              </div>
              <ul class="fight"> 
                <li class="team"> 
                    <img class="teamlogo" :src="item.leftTeamLogo" alt="">
                  <span class="name">{{item.leftTeamName}}</span> 
                  <span class="score">{{item.leftTeamScore}}</span>  
                </li> 
                <li class="team">
                    <img class="teamlogo" :src="item.rightTeamLogo" alt=""> 
                    <span class="name">{{item.rightTeamName}}</span>  
                    <span class="score">{{item.rightTeamScore}}</span>  
                </li> 
              </ul>
            </div>

              <div class="link">
              <a :href="item.video" target="_blank" v-if="item.video!=='' ">
                <div class="link-style">
                  <i class="el-icon-s-ticket" >锦集</i>
                </div>
                
              </a>
              <a :href="item.live" target="_blank" v-if="item.live!=='' ">
                <div class="link-style">
                <i class="el-icon-video-camera-solid">直播</i>
                </div>
              </a>

              
              <a :href="item.data" target="_blank" v-if="item.data!=='' ">
                <div class="link-style">
                <i class="el-icon-s-data" >数据</i>
                </div>
              </a>
              
            </div>
            
            </div>
            
          </div>
        </el-carousel-item>
      </el-carousel>
         </div>
         <div>
            <el-button @click="setActiveMatchList(1)"  type="text" icon="el-icon-arrow-right" class="slide-button" :disabled="curMatchIndex===(matchList.length-1)"></el-button>
         </div>
         
      </div>
      <div>
      <a href="https://china.nba.com/schedule/#!/7" target="_blank">
      <el-image
      style="width: 100%"
      src="http://img1.gtimg.com/chinanba/pics/hv1/250/207/2325/151236160.jpg"
      fit="cover"></el-image>
      <!-- <img src="http://img1.gtimg.com/chinanba/pics/hv1/250/207/2325/151236160.jpg" alt=""> -->
      </a>

      
      </div>
      <!-- 轮播图  -->
      <div class="hot-topic">
          <div class="swiper-style">
          <el-carousel  type="card"  indicator-position="none" height="382px">
              <el-carousel-item class="swiper-item"
                v-for="(item,index) in swiperImg" :key="index">
                <a :href="item.link" target="_blank">
                  <div>
                  <img :src="item.img" class="swiper-img" alt="轮播图">
                  <span class="shadow">{{item.title}}</span>
                </div>
                </a>
              </el-carousel-item>
          </el-carousel>
        </div>

        
      </div>

      <a href="https://qiaodan.jd.com/" target="_blank">
      <el-image
      style="width: 100%"
      src="http://img1.gtimg.com/sports/pics/hv1/24/172/2312/150381684.jpg"
      fit="cover"></el-image>
      <!-- <img src="http://img1.gtimg.com/chinanba/pics/hv1/250/207/2325/151236160.jpg" alt=""> -->
      </a>
      <div class="news-goods">
        <div class="news">
         <div class="news-header">
           <div class="news-title">
             新闻
             <!-- <el-button type="text" icon="el-icon-refresh" style="height: 40px;
  line-height: 40px; float: right;" @click="getRecentNews()">刷新</el-button> -->
             <i class="el-icon-refresh" style="height: 40px;
  line-height: 40px; float: right; cursor: pointer;" @click="getRecentNews()">
               刷新
             </i>
           
           </div>
         </div>

         <div class="news-list" v-for="(item,index) in newsList" :key="index">
            <div class="news-item">
              <a :href="item.href" target="_blank">{{item.title}}</a>
            </div>
           </div>
        </div>

        <!-- <div class="good-recommand"> -->
          <!-- <span>周边推荐</span> -->
          <!-- <div> -->
            <div class="goods" v-for="(item,index) in goods" :key="index">
            <a :href="item.href" target="_blank">
              <div class="goods-item"  >
              <el-card :body-style="{ padding: '5px' }">
              <img :src="item.img" class="good-img">
              <div>
                <p>{{item.name}}</p>
                <span style="color:#E43971; font-size:25px">{{item.price}}</span>
                <!-- <el-button type="text" class="button">操作按钮</el-button> -->
              </div>
            </el-card>
            </div>
            </a>

        </div>
          <!-- </div> -->
        <!-- </div> -->

      </div>
      
      
    </div>
    <!-- <div class="dashboard-text">name: {{ name }}</div> -->
    
  </div>
</template>

<script>

import { mapGetters } from 'vuex'
import EChartCmp from '@/components/EChartCmp/EChartCmp'
import {Chart} from 'highcharts-vue'
import {getNews} from '@/api/getNews'
import {getRecentMatch} from '@/api/getRecentMatch'
import {getScrollImg} from '@/api/getScrollImg'
// 引入雷达图组件
// import 'echarts/lib/chart/radar'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  data () {
   return {
      curMatchIndex:0,
      todayMatchCnt:0,
      weekday:["星期日","星期一","星期二","星期三","星期四","星期五","星期六"],
      goods:[
        {
          img:"https://img14.360buyimg.com/n7/jfs/t1/120190/3/8184/387318/5f239462Eedafeb57/bbec9552fc00d474.jpg",
          name:"n·b·a官方旂·舰店同款科·比12毒液篮球男鞋夏季詹·姆斯正版高帮战靴庫里4代6歐",
          href:"https://item.jd.com/72103765134.html",
          price: "￥275.00"
        },
        {
          img:"https://img10.360buyimg.com/n7/jfs/t1/129600/2/13055/469563/5f8d5a9aEde66d503/3120b85e2993bcd4.png",
          name:"耐克NIKE NBASwingmanJersey 男子球衣2020赛季洛杉矶湖人队 CW3669",
          href:"https://item.jd.com/10023275962535.html",
          price: "￥599.00"
        }
      ],
      currentDate: new Date(),
      matchList:[],
      swiperImg: [],
      newsList:[]
    }
  },
  components:{
    EChartCmp,
    highcharts: Chart,
  },
  mounted(){
    this.fectchSwiperImg()
    this.getRecentNews()
    console.log(this.currentDate)
    // console.log("year:"+this.currentDate.getFullYear())
    // console.log("month"+this.currentDate.getMonth()+1)
    // console.log("day"+this.currentDate.getDate())
    // // this.currentDate.getDate()-3
    // console.log(this.currentDate-2)
    // // this.currentDate.getDate()+3
    // console.log(this.currentDate+2)
    // console.log(this.currentDate.getFullYear()+'-'+this.currentDate.getMonth()+'-'+this.currentDate.getDay())
    let startTime=this.dateChange(-3)
    let endTime=this.dateChange(5)
    this.getMatches(startTime,endTime)
    // console.log(this.linkArray)
    // console.log(typeof this.linkArray)
  },
  methods:{
    //轮播图接口
    fectchSwiperImg(){
      getScrollImg().then(res =>{
        // console.log(res)
        console.log(res["imgs"])
        this.swiperImg=res["imgs"]
      }).catch(err=>{
        console.log(res)
      })
    },
    setActiveMatchList(flag){
      if(flag===0)//向左
        this.$refs.matchslide.prev()
        // this.$refs.matchslide.setActiveItem(index-1)
      else if(flag===1)//max 向右
      {
        this.$refs.matchslide.next()
        // this.$refs.matchslide.setActiveItem(index+1)
      }
    },
    getActiveItem(index)
    {
      // console.log(index)
      // console.log(typeof index)
      this.curMatchIndex=index;
    },
    getRecentNews()
    {
      getNews().then(res =>{
        console.log(res['news'])
        this.newsList=res['news']
      }).catch(err =>{
        console.log(err)
      })

    },
    dateChange(count){
      let date1 = new Date()
      let date2 = new Date(date1)
      date2.setDate(date1.getDate()+count)
      let time2 = date2.getFullYear()+"-"+(date2.getMonth()+1)+"-"+date2.getDate()
      return time2
    },
    getMatches(startTime,endTime){
      getRecentMatch(startTime,endTime).then(res =>{
        console.log(res['recentMatches'])
        console.log(res['today_nums'])
        this.matchList=res['recentMatches']
        this.todayMatchCnt=res['today_nums']
        // console.log(parseInt(this.matchList.length/2))
        this.curMatchIndex=Math.ceil(this.matchList.length/2)
        // this.$refs.matchslide.setActiveItem(parseInt(this.matchList.length/2))
      }).catch(err =>{
      console.log(err)
      })
      
    },

    //获取年份用getFullYear
    // 月份是从0开始的 所以你要加1
    // 获取日期是getDate不是getDay
    // getDay是获取星期几
    parasDate(date)
    {
      return date2.getFullYear()+"-"+(date2.getMonth()+1)+"-"+date2.getDate()
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    padding: 2px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}

.index-container{
  // border: solid 1px black;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.match-container{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  padding: 2px;
}
.info{
  padding: 3px;
}

.detail-match{
  background: #0079CD;
}

.detail-match:hover{
  background: #EC6A86;
}
.recent-match{
  width: 100%;
  height: 139px;
  
  
}
.link-style{
  color: #0060A1
}
.link-style:hover{
  color: #F23D63;
}


.slide-button{
  margin: 1px;
  height: 95%;
  // background:#2464B5; 
  background: #F23D63;
  font-size: 16px; 
  color:#fff;
}

.section{
  width: 136px;
  height:  132px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  text-align: center;
  background: #2464B5;
  padding: 5px;
  color: #fff;
  line-height: 22px;
}

.time-info{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  background: #0079CD;
}
.time-style{
  display: block;
  height: 25px;
  line-height: 25px;
  text-align: center;
}

.head{
    height: 30px;
    line-height: 30px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    // color: #232323;
    font-size: 13px;
}

// .hot-topic{
//   display: flex;
//   flex-direction: row;
//   align-items: center;
// }

.news{
  width: 382px;
  margin: 5px;
  // border: solid 1px black;
  // border-radius: 10px;
  // padding: 2px;
  background: #f3f3f3;
}

.activeMatch{
  color: #D51B33;
}

.fultureMatch{
  color: #0060A1;
}

.news-header{
  // background-size: 100% 100%;
  // background-size: contain;
  background-size: cover;
  background: url("https://mat1.gtimg.com/chinanba/web/statics/impnews-bg_838980.png");
}

.news-title{
  padding-left: 26px;
  padding-right: 15px;
  height: 40px;
  line-height: 40px;
  color: #fff;
  font-size: 20px;
}

.news-goods{
  width: 100%;
  display: flex;
  flex-direction: row;
  height: 340px;
  // border: solid 1px black;
  justify-content: space-around;
}

.goods{
  margin-left: 20px;
  width: 100%;
  height: 370px;
  display: flex;
  flex-direction: row;
}


.goods-item{
  width: 335px;
  height: 360px;
  // margin-top: 20px;
  margin: 5px;
}

.news-list{
  display: flex;
  flex-direction: column;
  background: #f3f3f3;
  justify-content: space-around;
  border: solid 1px grey;
}

.news-item{
  overflow: hidden;
  white-space:nowrap; 
  text-overflow:ellipsis;
  font-size: 17px;
  font-weight: 400;
  color: #081626;
  line-height: 33px;
  padding: 3px; 
}
.news-item:hover{
  // color: #F23D63
  // color: #0073C4;
  color: #E60640;
}

.shadow{
  position: absolute;
  font-size: 18px;
  font-weight: 400;
  left: 0;
  bottom: 0;
  color: #fff;
  width: 510px;
  height: 100px;
  line-height: 52px;
  padding: 48px 5px 20px;
  background: url(https://mat1.gtimg.com/pingjs/ext2020/spIndex/2019/images/focusbg-758502c1d0.png) center bottom repeat-x;
  cursor: pointer;
  overflow: hidden;
  // text-overflow: ellipsis;
  white-space: nowrap;
}

.fight{
  padding: 0;
  margin: 0;
}

.team{
  height: 36px;
  line-height: 36px;
  list-style-type:none;
  display: flex;
  flex-direction: row;
  color: #555555;
}

.teamlogo{
  width:30px;
  height:30px;
}

.name{
  width: 68%
}

.link{
  // padding-left: 30px;
  // padding-right: 30px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}


// .el-carousel__item h3 {
//     color: #475669;
//     font-size: 18px;
//     line-height: 300px;
//     // margin: 0;
//   }

.swiper-style{
  // width: 100%;
  padding: 10px;
  border-radius: 10px;
  // background:rgba(0,0,0,0.5);
  // height: 400px;
  // border: solid 1px grey;
  // box-shadow:0px 0px 5px 2px grey;
}
 
.swiper-img{
  width: 100%;
  height: 382px;
}


.block-container{
  width: 100%;
  height: 135px;
  padding-left: 5px;
  // display: flex;
  // flex-direction: row;
  // justify-content: center;
}

.block-item{
  margin-left: 9px;
  margin-right: 9px;
  width: 18%;
  height: 98%;
  border: 1px solid #f3f3f3;
  border-top: 2px solid #b1b0b0;
  display: flex;
  flex-direction: column;
  float: left;
}
.block-item:hover{
  border: solid 1px #0079CD;
  border-top: 3px solid #0079CD;
}


.good-img {
  padding-left: 40px;
  width: 75%;
}
</style>
