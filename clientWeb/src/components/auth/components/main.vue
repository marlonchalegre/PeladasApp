<template>
  <v-app id="inspire">
    <my-header></my-header>

    <v-content style="margin-top: 10%">
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="white">
                <v-toolbar-title dark color="red" style="color: red">Login Peladas</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <div v-if=!sigin>
                  <v-show>
                    error

                  </v-show>
                </div>
                <v-form>
                  <v-text-field prepend-icon="person" v-model="user.username" name="username" label="Login" type="text"
                    :rules="nameRules"></v-text-field>
                  <v-text-field id="password" prepend-icon="lock" v-model="user.password" name="password" label="Password"
                    :rules="passWordRules" type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn v-on:click.prevent="sigin" color="white" style="color: red">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>


  </v-app>
</template>

<script>
import axios from 'axios'
import Header from './header/header'

export default {
  components: {
    'my-header': Header
  },
  data() {
    return {
      user: {
        username: '',
        password: '',
      },
      nameRules: [
        v => !!v || 'Name this player required',
        v => v.length <= 10 || 'Name must be less than 10 characters'
      ],
      passWordRules: [
        v => !!v || 'PassWord Required'
      ],
      error: {
        error: false,
        message: ''
      },
      login_message: false,


    }
  },
  methods: {
    sigin() {
      this.$store.dispatch('login', this.user)
        .then((response) => {

        }).catch((respoonseErr) => {

        })

    },
  },
}
</script>

<style lang="css">
#inspire {
  margin-top: -68px;
}
</style>
