import Vue from 'vue'
import Router from 'vue-router'
import home from '@/pages/views'
import writeAr from '@/pages/writeArticle'
import showAllAr from '@/pages/showAllAr'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      children: [
        {
          path: 'writeAr',
          name: 'writeAr',
          component: writeAr
        },{
          path: 'showAllAr',
          name: 'showAllAr',
          component: showAllAr

        }
      ]
    }
  ]
})
