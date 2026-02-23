<template>
  <Header />
  
  <div>
    <h1>Про нас</h1>
  </div>

  <div>
    <p>{{ message }}</p>
  </div>
  
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { ref, onMounted  } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()
const route = useRoute()



let message = ref("")



onMounted(async () => {
  try {
    const res = await api.get("/about")
    message.value = res.data.message
  } 
  catch {
    message.value = ""
  }
})
</script>

<style scoped>

</style>
