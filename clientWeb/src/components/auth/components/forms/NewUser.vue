<template>
  <div class="text-xs-center">
  </div>

  <v-toolbar dark color="white">
    <v-spacer></v-spacer>
    <v-toolbar-title style="margin: 43%" class="red--text">Novo Usuário</v-toolbar-title>
  </v-toolbar>

  <v-container fluid fill-height>
    <v-row align-center justify-center>
      <v-col xs12 sm8 md4>
        <v-form v-model="isFormValid" @submit.prevent="submitForm">
          <v-text-field v-model="user.username" label="Username"></v-text-field>
          <v-text-field v-model="user.email" label="Email" :rules="emailRule"></v-text-field>
          <v-text-field v-model="user.password" label="Password" type="password" :rules="passwordRule"></v-text-field>
          <v-btn type="submit" color="primary" :disabled="!isFormValid">Create User</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
import token from '../../../../services/token';

const endpointUser = 'api/user/new'

export default {
  data: () => ({
    isFormValid: false,
    user: {
      username: '',
      email: '',
      password: ''
    },
    emailRule: [
      v => !!v || 'Email is required',
      v => /.+@.+\..+/.test(v) || 'Email must be valid'
    ],
    passwordRule: [
      v => !!v || 'Password is required',
      v => v.length >= 4 || 'Password must be at least 4 characters long'
    ]
  }),
  methods: {
    submitForm() {
      axios
        .post(endpointUser, this.user)
        .then(response => {
          URL.revokeObjectURL(this.dados.image);
          this.$swal({
            title: 'Sucesso',
            text: 'Usuário criado com sucesso',
            confirmButtonText: 'Ok!'
          })
          router.push({
            path: '/auth/login'
          })
        })
        .catch(err => { })
    }
  }
};
</script>
