<template>
  <div class="conversation">
    <message v-for="message in messages" :content="message.text"></message>
    <form class="messagebox" action='/' @submit='sendMessage'>
      <input class="text-input-field" type='text' v-model="message" placeholder="Enter message here" />
      <input type='submit' />
    </form>
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

      // log message for DEBUG
      console.log(this.message)
      var msg = {'text': this.message, 'isTrumpMessage': false}
      this.messages.push(msg)
      // now send to the API
      axios.get(TRUMPBOT_URL, {
        params: {
          q: this.message
        }
      }).then((response) => {
        var msg = {'text': response.data, 'isTrumpMessage': true}
        this.messages.push(msg)
      });

      // finally clear the textbox.
      this.message = ""
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.messagebox {
    background-color: green;
    width: 100%;
    height: 4rem;
    position: fixed;
    bottom: 0;
}
.conversation {
  overflow-y: auto;
}
.text-input-field {
  margin-top: 1rem;
  font-size: 18px;
}
</style>
