<template>
    <el-form ref="form" :model="form" label-position="top">
        <h2 style="left: 10px;">编辑文章</h2>
        <el-form-item label="名字" style="padding-right: 600px;">
            <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="内容" style="padding-right: 600px;">
            <el-input type="textarea" v-model="form.desc" :autosize="{ minRows: 2, maxRows: 4}"></el-input>
        </el-form-item>
        <el-form-item label="类型">
            <el-select v-model="form.region" placeholder="请选择文章类型">
            <el-option label="技术" value="jishu"></el-option>
            <el-option label="休闲" value="xiuxian"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button @click="onCancel">取消</el-button>
        </el-form-item>
    </el-form>
</template>
<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        }
      }
    },
    methods: {
      onSubmit() {
        this.$confirm('此操作将永久提交该文章, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '提交成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消提交'
          });          
        });
      },
      onCancel() {
          
      }
    }
  }
</script>
<style>
</style>