<template>
  <Header />
  
  <div>
    <h1>Главная</h1>
  </div>

  <div>
    <p>{{ message }}</p>
  </div>

</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { onMounted, ref } from 'vue'

const message = ref("")

onMounted(async () => {
  try {
    const res = await api.get("")
    message.value = res.data.message
  } 
  catch {
    message.value = ""
  }
})
</script>

<style scoped>

</style>
