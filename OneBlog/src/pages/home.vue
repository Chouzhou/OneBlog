<template>
  <el-row class="content">
    <!--头部显示-->
    <el-col :span="24" class="header">
      <el-col :span="20" class="logo">
        <!--标题-->
				<span>My Little Blog</span>
      </el-col>

      <el-col :span="1" style="position: absolute; right: 130px;">
        <span><router-link to="/">主页</router-link></span>
      </el-col>
      <el-col :span="1" style="position: absolute; right: 90px;">
        <span><router-link to="/writeAr">写文章</router-link></span>
      </el-col>
              <!--下拉菜单-->
        <el-col :span="4" class="articleselect">
          <el-dropdown trigger="click">
            <span class="el-dropdown-link articleselect-inner"><img :src="this.sysUserAvatar" />文章分类<i class="el-icon-caret-bottom el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>技术</el-dropdown-item>
              <el-dropdown-item>休闲</el-dropdown-item>
            </el-dropdown-menu>
				  </el-dropdown>
        </el-col>
      </el-col>
    </el-col>
    <el-col :span="24" class="main">
			<!--<section class="content-container">
				<div class="grid-content bg-purple-light">
					<el-col :span="24" class="content-wrapper">
						<transition>
							<router-view></router-view>
						</transition>
					</el-col>
				</div>
			</section>-->
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
  left: 500px;
  padding-right: 500px;
  /*overflow: hidden;*/
}
.logo{
	font-size: 22px;
}
.content-container {
	background: #f1f2f7;
	position: absolute;
	right: 0px;
	top: 0px;
	bottom: 0px;
	left: 230px;
	overflow-y: scroll;
	padding: 20px;
}
.content-wrapper {
	background-color: #fff;
	box-sizing: border-box;
}
</style>