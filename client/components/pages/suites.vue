<template lang="pug">
  div
    h5 Test suites
    v-expansion-panel
      v-expansion-panel-content
        div(slot="header") Add new test suite
        v-card
          v-card-text
            v-container(fluid)
              v-text-field(label="Tes suit name" v-model="newTestSuiteName")
              v-text-field(multi-line label="Launch command" v-model="newTestSuiteCommand")
              v-btn(
                light flat class="btn--light-flat-focused"
                @click.native="addSuite"
                v-bind:loading="$store.state.suiteAppending"
                v-bind:disabled="$store.state.suiteAppending || $store.state.suitesLoading"
              ) Add suite
    div(class="pt-3")
    v-container(fluid v-if="$store.state.suitesLoading")
      div(class="pt-5")
      div(class="text-xs-center")
        v-progress-circular(
          class="center"
          indeterminate
          v-bind:size="60"
          class="primary--text"
        )
    v-expansion-panel(v-else)
      v-expansion-panel-content(v-for="(suite, i) in suites" v-bind:key="i")
        div(slot="header")
          label {{suite.name}}
          code(class="ml-3") {{suite.command}}
        v-card
          v-card-text
            v-container(fluid)
              v-text-field(
                label="Command"
                v-bind:value="suite.command"
                @keyup.native.enter="editSuiteCommand(suite, $event)"
              )
</template>

<script lang="coffee">
import { mapGetters } from 'vuex'

export default {
  computed:
    mapGetters { suites: 'getSuites' }

  data: ->
    newTestSuiteName: null
    newTestSuiteCommand: null

  methods:
    addSuite: ->
      if this.$store.state.suitesLoading then return
      suite =
        name: this.newTestSuiteName
        command: this.newTestSuiteCommand
      this.newTestSuiteName = null
      this.newTestSuiteCommand = null
      this.$store.dispatch 'addSuite', suite

    editSuiteCommand: (suite, e) ->
      if suite.modifying then return
      newCommand = e.target?.value
      if newCommand and newCommand != suite.command
        this.$store.dispatch 'editSuiteCommand', { suite, command: newCommand }

  beforeRouteEnter: (route, redirect, next) ->
    next (vm) -> vm.$store.dispatch 'listSuites'
}
</script>
