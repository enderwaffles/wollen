import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const session = ref(
    localStorage.getItem("session") === "true"
  );

  const user = ref(
    JSON.parse(localStorage.getItem("user"))
  );

  function login({ id, email, nickname, name, surname }) {
    user.value = { id, email, nickname, name, surname };
    session.value = true;

    localStorage.setItem("session", "true");
    localStorage.setItem("user", JSON.stringify(user.value));
  }

  function logout() {
    user.value = null;
    session.value = false;

    localStorage.removeItem("session");
    localStorage.removeItem("user");
  }

  return {
    session,
    user,
    login,
    logout,
  };
});
