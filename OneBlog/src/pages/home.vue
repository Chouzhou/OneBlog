<template>
  <div>
        <p>文章类型</p>
        <!--点击选择文章类型显示-->
        <el-button class="button-new-tag" size="small" @click="showAr('jishu')">技术</el-button>
        <el-button class="button-new-tag" size="small" @click="showAr('2')">休闲</el-button>
        <el-button class="button-new-tag" size="small" @click="showAllAr">所有文章</el-button>
        <!--显示所有文章-->
        <el-row style="top: 20px;">
          <el-col :span="8" v-for="(article, key) in articles" class="cardboder">
              <el-card :body-style="{ padding: '2px' }">
                <div style="padding: 14px;">
                  <h3 v-text="article.ar_name"></h3></br>
                  <span v-text="article.ar_desc"></span>
                  <div class="bottom clearfix">
                    <time class="time">{{ article.timestamp | timeformat}}</time>
                    <el-button type="text" class="button" @click="showOneAr(article)">查看文章</el-button>
                  </div>
                </div>
              </el-card>
          </el-col>
        </el-row>
  </div>
</template>
<script>
// 引入moment.js第三方时间框架
var moment = require('moment');
// 状态管理
export default { 
  data() {
      return {
        tags: [
          { name: '技术', type: '' },
          { name: '休闲', type: 'gray' },
        ],
        currentDate: moment().locale('zh-cn').format("dddd, MMMM Do YYYY, h:mm:ss a"),
        articles: []
      }
    },
  mounted: function() {
    this.$nextTick(function (){
      this.showAllAr();
    });
  },
  filters: {
    timeformat: function (value){
      return moment(value).locale('zh-cn').format("dddd, MMMM Do YYYY, h:mm:ss a")
    }
  },
  methods: {
    // 显示想看类型的文章
    showAr: function(type) {
      this.$http.get('http://127.0.0.1:8000/api/articles/'+type).then(res=>{
        this.articles = [];
        this.articles = res.data.results;
        // console.log(res);
      });
      // console.log('submit!');
    },
    // 查看文章
    showOneAr: function(key) {
      console.log(key);
      this.$router.push({name: 'article', params: {article: key}});
    },
    // 显示所有文章
    showAllAr: function() {
      this.$http.get('http://127.0.0.1:8000/api/articles/').then(res=>{
        this.articles = res.data.results;
      });
      // console.log('submit!');
    }
  }
}
</script>

<style>

/*显示文章的CSS*/
.time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both;
  }
  .cardboder{
    position: relative;
    margin: 10px;
  }
  /*×××××××××××××××××××××××*/
</style>