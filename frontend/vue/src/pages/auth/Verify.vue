<template>
  <Header />

  <div class="title">
    <h1>Вериикация</h1>
  </div>

  <main class="auth">

    <div class="card">

      <input
        type="incode"
        v-model="incode"
        placeholder="Код"
      />

      <button
        :disabled="loading"
        @click="verify"
      >
        {{ loading ? 'Загрузка...' : 'Верификация' }}
      </button>

      <p v-if="message" class="error">
        {{ message }}
      </p>

      <div class="links">
        
      </div>

    </div>

  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/api'

const auth = useAuthStore()
const router = useRouter()
const route = useRoute()

const email = ref(route.query.email || '')

const incode = ref('')

const message = ref('')
const loading = ref(false)

async function verify() {

  if (!incode.value) {
    message.value = 'Fill in all fields'
    return
  }

  try {
    loading.value = true
    message.value = ''

    const res = await api.post('/verify', {
        email: email.value,
        code: incode.value
    })

    auth.login({
      id: res.data.user.id,
      email: res.data.user.email,
      nickname: res.data.user.nickname,
      name: res.data.user.name,
      surname: res.data.user.surname,

    })

    router.push('/')
  }
  catch (error) {
    console.log(error)
    message.value = 'Signup failed'
  }
  finally {
    loading.value = false
  }
}
</script>

<style scoped>

</style>
