import Vue from 'vue';
import axios from 'axios';

import interceptor from './interceptors'
// require('./interceptors')
export class Token {
  static acessToken(username,password){
    const headers = {
      'Content-Type': 'application/json',
    };
    return  axios.post('/api/login',{username,password},{headers:headers});
  }
}
const USER  = ''
