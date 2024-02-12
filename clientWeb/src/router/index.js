import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '@/components/home/Index'
import Pelada from '@/components/Pelada/index'
import Login from '@/components/auth/components/main'
import PeladasPublicas from '@/components/Peladas-Publicas/index'
import AddJogador from '@/components/Pelada/form/add-player'
import Configuracao from '@/components/configuracao/index'
import NovaOrganizacao from '@/components/Home/form/add-organizacao'
// import EditarPelada from '@/components/Home/form/edit-pelada'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/peladas', component: PeladasPublicas, titulo: 'Peladas' },
    { path: '/auth/login', component: Login, titulo: 'Login' },
    { path: '/home', name: 'Home', component: Home, titulo: 'Home', props: true },
    { path: '/organizacao/new', name: 'NovaOrganizacao', component: NovaOrganizacao, titulo: 'NovaOrganizacao', props: true },
    // { path: '/pelada/edit', name: 'EditarPelada', component: EditarPelada, titulo: 'EditarPelada', props: true },
    { path: '/pelada/:id', name: 'Pelada', component: Pelada, titulo: 'Pelada', props: true },
    { path: '/pelada/:id/jogador-add', name: 'AddJogador', component: AddJogador, titulo: 'AddJogador', props: true },
    { path: '/:catchAll(.*)', redirect: '/peladas' },
    { path: '/configuracao', name: 'Configuracao', component: Configuracao, titulo: 'Configurcao' }
  ]
})
