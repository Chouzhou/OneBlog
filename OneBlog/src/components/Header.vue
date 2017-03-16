<template>
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
</template>
<script>

</script>
<style>
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
</style>