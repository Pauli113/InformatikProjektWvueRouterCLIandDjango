import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import InputPage from './components/InputPage.vue'
import MyCourses from './components/MyCourses.vue'


const routes = [
    //{path:'/courses'}
    {path:'/input',component:InputPage},
    {path:'/mycourses',component:MyCourses}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})






createApp(App).use(router).mount('#app')

