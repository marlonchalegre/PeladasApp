<template>
  <v-app id="inspire">
    <header-user></header-user>
    <v-content>
      <div style="margin-top: 5%">
        <h3>Seja Bem vindo: <span>{{ user }}</span></h3>
        <h3>email: {{ email }} </h3>
      </div>
      <div style="margin-top: 5%">
        <h2>Minhas Peladas</h2>
      </div>
      <v-container fluid grid-list-md fill-height>
        <v-layout row wrap>
          <v-flex xs12 sm4 md5 v-for="pelada of peladaUser" :key="pelada.nome">
            <v-card hover>
              <v-toolbar dark color="white">
                <v-toolbar-title dark color="red" style="color: red">Nome-Pelada: {{ pelada.nome }} </v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-media @click="peladaId(pelada.id)"
                src="https://conteudo.imguol.com.br/c/esporte/6c/2017/09/06/neymar-e-mbappe-se-encontram-pela-primeira-vez-em-treino-do-psg-1504716753721_615x300.jpg"
                height="200px">
              </v-card-media>
              <v-card-text>
                <span class="headline black--text">Id: {{ pelada.id }}</span>
              </v-card-text>
              <v-card-text>
                <span class="headline black--text">Dono: {{ pelada.dono }}</span>
              </v-card-text>
              <v-card-text>
                <span class=" headline black--text">Limite de Gols: {{ pelada.configuracao.limite_gols }} </span>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon @click="peladaId(pelada.id)">
                    visibility
                  </v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon @click="edit(pelada.id)">edit</v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon @click="remove(pelada.id)">delete</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>

          </v-flex>
          <v-layout row wrap>
          </v-layout>
        </v-layout>
        <v-flex xs12 sm12 md6>
          <v-btn dark fab bottom right color="red">
            <v-icon @click="criarPelada()">
              add
            </v-icon>
          </v-btn>
        </v-flex>
      </v-container>
    </v-content>
  </v-app>
</template>

<style scoped>
#inspire {
  height: 1220px;
}
</style>

<script>
import axios from 'axios'
import token from '../../services/token'
import Header from './header/header'
import store from '@/store'
import { mapState } from 'vuex'
import router from '../../router/index'

import Swar from 'sweetalert2'

const endpoint = 'api/user-peladas/'
const endpointPelada = 'api/pelada/'

export default {
  components: {
    'header-user': Header
  },
  data() {
    return {
      peladaUser: [],
      pelada: '',
      peladaUserId: [],
      cards: [
        {
          title: 'Pre-fab homes',
          src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
          flex: 12
        }
      ]
    }
  },
  computed: {
    ...mapState({
      user: state => state.user.name,
      email: state => state.user.email
    })
  },
  methods: {
    criarPelada() {
      router.push({
        path: '/organizacao/new'
      })
    },
    peladaId(id) {
      router.push({
        path: `/pelada/` + id
      })
    },
    edit(item) {
      alert(`Edit ${item.nome}`)
    },
    remove(id) {
      Swar({
        title: 'Danger',
        text: 'Tem certeza que quer remover?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Ok!',
        cancelButtonText: 'No, keep it'
      }).then(result => {
        if (result.value) {
          const endpointDelete = endpointPelada + id
          const token_export = sessionStorage.getItem('token')
          let auth = {
            headers: {
              Authorization: 'Token ' + token_export
            }
          }
          axios.delete(endpointDelete, { headers: auth.headers })
          Swar('Pelada removida!', '', 'success')
        } else if (result.dismiss === Swar.DismissReason.cancel) {
          Swar('Operação cancelada', '', 'error')
        }
      })
    }
  },
  mounted() {
    const token_export = sessionStorage.getItem('token')
    let authe = {
      headers: {
        Authorization: 'Token ' + token_export
      }
    }
    axios.get(endpoint, { headers: authe.headers }).then(response => {
      this.peladaUser = response.data
    })
  },

  created() { }
}
</script>
