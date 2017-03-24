import Vue from 'vue'
import Router from 'vue-router'
import home from '@/pages/home'
// import writeAr from '@/pages/writeArticle'
import article from '@/pages/article'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
    },
    {
      path: '/article/:article',
      name: 'article',
      component: article
    }
  ]
})
