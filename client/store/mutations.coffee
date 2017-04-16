mutations =
  increment: (state) ->
    state.counter++
    console.log "counter = #{state.counter}"

export default mutations
