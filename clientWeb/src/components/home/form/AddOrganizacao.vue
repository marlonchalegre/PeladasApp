<template>
  <v-app id="inspire">
    <div class="text-xs-center">
    </div>
    <v-toolbar dark color="white">
      <v-spacer></v-spacer>
      <v-toolbar-title style="margin: 43%" class="red--text">Adicionar Organização</v-toolbar-title>
    </v-toolbar>
    <v-container fluid fill-height>
      <v-row align-center justify-center>
        <v-col xs12 sm8 md4>
          <v-form v-model="valid">
            <v-text-field v-model="dados.name" :rules="nameRules" :counter="10" label="Name" required></v-text-field>
            <v-file-input accept="image/*" prepend-icon="camera" v-model="dados.image"></v-file-input>
          </v-form>
          <v-btn dark color="red" style="color:white" @click="postData()">
            Adicionar
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>
<script>
import axios from 'axios'
import router from '../../../router/index'

const endpointOrganizacao = '/api/organizacao/'
export default {
  components: {},
  data: () => ({
    valid: false,
    select: null,
    alert: false,
    items: [],
    dados: {},
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
    toBase64(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = (error) => reject(error);
      });
    },
    async postData() {
      const token_export = sessionStorage.getItem('token')

      let brasao = await this.toBase64(this.dados.image[0])

      let data = {
        nome: this.dados.name,
        administrador: sessionStorage.getItem('id'),
        brasao: brasao
      }

      const headers = {
        Authorization: 'Token ' + token_export
      }

      axios
        .post(endpointOrganizacao, data, { headers: headers })
        .then(response => {
          URL.revokeObjectURL(this.dados.image);
          this.$swal({
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
    //TODO validate brasao size
  }
}
</script>
<style>
</style>
