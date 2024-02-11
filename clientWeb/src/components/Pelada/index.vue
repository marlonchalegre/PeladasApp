<template>
  <v-app id="inspire">
    <my-header></my-header>

    <div style="margin-top: 5%">
      <h1>Detalhes da Sua Pelada</h1>
      <h2>Nome: {{ peladaUserId.nome }}</h2>
    </div>

    <h1>Jogadores Da sua pelada</h1>

    <v-container>
      <v-data-table :headers="headers" :items="peladaUserId.jogadores">
        <template slot="items" slot-scope="props">
          <td>{{ props.item.id }}</td>
          <td>{{ props.item.nome }}</td>
          <td>
            <my-star v-bind:read-only=true v-bind:show-rating=false v-bind:star-size="20" active-color="red"
              v-model="props.item.rating"></my-star>
          </td>
          <td>{{ props.item.created_at | date }}</td>
          <td>{{ props.item.pelada }}</td>
          <td class="justify-center layout px-0">
            <v-btn @click="edit(props.item)" icon>
              <v-icon small>edit</v-icon>
            </v-btn>
            <v-btn @click="remove(props.item.id)" icon>

              <v-icon small>delete</v-icon>
            </v-btn>
          </td>
        </template>
      </v-data-table>
    </v-container>

    <v-layout row wrap>
      <v-flex xs12 sm12 md6>
        <v-btn absolute dark fab bottom right color="red">
          <v-icon @click="createdPlayer()">
            add
          </v-icon>
        </v-btn>
      </v-flex>
    </v-layout>
  </v-app>
</template>
<script>
import response from './form/add-player'

import Header from '../home/header/header'
import axios from 'axios'
import router from '../../router/index'
import Star from 'vue-star-rating'

import Swar from 'sweetalert2'

const endpoint = 'api/user-peladas/'

const endpointPelada = 'api/pelada/'
export default {
  components: {
    'my-header': Header,
    'my-star': Star
  },
  props: ['id'],
  computed: {
    getIdRouter: function () {
      if (this.id != null) {
        return this.id
      }
    }
  },
  data() {
    return {
      sucess_data: response,
      peladaUserId: [],
      headers: [
        { text: 'ID', value: 'id', align: 'left' },
        { text: 'Nome', value: 'nome', align: 'left' },
        { text: 'Avaliação', value: 'rating', align: 'left' },
        { text: 'Cadastrado em', value: 'created_at', align: 'left' },
        { text: 'Pelada', value: 'pelada' },
        { text: 'Actions', sortable: false, align: 'left' }
      ],
      pelada: {}
    }
  },
  methods: {
    createdPlayer() {
      const id = this.peladaUserId.id
      router.push({
        path: '/pelada/' + id + '/jogador-add'
      })
    },
    edit(item) {
      alert(`Edit ${item.nome}`)
    },
    remove(item) {
      Swar({
        title: 'Danger',
        text: 'Tem certeza que quer cancelar?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Ok!',
        cancelButtonText: 'No, keep it'
      }).then(result => {
        if (result.value) {
          Swar('Deleted!', 'Your imaginary file has been deleted.', 'success')
        } else if (result.dismiss === Swar.DismissReason.cancel) {
          Swar('Cancelled', 'Your imaginary file is safe :)', 'error')
        }
      })
      const endpointDelete = 'api/jogador/' + item
      const token_export = sessionStorage.getItem('token')
      let authe = {
        headers: {
          Authorization: 'Token ' + token_export
        }
      }
      axios.delete(endpointDelete, { headers: authe.headers })
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
  created() {
    // const id = sessionStorage.getItem("id");
    const token_export = sessionStorage.getItem('token')
    let authe = {
      headers: {
        Authorization: 'Token ' + token_export
      }
    }
    axios.get(`${endpointPelada}${this.getIdRouter}`, { headers: authe.headers }).then(response => {
      this.peladaUserId = response.data
    })
  }
}
</script>
