<template>
  <div id="app">
    <img id="banner" src="./assets/america_banner.jpg">
    <conversation></conversation>
  </div>
</template>

<script>
import Conversation from './components/Conversation'

export default {
  name: 'app',
  components: {
    Conversation
  }
}
</script>

<style>
#banner {
  max-height: 100px;
  width: auto;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
