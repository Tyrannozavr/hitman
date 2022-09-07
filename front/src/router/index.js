import VueRouter from 'vue-router'

export default new VueRouter({
    mode: 'history',
    routes: [
        {path: '/',
         name: 'index',
        component: () => import('@/pages/index-page')},
        {path: '/fight',
         name: 'fight',
        component: () => import('@/pages/fight-page')},
        {path: '/statistic',
         name: 'statistic',
        component: () => import('@/pages/statistic-page')},
    ]
})