import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'
import InputPage from '@/components/InputPage.vue'
import MyCourses from '@/components/MyCourses.vue'
import LoginPage from '@/components/LoginPage.vue'
import '@fortawesome/fontawesome-free/js/all'



const routes = [
    {path:'/input',name:'Input', component: InputPage},
    {path:'/myCourses',name:'MyCourses', component: MyCourses},
    {path:'/login',name:'LoginPage', component: LoginPage}
]

const router = createRouter({
    history: createWebHistory(),
    routes:routes
})






createApp(App).use(router).mount('#app')

