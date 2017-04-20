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
          v-model="selectedSuite")
        v-btn(class="ml-4" primary) Run

    v-data-table(
      hide-actions
      class="mt-3 elevation-1"
      v-bind:headers="headers"
      v-model="runs")
      template(slot="headers" scope="props")
        span {{ props.item.text }}
      template(slot="items" scope="props")
        td {{ props.item.suite.name }}
        td(class="text-xs-right") {{ props.item.passRate }}
        td(class="text-xs-right" v-bind:class="{\
          'green--text': props.item.status === 'finished',\
          'orange--text': props.item.status === 'running' \
        }") {{ props.item.status }}
</template>

<script lang="coffee">
import { mapGetters } from 'vuex'

headers = [
  { text: 'Test suite name', left: true, value: 'suite.name' }
  { text: 'Pass rate', value: 'passRate' }
  { text: 'Status', value: 'status' }
]

getters = mapGetters
  runs: 'runs'
  suites: 'suites'
  selectedSuite: 'selectedSuite'

export default {
  computed: getters
  data: () =>
    headers: headers
}
</script>
