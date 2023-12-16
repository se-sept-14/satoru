import axios from "axios";
import { defineStore } from "pinia";

/**
 * Using Dicebear to generate random profile pictures, check docs: https://www.dicebear.com/how-to-use/http-api/
 */
export const useReviewStore = defineStore("reviewStore", {
  state: () => ({
    api: {
      server: "https://api.pickmycourse.online",
      endpoints: {
        create: "/api/review/",
        fetchAll: "/api/review/all",
        fetchByCourseId: "/api/review/course-id/",
        flag: "/api/review/flag/",
        edit: "/api/review/",
        delete: "/api/review/",
        deleteFlagged: "/api/review/flagged/",
        tag: "/api/review/tag"
      },
    },
  }),
  getters: {},
  actions: {
    async getReviewsByCourseId(courseId) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if(tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.fetchByCourseId}${courseId}`;
        const headers = {
          Authorization: authToken,
          accept: "application/json",
          "Content-Type": "application/json"
        }

        try {
          const response = await axios.get(apiUrl, { headers });

          if(response.status == 200) {
            return response.data['data'];
          }
        } catch(err) {
          if (err.response && err.response.status === 404) {
            console.error("No such course found");
            return null;
          } else {
            console.error("Error fetching reviews:", err.message);
            return false;
          }
        }
      } else {
        return this.$router.push("/login")
      }
    },
    async flagReviewById(id) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if(tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.flag}${id}`;
        const headers = {
          Authorization: authToken,
          accept: "application/json",
          "Content-Type": "application/json"
        }

        try {
          const response = await axios.post(apiUrl, {}, { headers });

          if(response.status == 200) {
            return response.data;
          }
        } catch(err) {
          if (err.response && err.response.status === 404) {
            console.error("No such course found");
            return null;
          } else {
            console.error("Error fetching reviews:", err.message);
            return false;
          }
        }
      } else {
        return this.$router.push("/login")
      }
    },
    async deleteReviewById(id) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if(tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.deleteFlagged}${id}`;
        const headers = {
          Authorization: authToken,
          accept: "application/json",
          "Content-Type": "application/json"
        }

        try {
          const response = await axios.delete(apiUrl, { headers });

          if(response.status == 200) {
            return response.data;
          }
        } catch(err) {
          if (err.response && err.response.status === 404) {
            console.error("No such course found");
            return null;
          } else {
            console.error("Error fetching reviews:", err.message);
            return false;
          }
        }
      } else {
        return this.$router.push("/login")
      }
    }
  },
});
