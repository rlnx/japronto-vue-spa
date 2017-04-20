class Mutations
  prepareNewSuite: (suite) ->
    suite.modifying = false
    return suite

  addSuitesInternal: (state, suites) ->
    state.suites ||= []
    for suite in suites
      if suite?.id? and suite?.name and suite?.command
        state.suites.push @prepareNewSuite(suite)
    if state.suites.length > 0 and not state.selectedSuite
      state.selectedSuite = state.suites[0]

  startSettingSuites: (state) =>
    state.suitesLoading = true

  setSuites: (state, { suites }) =>
    state.suites = []
    @addSuitesInternal state, suites
    state.suitesLoading = false

  listSuitesError: (state, { message }) =>
    console.log "List suites error: #{message}"
    state.suitesLoading = false


  startAddingSuite: (state) =>
    state.suiteAppending = true

  addSuites: (state, { suites }) =>
    @addSuitesInternal state, suites
    state.suiteAppending = false

  addSuiteError: (state, { message }) =>
    console.log "Add suite error: #{message}"
    state.suiteAppending = false


  startModifyingSuite: (state, { suite }) =>
    suite?.modifying = true

  updateSuiteCommand: (state, { suite, command }) =>
    suite?.command = command
    suite?.modifying = false

  updateSuiteError: (state, { suite, message }) =>
    console.log "Modifying suite error: #{message}"
    suite?.modifying = false


export default new Mutations
