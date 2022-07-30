import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import InputPage from './components/InputPage.vue'


const routes = [
    //{path:'/courses'}
    {path:'/input',component:InputPage}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


createApp(App).use(router).mount('#app')

