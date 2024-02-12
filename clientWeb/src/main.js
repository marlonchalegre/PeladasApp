// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import { createApp } from 'vue'

import App from './App.vue'
import router from './router'


import 'material-design-icons-iconfont/dist/material-design-icons.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from './store'
import StarRating from 'vue-star-rating'

import 'vuetify/dist/vuetify.min.css'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/lib/components'
import * as directives from 'vuetify/lib/directives'

__VUE_OPTIONS_API__ = true;

if (process.env.NODE_ENV !== 'production') {
  __VUE_PROD_DEVTOOLS__ = true;
} else {
  __VUE_PROD_DEVTOOLS__ = false;
}

const app = createApp(App)
const vuetify = createVuetify({
  ssr: true,
  components,
  directives
})

app.component('star-rating', StarRating)
app.use(VueAxios, axios)
app.use(vuetify)
app.use(store)
app.use(router)

app.config.productionTip = false

window.axios = {
  Accept: 'application/json',
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*'
}

app.mount('#app')
