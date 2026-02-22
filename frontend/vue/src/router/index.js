import { createRouter, createWebHistory } from "vue-router"
import { useAuthStore } from "@/stores/auth";

import Home from "@/pages/Home.vue"
import About from "@/pages/About.vue"
import Login from "@/pages/auth/Login.vue"
import Signup from "@/pages/auth/Signup.vue"
import Verify from "@/pages/auth/Verify.vue";
import Profile from "@/pages/auth/Profile.vue";

// import Posts from "@/pages/posts/Posts.vue"
// import Post from "@/pages/posts/Post.vue"
// import Create_post from "@/pages/posts/Create_post.vue"
// import Update_post from "@/pages/posts/Update_post.vue";

const routes = [
    { path: '/', component: Home },
    { path: '/about', component: About },

    { path: '/login', component: Login },
    { path: '/signup', component: Signup },
    { path: '/verify', component: Verify },
    { path: '/profile', component: Profile, meta: { requiresAuth: true } },

    // { path: '/posts', component: Posts },
    // { path: '/posts/:id', component: Post },
    // { path: '/create_post', component: Create_post, meta: { requiresAuth: true } },
    // { path: '/update_post/:id', component: Update_post, meta: { requiresAuth: true } },


    
]


const router = createRouter(
    {
        history: createWebHistory(),
        routes,
    }
)

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();

  if (to.meta.requiresAuth && !auth.session) {
    next("/login");
  } else {
    next();
  }
});


export default router;