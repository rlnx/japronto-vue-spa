import api from './../rest/api.coffee'

class Actions
  constructor: ->
    @listSuitesInternalThrottled = @throttle @listSuitesInternal
    @listRunsInternalThrottled   = @throttle @listRunsInternal

  throttle: (func) ->
    _.throttle func, 500, { trailing: false }

  listSuitesInternal: (commit) =>
    commit 'startSettingSuites'
    api.suites.list
      onSuccess: (suites) => commit 'setSuites', { suites }
      onError: ({ message }) => commit 'listSuitesError', { message }

  listRunsInternal: (commit, disableIndicator) =>
    unless disableIndicator
      commit 'startSettingRuns'
    api.runs.list
      onSuccess: (runs) => commit 'setRuns', { runs }
      onError: ({ message }) => commit 'listRunsError', { message }

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

  runSuite: ({ commit }, suite) =>
    api.runs.start suite,
      onSuccess: (run) => commit 'addRun', { run }

  listRuns: ({ commit }) =>
    @listRunsInternal commit

  listRunsInBackground: ({ commit }) =>
    @listRunsInternal commit, true

export default new Actions
