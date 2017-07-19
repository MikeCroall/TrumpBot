<template>
  <div id="app">
    <h1>Chat to TrumpBot</h1>
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
  color: #ffffff;
  margin-top: 60px;
}
html {
  height: 100%;
}
body {
    background-image: url('./assets/america_banner.jpg');
    height: 100%;
    /* Center and scale the image nicely */
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

h1 {
    background-color: black;
    margin-left: 20%;
    margin-right: 20%;
    padding-top: 10px;
    padding-bottom: 10px;
    
}
</style>
