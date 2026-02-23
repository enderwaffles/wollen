<template>
  <Header />

  <div>
    <h1>Войти</h1>
  </div>

  <div>
    <input type="email" v-model="email" placeholder="Почта" /><br>
    <input type="password" v-model="password" placeholder="Пароль" /><br>

    <button :disabled="loading" @click="login">{{ loading ? 'Загрузка...' : 'Войти' }}</button> <br>
    <p v-if="message" class="error">{{ message }}</p> <br>
    <RouterLink to="/signup">У вас нету аккаунта?</RouterLink> <br>
    <RouterLink to="/">Вернуться назад</RouterLink>
  </div>
    
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()



let email = ref("")
let password = ref("")

let message = ref("")
let loading = ref(false)



async function login() {
  try {
    loading.value = true
    message.value = ""
    const res = await api.post("/login", {
      email: email.value,
      password: password.value
    })
    auth.login({
      id: res.data.user.id,
      email: res.data.user.email,
      nickname: res.data.user.nickname,
      name: res.data.user.name,
      surname: res.data.user.surname,
      admin: res.data.user.admin,
    })
    router.push("/")
  }
  catch (error) {
    console.log(error)
    message.value = "Login failed"
  }
  finally {
    loading.value = false
  }
}

</script>

<style scoped></style>
