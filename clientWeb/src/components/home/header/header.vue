
<template>
  <v-toolbar dark color="orange">
    <v-toolbar-title class="red--text">Peladas App</v-toolbar-title>
    <v-toolbar-items>
      <v-btn dark color="white" style="color:red">
        Jogadores
      </v-btn>
      <v-btn @click="logout()" dark color="white" style="color:red">
        Sair
      </v-btn>
    </v-toolbar-items>

  </v-toolbar>
</template>

<script>
import router from '../../../router/index'

export default {
  data: () => ({}),

  methods: {
    logout() {
      sessionStorage.removeItem("token");
      sessionStorage.removeItem("id");
      sessionStorage.removeItem("username");

      router.push({ path: '/auth/login' })
    },
    getImage() {
      const min = 550
      const max = 560

      return Math.floor(Math.random() * (max - min + 1)) + min
    }
  }
}
</script>

<style scoped>
</style>
