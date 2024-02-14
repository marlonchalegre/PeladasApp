<template>
  <Header></Header>
  <v-app id="inspire">
    <div style="margin-top: 5%">
      <h1>Detalhes da Sua Pelada</h1>
    </div>
    <v-container>
      <v-row justify="space-between">
        <v-btn fab dark right color="primary">
          Criar nova pelada
        </v-btn>
        <v-btn fab dark right color="primary">
          Gerenciar jogadores
        </v-btn>
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
                  <v-icon >
                    visibility
                  </v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon >edit</v-icon>
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


    <!-- <v-container>
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
    </v-container> -->

    <!-- <v-row row wrap>
      <v-col xs12 sm12 md6>
        <v-btn absolute dark fab bottom right color="red">
          <v-icon @click="createdPlayer()">
            add
          </v-icon>
        </v-btn>
      </v-col>
    </v-row> -->
  </v-app>
</template>
<script>
import response from './form/add-player'

import Header from '../home/header/header.vue'
import axios from 'axios'
import router from '../../router/index'
import Star from 'vue-star-rating'

const endpointOrganizacao = 'api/organizacao/'

export default {
  components: {
    Header,
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
      this.$swal({
        title: 'Danger',
        text: 'Tem certeza que quer cancelar?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Ok!',
        cancelButtonText: 'No, keep it'
      }).then(result => {
        if (result.value) {
          this.$swal('Deleted!', 'Your imaginary file has been deleted.', 'success')
        } else if (result.dismiss === this.$swal.DismissReason.cancel) {
          this.$swal('Cancelled', 'Your imaginary file is safe :)', 'error')
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
    axios.get(`${endpointOrganizacao}${this.getIdRouter}`, { headers: authe.headers }).then(response => {
      this.peladaUserId = response.data
    })
  }
}
</script>
