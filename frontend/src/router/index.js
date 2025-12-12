import Index from '@/views/index.vue'
import User from '@/views/user.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'home',
      component : Index
    },
    {
      path : '/user',
      name : 'user',
      component : User
    },
  ],
})

export default router
