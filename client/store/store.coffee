import Vue  from 'vue'
import Vuex from 'vuex'

Vue.use Vuex

import actions   from './actions.coffee'
import mutations from './mutations.coffee'

state =
  counter: 0

export default new Vuex.Store {
  state
  actions
  mutations
}
