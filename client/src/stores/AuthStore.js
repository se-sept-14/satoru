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
    async login(userData) {
      const { username, password } = await userData;
      const apiUrl = `${this.api.server}${this.api.endpoints.auth.login}`;
      const headers = {
        accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
      };

      const formData = new URLSearchParams();
      formData.append("username", username);
      formData.append("password", password);

      try {
        const { data } = await axios.post(apiUrl, formData, { headers });

        if (data) {
          const { access_token, token_type } = data;

          this.currentUser["token_type"] = token_type;
          this.currentUser["access_token"] = access_token;
        }
      } catch (err) {
        switch(err.response.status) {
          case 401: return 401;
          case 404: return 404;
          default: return err.message;
        }
      }

      return this.currentUser;
    },
    async register(userData) {
      const apiUrl = `${this.api.server}${this.api.endpoints.auth.register}`;
      const headers = {
        accept: "application/json",
        "Content-Type": "application/json",
      };
      const { username, email, password } = await userData;
      const payload = { email, username, password };

      try {
      } catch (err) {
        if (err.response.status == 400) {
          // User already exists condition
          return null;
        }
      }
    },
  },
});
