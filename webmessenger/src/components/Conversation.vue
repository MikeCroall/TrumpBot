<template>
  <div class="conversation">
    <div class="message-list">
      <message v-for="message in messages" :content="message.text" :isMyMessage="message.isMyMessage"></message>
    </div>
    <div class="spacer">

    </div>
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
      var msg = {'text': response.data, 'isMyMessage': false}
      this.messages.push(msg)
    })
  },
  methods: {
    sendMessage(event) {
      event.preventDefault()

      // log message for DEBUG
      console.log(this.message)
      var msg = {'text': this.message, 'isMyMessage': true}
      this.messages.push(msg)
      // now send to the API
      axios.get(TRUMPBOT_URL, {
        params: {
          q: this.message
        }
      }).then((response) => {
        var msg = {'text': response.data, 'isMyMessage': false}
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

.message-list {
  display: block;
}
.messagebox {
    background-color: darkblue;
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
.spacer {
  height: 200px;
  width: 100%

}
</style>
