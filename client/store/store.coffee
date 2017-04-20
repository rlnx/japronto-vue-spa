import Vue  from 'vue'
import Vuex from 'vuex'

Vue.use Vuex

import actions   from './actions.coffee'
import getters   from './getters.coffee'
import mutations from './mutations.coffee'

state =
  suiteAppending: false
  suitesLoading: false
  selectedSuite: null
  suites: [ ]
  runs: [
    suite:
      name: 'Example'
      command: 'python3 run-example.py'
    timestamp: new Date
    passRate: '10/10'
    status: 'finished'
  ]

# Format of the state child elements
# suite = { id, name, command, modifying }
# run   = { id, suite, passRate, status  }

export default new Vuex.Store {
  state
  getters
  actions
  mutations
}
