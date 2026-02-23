<template>
  <Header />

  <div>
    <h1>Вериикация</h1>
  </div>

  <div>
    <input type="text" v-model="incode" placeholder="Код" /> <br>

    <button :disabled="loading" @click="verify">{{ loading ? 'Загрузка...' : 'Верификация' }}</button>
    <p v-if="message" class="error">{{ message }}</p>
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



let email = ref(route.query.email || "")
let incode = ref("")

let message = ref("")
let loading = ref(false)



async function verify() {
  try {
    loading.value = true
    message.value = ""
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
      admin: res.data.user.admin,
    })
    router.push("/")
  }
  catch (error) {
    console.log(error)
    message.value = "Verify failed"
  }
  finally {
    loading.value = false
  }
}

</script>

<style scoped></style>
