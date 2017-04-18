import Vue  from 'vue'
import Vuex from 'vuex'

Vue.use Vuex

import actions   from './actions.coffee'
import getters   from './getters.coffee'
import mutations from './mutations.coffee'

state =
  suiteAppending: false
  suitesLoading: false
  suites: [ ]

export default new Vuex.Store {
  state
  getters
  actions
  mutations
}
