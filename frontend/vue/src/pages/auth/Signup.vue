<template>
  <Header />

  <div>
    <h1>Регистрация</h1>
  </div>

  <div>
    <input type="email" v-model="email" placeholder="Почта" /><br>
    <input type="text" v-model="nickname" placeholder="Ник" /><br>
    <input type="text" v-model="name" placeholder="Имя" /><br>
    <input type="text" v-model="surname" placeholder="Фамилия" /><br>
    <input type="password" v-model="password" placeholder="Пароль" /><br>
    <input type="password" v-model="repeat_password" placeholder="Повторить пароль" /><br>

    <button :disabled="loading" @click="signup">{{ loading ? 'Загрузка...' : 'Регистрироваться' }}</button> <br>
    <p v-if="message" class="error">{{ message }}</p> <br>
    <RouterLink to="/login">У вас есть аккаунт?</RouterLink> <br>
    <RouterLink to="/">Вернуться назад</RouterLink>
  </div>

</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { ref, onMounted  } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()



let email = ref("")
let nickname = ref("")
let name = ref("")
let surname = ref("")
let password = ref("")
let repeat_password = ref("")

let message = ref("")
let loading = ref(false)



async function signup() {
  try {
    loading.value = true
    message.value = ""
    const res = await api.post("/signup", {
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
    message.value = "Signup failed"
  }
  finally {
    loading.value = false
  }
}

</script>

<style scoped></style>
