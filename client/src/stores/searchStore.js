import axios from "axios";
import { defineStore } from "pinia";

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    api: {
      server: "https://api.pickmycourse.online",
      endpoints: {
        auth: {
          login: "/api/auth/login",
          register: "/api/auth/register",
        },
      },
    },
    currentUser: {},
  }),
  getters: {},
  actions: {
    logout() {
      try {
        localStorage.setItem("access_token", "");
        localStorage.setItem("token_type", "");

        return {
          success: true,
        };
      } catch (err) {
        console.error("Logout failed:", err);
        return {
          success: false,
          error: err.message,
        };
      }
    },
  },
});
