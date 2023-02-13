import { createRouter, createWebHistory } from 'vue-router'
import StructGroupView from '../views/StructGroupView.vue'

import InfoView from '../views/InfoView.vue'
const routes = [
  {
    path: '/structure/:hierarchy(.*)',
    name: 'HomeView',
    components: {
      default: StructGroupView,
      info: InfoView,
      struct: StructGroupView,}
    },
    {
     path: '/',
     redirect: '/structure/'
    }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
