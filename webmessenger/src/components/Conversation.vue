<template>
  <div class="conversation">
    <message v-for="message in messages" :content="message.text"></message>
    <!-- <form action='/' @submit='sendMessage'>
      <input type='text' v-model="message" placeholder="Enter message here"
    </form> -->
  </div>
</template>

<script>
import Message from './Message.vue'
import axios from 'axios'
const TRUMPBOT_URL = 'https://trumpedupkicks.herokuapp.com/response'
export default {
  name: 'conversation',
  components: {'message': Message},
  data () {
    return {
      messages: []
    }
  },
  created() {
    axios.get(TRUMPBOT_URL)
    .then((response) => {
      var msg = {'text': response.data}
      this.messages.push(msg)
    })
  },
  methods: {
    sendMessage(event) {
      event.preventDefault()

      // send message
      console.log(this.message)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
