import { createStore } from 'vuex'
import Token from './token'

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
export default createStore({
  state,
  getters: {},
  mutations,
  actions
})
