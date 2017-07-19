<template>
  <div class="message">
    <p class="trump">
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
p .trump {
  
}

</style>
