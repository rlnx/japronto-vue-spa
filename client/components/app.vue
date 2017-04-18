<template lang="pug">
  v-app(top-fixed-toolbar left-fixed-sidebar)
    header
      v-toolbar(fixed)
        v-toolbar-side-icon(@click.native.stop="openSidebar" class="hidden-lg-and-up px-2")
        v-toolbar-title Test runner
    main
      v-sidebar(fixed class="white--text" v-model="sidebar")
        v-list(dense)
          v-subheader(inset) Folders
          v-list-tile(v-for="(item, i) in items", :to="item.href" avatar key="i")
            v-list-tile-avatar
              v-icon {{item.icon}}
            v-list-tile-content {{ item.title }}
      v-content
        v-container(fluid class="pa-3")
          router-view
</template>

<style lang="stylus">
  @import '../../node_modules/vuetify/src/stylus/main'
</style>

<script lang="coffee">
export default data: ->
  sidebar: false
  items: [
    href: '#home'
    title: 'Home'
    icon: 'home'
  ,
    href: '#suites'
    title: 'Suites'
    icon: 'extension'
  ]
  openSidebar: ->
    this.sidebar = !this.sidebar
</script>
