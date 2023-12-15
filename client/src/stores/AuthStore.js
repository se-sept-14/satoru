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
          isAdmin: "/api/auth/is-admin",
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
        switch (err.response.status) {
          case 401:
            return 401;
          case 404:
            return 404;
          default:
            return err.message;
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
        const { data } = await axios.post(apiUrl, payload, { headers });

        if (data) {
          const { access_token, token_type } = data;

          this.currentUser["token_type"] = token_type;
          this.currentUser["access_token"] = access_token;

          return this.currentUser;
        }
      } catch (err) {
        if (err.response) {
          const { status, data } = err.response;

          switch (status) {
            case 400:
              if (
                data.detail.includes("Email") ||
                data.detail.includes("Username")
              )
                return "Email or Username already in use";
            default:
              return status;
          }
        } else throw err;
      }
    },
    async isAdmin() {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.isAdmin}`;
        const headers = {
          accept: "application/json",
          Authorization: authToken,
        };

        try {
          const response = await axios.get(apiUrl, { headers });

          if (response.status == 200) {
            return response.data["is_admin"] == 1 ? true : false;
          }
        } catch (err) {
          if (err.response && err.response.status === 404) {
            console.error("Profile not found");
            return null;
          } else {
            console.error("Error fetching profile:", err.message);
            return false;
          }
        }
      } else {
        return false;
      }
    },
    isLoggedIn() {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      return tokenType && accessToken;
    },
  },
});
