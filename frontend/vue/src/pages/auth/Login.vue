<template>
  <Header />

  <div class="title">
    <h1>Войти</h1>
  </div>

  <main class="auth">

    <div class="card">

      <input type="email" v-model="email" placeholder="Почта" />
      <br>

      <input type="password" v-model="password" placeholder="Пароль" />
      <br>

      <button :disabled="loading" @click="login">
        {{ loading ? 'Загрузка...' : 'Войти' }}
      </button>

      <p v-if="message" class="error">
        {{ message }}
      </p>

      <div class="links">
        <RouterLink to="/signup">
          У вас нету аккаунта?
        </RouterLink>

        <RouterLink to="/">
          Вернуться назад
        </RouterLink>
      </div>

    </div>

  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import api from '@/api/api'

const auth = useAuthStore()
const router = useRouter()

const email = ref('')
const password = ref('')

const message = ref('')
const loading = ref(false)

async function login() {
  if (!email.value || !password.value) {
    message.value = 'Fill in all fields'
    return
  }

  try {
    loading.value = true
    message.value = ''

    const res = await api.post('/login', {
      email: email.value,
      password: password.value
    })

    auth.login({
      id: res.data.user.id,
      email: res.data.user.email,
      nickname: res.data.user.nickname,
      name: res.data.user.name,
      surname: res.data.user.surname
    })

    router.push('/')
  }
  catch (error) {
    console.log(error)
    message.value = 'Login failed'
  }
  finally {
    loading.value = false
  }
}
</script>

<style scoped></style>
