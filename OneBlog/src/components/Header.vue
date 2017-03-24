<template>
  <el-row class="content">
    <!--头部显示-->
    <el-col :span="24" class="header">
      <el-col :span="20" class="logo">
        <!--标题-->
				<!--<span><router>My Little Blog<</span>-->
        <router-link to="/" tag="span">My Little Blog</router-link>
      </el-col>
    </el-col>
    <el-col :span="24" class="main">
      <template>
          <router-view></router-view>        
      </template>
		</el-col>
  </el-row>
</template>
<script>

export default { 
}
</script>

<style>
.content{
  position: absolute;
  top: 0px;
	bottom: 0px;
	width: 100%;
}
.header{
    position: absolute;
    height: 60px;
		line-height: 60px;
		background: #1F2D3D;
		color: #c0ccda;
}
.articleselect {
		text-align: right;
		padding-right: 20px;
}
.articleselect .articleselect-inner {
		color: #c0ccda;
		cursor: pointer;
}
.main{
  background: #324057;
	position: absolute;
	top: 110px;
	bottom: 0px;
  left: 450px;
  padding-right: 500px;
  /*overflow: hidden;*/
}
.logo{
	font-size: 22px;
}
.content-container {
	background: #f1f2f7;
	position: absolute;
  
}
.content-wrapper {
	background-color: #fff;
	/*box-sizing: border-box;*/
}
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