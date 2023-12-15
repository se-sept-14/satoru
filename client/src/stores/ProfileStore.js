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
});