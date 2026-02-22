<template>
  <Header />

  <div class="title">
    <h1>Profile</h1>
  </div>

  <main class="profile">

    <div class="card">

      <p><b>Email:</b> {{ auth.user?.email }}</p>
      <p><b>Nickname:</b> {{ auth.user?.nickname }}</p>
      <p><b>Name:</b> {{ auth.user?.name }}</p>
      <p><b>Surname:</b> {{ auth.user?.surname }}</p>

      <button @click="logout">
        Logout
      </button>
      
      <div class="links">
        <a href="#" @click.prevent="goBack">← Back</a>
      </div>
    </div>

  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

function logout() {
  auth.logout()
  router.push('/')
}
function goBack() {
  // если человек открыл страницу напрямую — отправим домой
  if (window.history.length > 1) router.back()
  else router.push('/')
}
</script>

<style scoped>

</style>
