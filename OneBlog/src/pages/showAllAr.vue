<template>
    <div>
        <p>文章类型</p> 
<!--点击选择文章类型显示-->
        <el-button class="button-new-tag" size="small" v-on="showAr">技术</el-button>
        <el-button class="button-new-tag" size="small" v-on="showAr">休闲</el-button>
        <!--显示所有文章-->
        <el-row style="top: 20px;">
          <el-col :span="8" v-for="(o, index) in 2" :offset="index > 0 ? 2 : 0">
            <el-card :body-style="{ padding: '0px' }">
              <img src="#" class="image">
              <div style="padding: 14px;">
                <span>好吃的汉堡</span>
                <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
                  <el-button type="text" class="button" @click="showOneAr">查看文章</el-button>
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
// moment.locale(String);
export default { 
  data() {
      return {
        currentDate: moment().locale('zh-cn').format("dddd, MMMM Do YYYY, h:mm:ss a")
      }
    },
  methods: {
    // 显示想看类型的文章
    showAr() {
      console.log('submit!')
    },
    // 查看文章
    showOneAr() {
      console.log('submit!')
    }
  }
}
</script>