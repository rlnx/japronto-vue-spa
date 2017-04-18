import api from './../rest/api.coffee'

class Actions
  constructor: ->
    @listSuitesInternalThrottled = _.throttle(
      @listSuitesInternal, 500, { trailing: false }
    )

  listSuitesInternal: (commit) =>
    commit 'startSettingSuites'
    api.suites.list
      onSuccess: (r) => commit 'setSuites', { suites: r }
      onError: ({ message }) => commit 'listSuitesError', { message }

  listSuites: ({ commit }) =>
    @listSuitesInternalThrottled commit

  addSuite: ({ commit }, suite) =>
    commit 'startAddingSuite'
    unless suite?.name and suite?.command
      commit 'addSuiteError', { message: 'Test suite must have name and command.' }
    else
      api.suites.append suite,
        onSuccess: (r) => commit 'addSuites', { suites: [ r.suite ] }
        onError: ({ message }) => commit 'addSuiteError', { message }

  editSuiteCommand: ({ commit }, { suite, command }) =>
    commit 'startModifyingSuite', { suite }
    if command and suite?.command != command
      api.suites.update suite, { command },
        onSuccess: (r) => commit 'updateSuiteCommand', { suite, command }
        onError: ({ message }) => commit 'updateSuiteError', { suite, message }

export default new Actions
