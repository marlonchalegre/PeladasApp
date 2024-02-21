import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '~/src/components/home/Home.vue'
import Pelada from '~/src/components/organizacao/Organizacao.vue'
import Login from '~/src/components/auth/components/main.vue'
import NewUser from '~/src/components/auth/components/forms/NewUser.vue'
// import PeladasPublicas from '~/src/components/Peladas-Publicas/index.vue'
import AddPlayer from '~/src/components/organizacao/form/addPlayer.vue'
import Configuracao from '~/src/components/configuracao/index.vue'
import NovaOrganizacao from '~/src/components/Home/form/AddOrganizacao.vue'
// import EditarPelada from '~/src/components/Home/form/edit-pelada.vue'

import Token from '../services/token'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/auth/login', component: Login, titulo: 'Login' },
    { path: '/user/new', component: NewUser, titulo: 'NewUser' },
    { path: '/home', name: 'Home', component: Home, titulo: 'Home', props: true },
    {
      path: '/organizacao/new',
      name: 'NovaOrganizacao',
      component: NovaOrganizacao,
      titulo: 'NovaOrganizacao',
      props: true
    },
    // { path: '/pelada/edit', name: 'EditarPelada', component: EditarPelada, titulo: 'EditarPelada', props: true },
    { path: '/organizacao/:id', name: 'Pelada', component: Pelada, titulo: 'Pelada', props: true },
    { path: '/organizacao/:id/player/add', name: 'AddPlayer', component: AddPlayer, titulo: 'AddPlayer', props: true },
    { path: '/configuracao', name: 'Configuracao', component: Configuracao, titulo: 'Configurcao' },
    { path: '/:catchAll(.*)', redirect: '/home' }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.path !== '/auth/login' && to.path !== '/user/new' && !Token.isAuthenticated()) {
    console.log(to)
    next({ path: '/auth/login' })
  } else {
    next()
  }
})

export default router
