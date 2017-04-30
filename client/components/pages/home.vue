<template lang="pug">
  div
    h5 Test runs

    v-card
      v-container(fluid)
      v-row(class="pl-5 pr-5 pt-4")
        v-select(
          label="Test suite"
          item-text="name"
          item-value="name"
          v-bind:items="suites"
          v-model="$store.state.selectedSuite")
        v-btn(
          primary class="ml-4"
          @click.native="runSuite"
          v-bind:disabled="!canRunSuite") Run

    div(class="pt-3")
    v-container(fluid v-if="$store.state.runsLoading")
      div(class="pt-5")
      div(class="text-xs-center")
        v-progress-circular(
          class="center"
          indeterminate
          v-bind:size="60"
          class="primary--text")

    v-data-table(
      v-else hide-actions
      class="elevation-1"
      v-bind:headers="headers"
      v-model="runs")
      template(slot="headers" scope="props")
        span {{ props.item.text }}
      template(slot="items" scope="props")
        td {{ props.item.suiteName }}
        td(class="text-xs-right") {{ props.item.passRate }}
        td(class="text-xs-right" v-bind:class="{\
          'green--text': props.item.status  === 'passed',  \
          'orange--text': props.item.status === 'running', \
          'red--text': props.item.status    === 'failed'   \
        }") {{ props.item.status }}
</template>

<script lang="coffee">
import { mapGetters } from 'vuex'

headers = [
  { text: 'Test suite name', left: true, value: 'suiteName' }
  { text: 'Pass rate', value: 'passRate' }
  { text: 'Status', value: 'status' }
]

export default {
  computed: mapGetters { 'runs', 'suites', 'canRunSuite' }
  data: () ->
    headers: headers

  methods:
    runSuite: ->
      selectedSuite = this.$store.state.selectedSuite
      this.$store.dispatch 'runSuite', selectedSuite

}
</script>
