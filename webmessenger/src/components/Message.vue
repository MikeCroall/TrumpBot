<template>
  <div class="message">
    <p>
      {{ content }}
    </p>
  </div>
</template>

<script>

export default {
  name: 'message',
  props: ['content', 'isTrumpMessage']
}
</script>

<style scoped>
.p {

}

</style>
