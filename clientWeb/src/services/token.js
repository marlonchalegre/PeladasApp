import SessionStorage from './session-storage'
import { Token } from './resources'
import router from '../router/index'

export default {
  get token() {
    return SessionStorage.get('token')
  },
  set token(value) {
    SessionStorage.set('token', value)
  },
  get userName() {
    return SessionStorage.getUsername('username')
  },
  set userName(value) {
    SessionStorage.setUsername('username', value)
  },
  set userEmail(value) {
    SessionStorage.setUserEmail('email', value)
  },
  get userEmail() {
    return SessionStorage.getUserEmail('email')
  },
  set userId(value) {
    SessionStorage.setUserId('id', value)
  },
  get userId() {
    return SessionStorage.getUserId('id')
  },

  acessToken(username, password) {
    const err = ''
    return Token.acessToken(username, password)
      .then(response => {
        this.token = response.data.token
        this.userName = response.data.user_name
        this.userEmail = response.data.user_email
        this.userId = response.data.user_id
        router.push({ name: 'Home' })
      })
      .catch(responseErr => {})
  },
  getAuthorizationHeader() {
    return `Bearer ${this.token}`
  },
  isAuthenticated() {
    return !!this.token
  }
}
