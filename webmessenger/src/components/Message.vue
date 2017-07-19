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
  background-color: red;
}

.me {
  float: right;
  background-color: green;

}


</style>
