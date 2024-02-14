import { createRouter, createWebHashHistory } from 'vue-router'
import Home from 'components/home/Home.vue'
import Pelada from 'components/organizacao/Organizacao.vue'
import Login from 'components/auth/components/main.vue'
// import PeladasPublicas from 'components/Peladas-Publicas/index.vue'
// import AddJogador from 'components/Pelada/form/add-player.vue'
import Configuracao from 'components/configuracao/index.vue'
import NovaOrganizacao from 'components/Home/form/AddOrganizacao.vue'
// import EditarPelada from 'components/Home/form/edit-pelada'

import Token from '../services/token'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/auth/login', component: Login, titulo: 'Login' },
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
    // { path: '/pelada/:id/jogador-add', name: 'AddJogador', component: AddJogador, titulo: 'AddJogador', props: true },
    { path: '/configuracao', name: 'Configuracao', component: Configuracao, titulo: 'Configurcao' },
    { path: '/:catchAll(.*)', redirect: '/home' }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.path !== '/auth/login' && !Token.isAuthenticated()) {
    console.log(to)
    next({ path: '/auth/login' })
  } else {
    next()
  }
})

export default router
