import axios from "axios";
import { defineStore } from "pinia";

export const useCourseStore = defineStore("courseStore", {
  state: () => ({
    api: {
      baseUrl: "https://api.pickmycourse.online",
      endpoints: {
        studentCourseMap: "/api/course/student-course-map/",
        recommend: "/api/course/recommend/"
      }
    },
    courseList: [],
    courses: [],
  }),
  getters: { getCourses: (state) => state.courses },
  actions: {
    async isAdmin() {
      try {
        const accessToken = localStorage.getItem("access_token");
        const response = await axios.get(
          "https://api.pickmycourse.online/api/auth/is-admin",
          {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          }
        );

        // Check if the user is an admin based on the response
        return response.data.is_admin === 1;
      } catch (error) {
        console.error("Error checking admin status:", error);
        return false; // Default to false in case of an error
      }
    },
    async fetchCourses() {
      const accessToken = localStorage.getItem("access_token");
      try {
        const response = await axios.get(
          "https://api.pickmycourse.online/api/course/all",
          {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          }
        );
        this.courses = response.data;
      } catch (error) {
        console.error("Error fetching courses:", error);
      }
    },
    async fetchCourseById(id) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const headers = {
          accept: "application/json",
          Authorization: authToken,
        };
        const apiUrl = `https://api.pickmycourse.online/api/course/id/${id}`;

        try {
          const response = await axios.get(apiUrl, { headers });

          if (response.status == 200) {
            return response.data["data"];
          }
        } catch (err) {
          console.error(err);
          return {};
        }
      } else {
        this.$router.push("/login");
      }
    },
    async deleteCourse(courseId) {
      const accessToken = localStorage.getItem("access_token");
      try {
        await axios.delete(
          `https://api.pickmycourse.online/api/course/${courseId}`,
          {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          }
        );

        // Refresh the course list after deletion
        await this.fetchCourses();
      } catch (error) {
        console.error("Error deleting course:", error);
        // Handle error as needed
      }
    },
    async addCourse(courseData) {
      try {
        // Assuming you have an API endpoint for adding a course
        const accessToken = localStorage.getItem("access_token");

        const headers = {
          accept: "application/json",
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        };
        console.log(courseData);
        const response = await axios.post(
          "https://api.pickmycourse.online/api/course/",
          courseData,
          { headers }
        );

        this.courseList.push(response.data);
        return response.data;
      } catch (error) {
        // Handle errors appropriately
        console.error("Error adding course:", error);
        throw error;
      }
    },
    async studentCourseMapById(courseId) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.baseUrl}${this.api.endpoints.studentCourseMap}${courseId}`;
        const headers = {
          Authorization: authToken,
          accept: "application/json",
          "Content-Type": "application/json",
        };

        try {
          const response = await axios.post(apiUrl, {}, { headers });

          if (response.status == 200) {
            return response.data;
          }
        } catch (err) {
          if (err.response && err.response.status === 404) {
            console.error("No such course found");
            return null;
          } else {
            console.error("Error fetching reviews:", err.message);
            return false;
          }
        }
      } else {
        return this.$router.push("/login");
      }
    },
    async recommendCourses(numberOfCourses) {
      const tokenType = localStorage.getItem("token_type");
      const accessToken = localStorage.getItem("access_token");

      if (tokenType && accessToken) {
        const authToken = `${tokenType} ${accessToken}`;
        const apiUrl = `${this.api.baseUrl}${this.api.endpoints.recommend}${numberOfCourses}`;
        const headers = {
          Authorization: authToken,
          accept: "application/json",
          "Content-Type": "application/json",
        };

        try {
          const response = await axios.get(apiUrl, { headers });

          if (response.status == 200) {
            return response.data.data;
          }
        } catch (err) {
          if (err.response && err.response.status === 404) {
            console.error("No such course found");
            return null;
          } else {
            console.error("Error fetching reviews:", err.message);
            return false;
          }
        }
      } else {
        return this.$router.push("/login");
      }
    },
  },
});
