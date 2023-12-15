import axios from "axios";
import { defineStore } from "pinia";

/**
 * Using Dicebear to generate random profile pictures, check docs: https://www.dicebear.com/how-to-use/http-api/
 */
export const useUserProfileStore = defineStore("userProfileStore", {
  state: () => ({
    api: {
      server: "https://api.pickmycourse.online",
      endpoints: {
        courses: "/api/course/student-course",
        profile: "/api/profile/",
      },
    },
    profilePicture: {
      api: "https://api.dicebear.com/7.x/pixel-art/svg?seed=",
    },
  }),
  getters: {},
  actions: {
    async fetchProfile() {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.profile}`;
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
            console.error("Profile not found");
            return null;
          } else {
            console.error("Error fetching profile:", err.message);
            return false;
          }
        }
      } else {
        return {};
      }
    },
    async fetchStudentCourses() {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.courses}`;
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
            console.error("Profile not found");
            return null;
          } else {
            console.error("Error fetching profile:", err.message);
            return false;
          }
        }
      } else {
        return {};
      }
    },
    async fetchProfilePicture(username) {
      const apiUrl = `${this.profilePicture.api}${username.toString().trim()}`;
      const { data } = await axios.get(apiUrl);
      return data;
    },
    async fetchProfileById(id) {},
  },
});
