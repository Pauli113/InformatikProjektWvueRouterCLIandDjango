import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'


import App from './App.vue'
import InputPage from '@/components/InputPage.vue'
import MyCourses from '@/components/MyCourses.vue'


const routes = [
    {path:'/input',name:'Input', component: InputPage},
    {path:'/allCourses',name:'MyCourses', component: MyCourses}
]

const router = createRouter({
    history: createWebHistory(),
    routes:routes
})




createApp(App).use(router).mount('#app')

