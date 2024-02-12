<template>
  <v-app id="inspire">
    <div class="text-xs-center">
    </div>

    <v-toolbar dark color="white">
      <v-spacer></v-spacer>
      <v-toolbar-title style="margin: 43%" class="red--text">Adicionar Pelada</v-toolbar-title>

    </v-toolbar>
    <v-container fluid fill-height>
      <v-row align-center justify-center>
        <v-col xs12 sm8 md4>
          <v-form v-model="valid">
            <v-text-field v-model="dados.name" :rules="nameRules" :counter="10" label="Name" required></v-text-field>
            <v-text-field v-model="dados.tempo_duracao" type="number" label="Tempo de Duração (min)" required></v-text-field>
            <v-select v-model="dados.tempos" label="Tempos" :items="['T1', 'T2']" required></v-select>
            <v-select v-model="dados.limite_gols" :items="[0, 1, 2, 3, 4, 5]" label="Limite de Gols" required></v-select>
            <v-select v-model="dados.qtd_jogadores" label="Quantidade de Jogadores" :items="[5, 6]" required></v-select>
            <v-select v-model="dados.tipo_sorteio"
              :items="[{ 'name': 'Ordem de Chegada', 'id': 'O' }, { 'name': 'Nível Tecnico', 'id': 'N' }]" item-text="name"
              item-value="id" label="Tipo de Sorteio" required></v-select>
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

import Swar from 'sweetalert2'

const endpointPelada = 'http://localhost:8000/api/peladas/'
export default {
  components: {},
  data: () => ({
    valid: false,
    select: null,
    alert: false,
    // sucess: 'Jogador cadastrado',
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
        configuracao: {
          tempos: this.dados.tempos,
          tempo_duracao: this.dados.tempo_duracao,
          limite_gols: this.dados.limite_gols,
          qtd_jogadores: this.dados.qtd_jogadores,
          tipo_sorteio: this.dados.tipo_sorteio
        },
        dono: sessionStorage.getItem('id')
      }
      axios
        .post(endpointPelada, data, { headers: authe.headers })
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
    }
  }
}
</script>
<style>
</style>
