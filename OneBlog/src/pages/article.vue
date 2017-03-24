<template>
    <div id="vArticle">
        <article element-loading-text="加载中" class="article_wrap article">
          <header>
              <div class="home_title">{{ article.ar_name }}</div>
            <div>
              <p class="home_creatAt">发表时间：{{ article.timestamp | timeformat }}</p>
            </div>
          </header>
          <section class="home_main">{{ article.ar_body }}</section>
        </article>
    </div>
    
    

</template>
<script>
// 引入moment.js第三方时间框架
var moment = require('moment');
  export default {
    data() {
      return {
        article: []
      }
    },
    mounted: function() {
      this.$nextTick(function (){
        this.getId();
      });
    },
    filters: {
      timeformat: function (value){
        return moment(value).locale('zh-cn').format("M.D.YYYY")
      }
    },
    methods: {
      getId() {
        this.article = this.$route.params.article;
      }
    },
    
  }
</script>
<style>
article{
  margin:auto;
  /*margin-bottom:1rem;*/
}
.home_title{
  font-size: 3rem;
  font-weight: 400;
  color:#404040;
  padding:1rem 0;
}
.home_creatAt{
  font-family: "Comic Sans MS", curslve, sans-serif;
  padding:0.6rem 0;
  font-size: 1.8rem;
  color:#7f8c8d;
}
.home_main{
  font-size: 1.6rem;
  /*color:#34495e;*/
  line-height: 1.6em;
  padding:1rem 0;
}
@media screen and (max-width:786px){
  .home_title{
    font-size: 2.2rem;
  }
  .home_creatAt{
    font-size: 1.6rem;
  }
}
@media screen and (max-width:480px){
  .home_main{
    font-size:1.4rem;
    line-height: 1.6em;
  }
}
</style>

