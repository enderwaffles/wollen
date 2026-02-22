<template>
  <Header />

  <div class="title">
    <h1>Регистрация</h1>
  </div>

  <main class="auth">

    <div class="card">

      <input type="email" v-model="email" placeholder="Почта" />
      <br>
      
      <input type="text" v-model="nickname" placeholder="Ник" />
      <br>

      <input type="text" v-model="name" placeholder="Имя" />
      <br>

      <input type="text" v-model="surname" placeholder="Фамилия" />
      <br>

      <input type="password" v-model="password" placeholder="Пароль" />
      <br>

      <input type="password" v-model="repeat_password" placeholder="Повторить пароль" />
      <br>

      <button :disabled="loading" @click="signup">
        {{ loading ? 'Загрузка...' : 'Регистрироваться' }}
      </button>

      <p v-if="message" class="error">
        {{ message }}
      </p>

      <div class="links">
        <RouterLink to="/login">
          У вас есть аккаунт?
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
import { useRouter } from 'vue-router'
import api from '@/api/api'

const router = useRouter()

const email = ref('')
const nickname = ref('')
const name = ref('')
const surname = ref('')
const password = ref('')
const repeat_password = ref('')

const message = ref('')
const loading = ref(false)

async function signup() {

  if (
    !email.value ||
    !nickname.value ||
    !name.value ||
    !surname.value ||
    !password.value ||
    !repeat_password.value
  ) {
    message.value = 'Fill in all fields'
    return
  }

  if (password.value !== repeat_password.value) {
    message.value = 'Passwords do not match'
    return
  }

  try {
    loading.value = true
    message.value = ''

    await api.post('/signup', {
      email: email.value,
      nickname: nickname.value,
      name: name.value,
      surname: surname.value,
      password: password.value
    })

    router.push(`/verify?email=${email.value}`)

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

<style scoped></style>
