import axios from "axios";
import { defineStore } from "pinia";

export const useCourseStore = defineStore("courseStore", {
  state: () => ({
    api: {
      server: "https://api.pickmycourse.online",
      endpoints: { courses: "/api/course/" },
    },
  }),
  getters: {},
  actions: {
    async fetchCourse(courseId) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.courses}${courseId}`;
        const headers = {
          accept: "application/json",
          Authorization: authToken,
        };

        try {
          const response = await axios.get(apiUrl, { headers });

          if (response.status === 200) {
            return response.data['data'];
          }
        } catch (err) {
          if (err.response && err.response.status === 404) {
            // Handle 404 error here
            console.error("Course not found");
            return null;
          } else {
            // Handle other errors
            console.error("Error fetching course:", err.message);
            return false;
          }
        }
      } else {
        return {};
      }
    },
    // Add more actions for other course-related API calls as needed
  },
});
