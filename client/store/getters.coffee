class Getters
  runs: (state) => state.runs
  suites: (state) => state.suites

  canRunSuite: (state) =>
    not state.runsLoading   and
    not state.suitesLoading and
    state.selectedSuite?

export default new Getters
