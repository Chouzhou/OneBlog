<template>
  <div class="container">
    <!--头部信息-->
    <div class="header">
      <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <!--<el-menu-item index="1">首页</el-menu-item>
        <el-menu-item index="3">写文章</a></el-menu-item>-->
        <el-submenu index="2" class="myInfo" style="text-align: right;"> 
          <template slot="title">{{ name }}</template>
          <el-menu-item index="2-1">个人资料</el-menu-item>
          <el-menu-item index="2-2">所写文章</el-menu-item>
          <!--<el-menu-item index="2-3">选项3</el-menu-item>-->
        </el-submenu>
      </el-menu>
    </div>
    <div class="line"></div>
    <!--侧边栏-->
    <div class="leftmenu"> 
      <el-row class="tac">
        <el-col :span="30">         
          <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" theme="dark">
            <el-submenu index="1">
              <template slot="title"><i class="el-icon-home"></i>首頁</template>
              <el-menu-item-group>
                <template slot="title">分组一</template>
                <el-menu-item index="1-1">选项1</el-menu-item>
                <el-menu-item index="1-2">选项2</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group title="分组2">
                <el-menu-item index="1-3">选项3</el-menu-item>
              </el-menu-item-group>
              <el-submenu index="1-4">
                <template slot="title">写文章</template>
                <el-menu-item index="1-4-1">选项1</el-menu-item>
              </el-submenu>
            </el-submenu>
            <el-menu-item index="2"><i class="el-icon-edit"></i>首頁</el-menu-item>
            <el-menu-item index="2"><i class="el-icon-edit"></i>写文章</el-menu-item>
            <!--<el-menu-item index="3"><i class="el-icon-setting"></i>导航三</el-menu-item>-->
          </el-menu>
        </el-col>       
      </el-row>
    </div>
    <!--显示首页信息-->
    <div class="main">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>活动管理</el-breadcrumb-item>
        <el-breadcrumb-item>活动列表</el-breadcrumb-item>
        <el-breadcrumb-item>活动详情</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
  </div>
</template>
<script>
export default {
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        name: 'Jack'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>
<style>
  .header{
    position:relative;
  }
  .myInfo {
      text-align: right;
  }
  .leftmenu{
    background: #324057;
		position: absolute;
		top: 60px;
		bottom: 0px;
    width: 200px;
		overflow: hidden;
    aside {
				width: 230px;
			}
  }
  /*主体部分*/
  .main {
    position: relative;
    top: 10px;
    left: 205px;

  }
</style>