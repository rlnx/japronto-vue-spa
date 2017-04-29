import Vue       from 'vue'
import Vuetify   from 'vuetify'
import VueRouter from 'vue-router'
import { sync }  from 'vuex-router-sync'

Vue.use Vuetify
Vue.use VueRouter

import App        from './components/app.vue'
import HomePage   from './components/pages/home.vue'
import SuitesPage from './components/pages/suites.vue'
import vStore     from './store/store.coffee'

routes = [
  { path: '/',       component: HomePage   }
  { name: 'home', path: '/home',   component: HomePage   }
  { name: 'suites', path: '/suites', component: SuitesPage }
]
vRouter = new VueRouter { history: false, routes }

sync vStore, vRouter

app = new Vue
  el:     '#app'
  router: vRouter
  store:  vStore
  render: (h) => h(App)

app.$store.dispatch 'listSuites'
app.$store.dispatch 'listRuns'

listRuns = () => app.$store.dispatch 'listRunsInBackground'
setInterval listRuns, 5000
