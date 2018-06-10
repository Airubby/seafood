import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode:'hash',  //hash,history，history打包静态无法展示，不知道要怎么设置才行
  routes: [
    {
      path: '',
      component: (resolve) => require(['@/page/index'], resolve),
    },{
      path: '/',
      component: (resolve) => require(['@/page/index'], resolve),
    },{
      path: '/login',
      component: (resolve) => require(['@/page/login'], resolve),
    },{
      path: '/register',
      component: (resolve) => require(['@/page/register'], resolve),
    }

  ]
})


