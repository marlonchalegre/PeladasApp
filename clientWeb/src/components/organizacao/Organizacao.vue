<template>
  <Header></Header>
  <v-container>

    <v-row no-gutters>
      <v-col>
        <div>
          <h1>Detalhes da suas Peladas</h1>
        </div>
      </v-col>
      <v-col>
        <v-btn dark color="secondary" style="color:red" class="pa-2 ma-2">
          Criar nova pelada
        </v-btn>
        <v-btn dark color="secondary" @click="goToAddPlayer()" style="color:red" class="pa-2 ma-2">
          Jogadores
        </v-btn>
      </v-col>
    </v-row>

    <v-col>
      <div>
        <h2>Próxima pelada</h2>
      </div>
      <v-col cols="6">
        <v-card>
          <v-card-text>
            <div>
              <h3>Local</h3>
              <p>Local</p>

              <h3>Local</h3>
              <p>data</p>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn icon>
              <v-icon>
                visibility
              </v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>edit</v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>delete</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <div>
        <h2>Últimas 10 peladas</h2>
      </div>
      <v-row no-gutters>

        <v-col>
          <v-card>
            <v-card-text>
              <div>
                <h3>Local</h3>
                <p>Local</p>

                <h3>Local</h3>
                <p>data</p>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card>
            <v-card-text>
              <div>
                <h3>Local</h3>
                <p>Local</p>

                <h3>Local</h3>
                <p>data</p>
              </div>
            </v-card-text>
          </v-card>
        </v-col>

        <v-responsive width="100%"></v-responsive>

        <v-col>
          <v-card>
            <v-card-text>
              <div>
                <h3>Local</h3>
                <p>Local</p>

                <h3>Local</h3>
                <p>data</p>
              </div>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col>
          <v-card>
            <v-card-text>
              <div>
                <h3>Local</h3>
                <p>Local</p>

                <h3>Local</h3>
                <p>data</p>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
  </v-container>
</template>
<script>

import Header from '../home/header/header.vue'
import axios from 'axios'
import router from '../../router/index'

const playersEndpoint = 'api/organizacao/'

export default {
  components: {
    Header
  },
  props: ['id'],
  computed: {},
  data() {
    return {
      pelada: {}
    }
  },
  methods: {
    goToAddPlayer() {
      router.push({
        name: 'AddPlayer',
        params: {
          id: this.id
        }
      })
    }
  },
  filters: {
    date(v) {
      const date = new Date(v)
      const d = date.getDate()
      const m = date.getMonth() + 1
      const y = date.getFullYear()
      return `${d < 10 ? '0' + d : d}/${m < 10 ? '0' + m : m}/${y}`
    }
  },
  mounted() {
    const token_export = sessionStorage.getItem('token')
    let authe = {
      headers: {
        Authorization: 'Token ' + token_export
      }
    }
    axios.get(`${playersEndpoint}${this.id}`, { headers: authe.headers }).then(response => {
      this.players = response.data.jogadores
    })
  }
}
</script>
