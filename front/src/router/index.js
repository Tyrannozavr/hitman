import VueRouter from 'vue-router'

export default new VueRouter({
    mode: 'history',
    routes: [
        {path: '/',
        component: () => import('@/pages/index-page')},
        {path: '/fight',
        component: () => import('@/pages/fight-page')},
        {path: '/statistic',
        component: () => import('@/pages/statistic-page')},
    ]
})