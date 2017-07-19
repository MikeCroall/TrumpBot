<template>
  <div id="app">
    <div class="header">
      <h1>Chat to TrumpBot</h1>
      <p>
        Created by <a href="https://ohmgeek.co.uk">Ryan Collins</a> and <a href="http://mikecroall.me">Mike Croall</a>
      </p>
    </div>

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
    background-repeat: repeat-y;
    background-size: cover;
}

.header {
    background-color: black;
    margin-top: -30px;
    margin-left: 20%;
    margin-right: 20%;
    padding-top: 10px;
    padding-bottom: 10px;

}
a {
  color: white;

}
</style>
