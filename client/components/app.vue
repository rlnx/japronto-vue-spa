<template lang="pug">
  v-app(top-fixed-toolbar)
    header
      v-toolbar(fixed)
        v-toolbar-title Test runner
    main
      v-content
        v-container(fluid class="pa-3")
          router-view
    v-bottom-nav(fixed shift value="true")
      v-btn(flat dark @click.native="navigate('home')" v-bind:value="routerName === 'home'")
        span Runs
        v-icon directions_run
      v-btn(flat dark @click.native="navigate('suites')" v-bind:value="routerName === 'suites'")
        span Suites
        v-icon list
</template>

<style lang="stylus">
  @import '../../node_modules/vuetify/src/stylus/main'
</style>

<script lang="coffee">
export default {
  computed:
    routerName: () -> this.$store.state.route.name
  methods:
    navigate: (path) -> this.$router.push { path }
}
</script>
