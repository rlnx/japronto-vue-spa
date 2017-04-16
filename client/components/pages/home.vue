<template lang="pug">
  v-btn(primary dark @click.native="homeButtonClick") Home Test
</template>

<script lang="coffee">
export default data: ->
  homeButtonClick: ->
    this.$store.dispatch 'increment'
</script>
