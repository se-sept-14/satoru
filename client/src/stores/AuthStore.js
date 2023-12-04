import axios from "axios";
import { defineStore } from "pinia";

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    api: {
      server:
        window.location.hostname == "localhost" ||
        window.location.hostname == "127.0.0.1"
          ? "http://localhost:8000"
          : "https://pickmycourse.online",
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
      const apiUrl = `${this.api.server}${this.api.endpoints.auth.login}`;
      const headers = {
        accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
      };
      const { username, password } = await userData;
      const formData = new URLSearchParams();
      formData.append('username', username);
      formData.append('password', password);

      try {
        const { data } = await axios.post(apiUrl, formData, { headers });
        console.log(data);

        if (data) {
          const { access_token, token_type } = data;
          this.currentUser["access_token"] = access_token;
          this.currentUser["token_type"] = token_type;
          localStorage.setItem("currentUser", JSON.stringify(this.currentUser));
        }
      } catch (err) {
        if (err.response.status == 401) {
          return null;
        }
      }

      return this.currentUser;
    },
  },
});
