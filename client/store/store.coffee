import Vue  from 'vue'
import Vuex from 'vuex'

Vue.use Vuex

import actions   from './actions.coffee'
import getters   from './getters.coffee'
import mutations from './mutations.coffee'

state =
  suiteAppending: false
  suitesLoading: false
  runsLoading: false
  selectedSuite: null
  suites: [ ]
  runs: [ ]

# Format of the state child elements
# suite = { id, name, command, modifying }
# run   = { id, suiteId, suiteName, passRate, status  }

export default new Vuex.Store {
  state
  getters
  actions
  mutations
}
