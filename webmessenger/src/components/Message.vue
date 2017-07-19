<template>
  <div class="message">
    <div class="container" v-bind:class="{me: isMyMessage }">
        {{ content }}
    </div>
  </div>

</template>

<script>

export default {
  name: 'message',
  props: ['content', 'isMyMessage']
}
</script>

<style scoped>
.message {
  width: 100%;
  display: block;
  clear: both;
}
.container {
  margin-top: 10px;
  margin-bottom: 10px;
  border-radius: 10px;
  width: 60%;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 10px;
  padding-right: 10px;
  background-color: darkred;
  font-family: sans-serif;
  font-size: 18pt;
  font-weight: bold;
  font-variant: small-caps;
}

.me {
  float: right;
  background-color: green;
  font-weight: normal;
  font-variant: normal;
}


</style>
