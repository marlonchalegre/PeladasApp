import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import Token from './services/token'
import SessionStorage from './services/session-storage'
import router from './router/index'

Vue.use(Vuex)

const userName = window.sessionStorage.getItem('username')
const userEmail = window.sessionStorage.getItem('email')
const state = {
  user: {
    name: userName,
    email: userEmail
  }
}

const mutations = {}

const actions = {
  login(context, { username, password }) {
    Token.acessToken(username, password)
  }
}
export default new Vuex.Store({
  state,
  getters: {},
  mutations,
  actions
})
