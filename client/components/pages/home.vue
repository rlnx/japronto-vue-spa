<template lang="pug">
  div
    h5 Test runs
    v-card
      v-container(fluid)
      v-row(class="pl-5 pr-5 pt-4")
        v-select(label="Test suite" v-bind:items="suites" item-text="name")
        v-btn(class="ml-4" primary) Run
</template>

<script lang="coffee">
import { mapGetters } from 'vuex'

export default {
  computed:
    mapGetters { suites: 'getSuites' }
}
</script>
