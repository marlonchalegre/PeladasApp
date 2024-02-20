<template>
  <Header></Header>
  <v-container>
    <div style="margin-top: 5%">
      <h2>Meus Grupos</h2>
    </div>
    <v-container fluid grid-list-md fill-height>
      <v-row row wrap>
        <v-col xs12 sm4 md5 v-for="organizacao of organizacaoUser" :key="organizacao.id">
          <v-card hover>
            <v-toolbar dark color="white">
              <v-toolbar-title dark color="red" style="color: red">Grupo: {{ organizacao.nome }} </v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <img @click="organizacaoId(organizacao.id)" :src="organizacao.brasao" height="200px">
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon @click="organizacaoId(organizacao.id)">
                  visibility
                </v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon @click="edit(organizacao.id)">edit</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon @click="remove(organizacao.id)">delete</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>

        </v-col>
        <v-row row wrap>
        </v-row>
      </v-row>
      <v-col xs12 sm12 md6>
        <v-btn dark fab bottom right color="red">
          <v-icon @click="criarOrganizacao()">
            add
          </v-icon>
        </v-btn>
      </v-col>
    </v-container>
  </v-container>
</template>

<style scoped>
#inspire {
  height: 1220px;
}
</style>

<script>
import axios from 'axios'
import Header from './header/header.vue'
import { mapState } from 'vuex'
import router from '../../router/index'

const endpoint = 'api/organizacao/list'
const endpointOrganizacao = 'api/organizacao/'

export default {
  components: {
    Header
  },
  data() {
    return {
      organizacaoUser: [],
      organizacao: '',
      organizacaoUserId: [],
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
    criarOrganizacao() {
      router.push({
        path: '/organizacao/new'
      })
    },
    organizacaoId(id) {
      router.push({
        path: `/organizacao/` + id
      })
    },
    edit(item) {
      alert(`Edit ${item.nome}`)
    },
    remove(id) {
      this.$swal({
        title: 'Danger',
        text: 'Tem certeza que quer remover?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Ok!',
        cancelButtonText: 'No, keep it'
      }).then(result => {
        if (result.value) {
          const endpointDelete = endpointOrganizacao + id
          const token_export = sessionStorage.getItem('token')
          let auth = {
            headers: {
              Authorization: 'Token ' + token_export
            }
          }
          axios.delete(endpointDelete, { headers: auth.headers })
          this.$swal('Pelada removida!', '', 'success')
        } else if (result.dismiss === this.$swal.DismissReason.cancel) {
          this.$swal('Operação cancelada', '', 'error')
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
      this.organizacaoUser = response.data
    })
  },

  created() { }
}
</script>
