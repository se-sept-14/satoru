import axios from "axios";
import { defineStore } from "pinia";

export const useProfileStore = defineStore("profileStore", {
  state: () => ({
    api: {
      server: "https://api.pickmycourse.online",
      endpoints: {
        courses: "/api/course/student-course",
        profile: "/api/profile/",
      },
    },
  }),
  getters: {},
  actions: {
    async createProfile(profileData) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.server}${this.api.endpoints.profile}`;
        const headers = {
          accept: "application/json",
          Authorization: authToken,
        };

        // const { payload } = profileData;
        console.log(apiUrl);
        console.log(authToken);
        try {
          const response = await axios.post(apiUrl, profileData, { headers });
          console.log(response);
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
  },
});
