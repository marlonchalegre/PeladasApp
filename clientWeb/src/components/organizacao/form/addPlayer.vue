<template>
  <v-app id="inspire">
    <div class="text-xs-center">
    </div>

    <v-toolbar dark color="white">
      <v-spacer></v-spacer>
      <v-toolbar-title style="margin: 43%" class="red--text">Adicionar Jogador</v-toolbar-title>
    </v-toolbar>

    <v-container>
      <v-row align-center justify-center>
        <v-col xs12 sm8 md4>
          <v-form v-model="valid">
            <v-autocomplete v-model:search-input="search" :items="playersList" :loading="isLoading"
              @update:search="onInput" no-filter item-title="name" item-value="name" return-object />
          </v-form>
          <v-btn dark color="red" style="color:white" @click="postData()">
            Adicionar
          </v-btn>
        </v-col>
      </v-row>

      <v-data-table :headers="headers" :items="players">
        <template v-slot:item>
          <td>{{ item.id }}</td>
          <td>{{ item.nome }}</td>
          <td>
            <my-star v-bind:read-only=true v-bind:show-rating=false v-bind:star-size="20" active-color="red"
              v-model="item.rating"></my-star>
          </td>
          <td>{{ item.created_at | date }}</td>
          <td>{{ item.pelada }}</td>
          <td class="justify-center layout px-0">
            <v-btn @click="edit(item)" icon>
              <v-icon small>edit</v-icon>
            </v-btn>
            <v-btn @click="remove(item.id)" icon>

              <v-icon small>delete</v-icon>
            </v-btn>
          </td>
        </template>
      </v-data-table>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios'
import router from '../../../router/index'
import Star from 'vue-star-rating'
import _ from "lodash"
import { ref } from 'vue'

const endpointJogadores = 'api/user/list/'
const playersEndpoint = 'api/organizacao/'

export default {
  components: {
    "my-star": Star
  },
  data: () => ({
    players: [],
    playersList: [],
    valid: false,
    select: null,
    alert: false,
    search: ref(''),
    isLoading: ref(false),
    dados: {
      name: '',
      raiting: null,
    },
    headers: [
      { text: 'ID', value: 'id', align: 'left' },
      { text: 'Nome', value: 'nome', align: 'left' },
      { text: 'Avaliação', value: 'rating', align: 'left' },
      { text: 'Cadastrado em', value: 'created_at', align: 'left' },
      { text: 'Pelada', value: 'pelada' },
      { text: 'Actions', sortable: false, align: 'left' }
    ],
    nameRules: [
      v => !!v || 'Name this player required',
      v => v.length <= 10 || 'Name must be less than 10 characters'
    ],
    raitingRules: [
      v => !!v || 'Raiting is Required',
      v => v.valueOf() <= 5 || 'Raiting ultrapassou'
      // v => /.+@.+/.test(v) || 'E-mail must be valid'
    ]
  }),
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
  },
  props: ['id'],
  computed: {},
  methods: {
    onInput(val) {
      if (!val) return false

      // _.debounce(function (val) {
      console.log("(debounce) Searching for players...");
      this.isLoading.value = true;
      let searchQuery = encodeURI("?search=" + val); // URI encode the query so it is able to be fetched properly
      this.searchPlayers(searchQuery);
      // }, 250)
    },
    searchPlayers(params = "") {
      console.log("Searching for players...");
      this.axios
        .get(endpointJogadores + params)
        .then(response => {
          this.playersList = response.data.map(player => {
            return {
              id: player.id,
              name: player.username
            };
          });
          this.isLoading.value = false;
        })
        .catch(e => {
          console.error(e); // display error message
        });
    },
    postData() {
      const id = this.id;
      const user_id = this.search.id;

      console.log(this.search)
      const token_export = sessionStorage.getItem("token");
      const authe = {
        headers: {
          Authorization: 'Token ' + token_export
        }
      };
      axios.post(`api/pelada/${id}/jogador/${user_id}`, {}, { headers: authe.headers })
        .then((response) => {
          this.$swal({
            title: 'Sucesso',
            text: 'O jogador foi cadastrado',
            confirmButtonText: 'Ok!',
          });
          // router.push({
          //   path: '/pelada/' + id,
          // })
        }).catch(err => {
          this.$swal({
            title: 'Erro',
            text: 'Ocorreu um erro ao cadastrar o jogador',
            confirmButtonText: 'Ok!',
          });
        })
    },
  },
  watch: {
    search: _.debounce(function (query) {
      console.log("(debounce) Searching for players...");
      // debounce with a a value of 250 will allow this function to be every 250 milliseconds at most. So if the user is typing continually, it won't run until the user stops.
      this.searchPlayers(query);
    }, 250)
  },
}
</script>
<style>
</style>
