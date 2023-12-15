import axios from "axios";
import { defineStore } from "pinia";

/**
 * Using Dicebear to generate random profile pictures, check docs: https://www.dicebear.com/how-to-use/http-api/
 */
export const useSearchStore = defineStore("searchStore", {
  state: () => ({
    api: {
      server: "https://api.pickmycourse.online",
      endpoints: { search: "/api/course/search" },
    },
  }),
  getters: {},
  actions: {
    async searchCourse(query) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if(tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.search}`;
        const headers = {
          Authorization: authToken,
          accept: "application/json",
          "Content-Type": "application/json"
        }
        const payload = { query };

        try {
          const response = await axios.post(apiUrl, payload, { headers });

          if(response.status == 200) {
            return response.data['data'];
          }
        } catch(err) {
          if (err.response && err.response.status === 404) {
            console.error("Profile not found");
            return null;
          } else {
            console.error("Error fetching profile:", err.message);
            return false;
          }
        }
      } else {
        return this.$router.push("/login")
      }
    },
  },
});
