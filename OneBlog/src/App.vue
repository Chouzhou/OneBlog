<template>
  <div id="app">
		<index></index>
  </div>
</template>

<script>
import index from './components/Header'
export default {
  name: 'app',
	components: {
		index: index
	}
}
</script>

<style>
  body {
		margin: 0px;
		padding: 0px;
		/*background: url(assets/bg1.jpg) center !important;
		background-size: cover;*/
		/*background: #1F2D3D;*/
		font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, SimSun, sans-serif;
		font-size: 14px;
		-webkit-font-smoothing: antialiased;
	}
	
	#app {
		position: absolute;
		top: 0px;
		bottom: 0px;
		width: 100%;
	}
</style>
