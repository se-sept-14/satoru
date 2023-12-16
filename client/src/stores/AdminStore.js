import axios from "axios";
import { defineStore } from "pinia";

export const useAdminStore = defineStore("adminStore", {
  state: () => ({
    api: {
      baseUrl: "https://api.pickmycourse.online",
      endpoints: {
        allStudents: "/api/admin/all-students",
      },
    },
    currentUser: {},
  }),
  getters: {},
  actions: {
    async fetchAllStudents() {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.baseUrl}${this.api.endpoints.allStudents}`;
        const headers = {
          accept: "application/json",
          Authorization: authToken,
        };

        try {
          const response = await axios.get(apiUrl, { headers });

          if (response.status == 200) {
            return response.data["data"];
          }
        } catch (err) {
          if (err.response && err.response.status === 404) {
            console.error("No students not found");
            return null;
          } else {
            console.error("Error fetching students:", err.message);
            return false;
          }
        }
      } else {
        return false;
      }
    },
  },
});
