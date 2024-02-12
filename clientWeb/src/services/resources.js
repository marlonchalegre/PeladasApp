import axios from 'axios';

export class Token {
  static acessToken(username,password){
    const headers = {
      'Content-Type': 'application/json',
    };
    return  axios.post('/api/login',{username,password},{headers:headers});
  }
}
