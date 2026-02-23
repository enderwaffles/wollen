<template>
  <Header />

  <div>
    <h1>Profile</h1>
  </div>

  <div>
    <p><b>Email:</b> {{ auth.user?.email }}</p>
    <p><b>Nickname:</b> {{ auth.user?.nickname }}</p>
    <p><b>Name:</b> {{ auth.user?.name }}</p>
    <p><b>Surname:</b> {{ auth.user?.surname }}</p>
    
    <button @click="logout">Logout</button>
    <a href="#" @click.prevent="goBack">← Back</a>
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



function logout() {
  auth.logout()
  router.push('/')
}

function goBack() {
  if (window.history.length > 1) router.back()
  else router.push("/")
}

</script>

<style scoped>

</style>
