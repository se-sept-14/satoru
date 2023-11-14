import axios from "axios";
import { defineStore } from "pinia";

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    api: {
      server: "http://localhost:8000",
      endpoints: {
        auth: {
          login: "/api/auth/login",
          register: "/api/auth/register",
        },
      },
    },
    currentUser: {},
  }),
  getters: {
    getCurrentUser() {
      return this.currentUser;
    },
  },
  actions: {
    async login(userData) {
      const { email, password } = await userData;
      const payload = {
        email: email,
        password: password,
      };

      try {
        const { data } = await axios.post(
          `${this.api.server}${this.api.endpoints.auth.login}`,
          payload
        );

        if (data) {
          const { access_token, token_type } = data;
          this.currentUser["access_token"] = access_token;
          this.currentUser["token_type"] = token_type;
          localStorage.setItem("currentUser", JSON.stringify(this.currentUser));
        }
      } catch (err) {
        console.error(err);
      }

      return this.currentUser;
    },
  },
});
