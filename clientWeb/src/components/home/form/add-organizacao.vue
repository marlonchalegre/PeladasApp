<template>
  <v-app id="inspire">
    <div class="text-xs-center">
    </div>

    <v-toolbar dark color="white">
      <v-spacer></v-spacer>
      <v-toolbar-title style="margin: 43%" class="red--text">Adicionar Organizacao</v-toolbar-title>

    </v-toolbar>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-form v-model="valid">
            <v-text-field v-model="dados.name" :rules="nameRules" :counter="10" label="Name" required></v-text-field>
            <v-file-input v-model="dados.image" :rules="[v => !!v || 'Imagem é obrigatória', v => validateImageSize(v)]"
              accept="image/*" label="Imagem" required></v-file-input>
          </v-form>
          <v-btn dark color="red" style="color:white" @click="postData()">
            Adicionar
          </v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>
<script>
import axios from 'axios'
import router from '../../../router/index'

import Swar from 'sweetalert2'

const endpointOrganizacao = '/api/organizacao/'
export default {
  components: {},
  data: () => ({
    valid: false,
    select: null,
    alert: false,
    items: [],
    dados: {
      name: ''
    },
    nameRules: [
      v => !!v || 'Nome da pelada é obrigatório',
      v => v.length <= 50 || 'Nome deve ser menor que 50 caracteres'
    ]
  }),
  created() { },
  computed: {},
  methods: {
    formatMinutesToTimeStr(minutes) {
      new Date(minutes * 60 * 1000).toISOString().substring(11, 19)
    },
    postData() {
      const token_export = sessionStorage.getItem('token')
      const authe = {
        headers: {
          Authorization: 'Token ' + token_export
        }
      }
      const data = {
        nome: this.dados.name,
        administrador: sessionStorage.getItem('id'),
        image: this.dados.image
      }
      axios
        .post(endpointOrganizacao, data, { headers: authe.headers })
        .then(response => {
          Swar({
            title: 'Sucesso',
            text: 'A pelada foi cadastrada',
            confirmButtonText: 'Ok!'
          })
          router.push({
            path: '/home'
          })
        })
        .catch(err => { })
    },
    validateImageSize(file) {
      if (file) {
        const image = new Image()
        image.src = URL.createObjectURL(file)
        return new Promise((resolve, reject) => {
          image.onload = () => {
            if (image.width <= 200 && image.height <= 100) {
              resolve(true)
            } else {
              reject('A imagem deve ter no máximo 200 x 100 pixels')
            }
          }
          image.onerror = () => {
            reject('Erro ao carregar a imagem')
          }
        })
      }
      return true
    },
  }
}
</script>
<style>
</style>
