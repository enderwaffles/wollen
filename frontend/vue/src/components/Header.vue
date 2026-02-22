<template>

<header class="header">

<div class="part">
    <h1>Wollen</h1>
</div>

<div class="part">
    <RouterLink class="nav-link" to="/">Главное </RouterLink>
    <RouterLink class="nav-link" to="/about">Про нас </RouterLink>
    <!-- <RouterLink class="nav-link" to="/posts">Продукты </RouterLink> -->
    <!-- <RouterLink v-if="auth.session" to="/create_post">Добавить продукт </RouterLink> -->
</div>

<div class="part">
    <div v-if="!auth.session">
        <RouterLink class="auth-link signup-btn" to="/signup">Регистрация </RouterLink>
        <RouterLink class="auth-link" to="/login">Войти </RouterLink>
    </div>  

    <div v-else>
        <RouterLink class="auth-link" to="/profile">Profile</RouterLink>
    </div>
</div>


</header>

</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()
</script>

<style scoped>

</style>
