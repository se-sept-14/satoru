<template>
  <div class="w-[800px] h-[800px] relative bg-black mx-auto p-8">
    <div class="text-center text-white text-3xl font-bold mb-4">
      Manage Courses
    </div>
    <br />
    <div v-for="(course, index) in courses.data" :key="course.id">
      <div
        class="mx-auto relative bg-gray-950 rounded-xl text-white border border-gray-500"
      >
        <div class="p-4">
          <div class="text-center text-xl font-semibold mb-2">
            {{ course.name }}<a href="#">(click to view)</a>
          </div>
          <div class="text-center text-lg font-light">
            {{ course.instructor_name }}
          </div>
        </div>

        <div class="flex justify-between p-4 text-center">
          <div class="text-xl font-normal">{{ course.credits }} credits</div>
          <div class="text-xl font-normal">199 students</div>
          <div class="flex">
            <div class="w-5 h-5 bg-yellow-400 clip-star"></div>
            <div class="text-xl font-normal ml-2">4.5</div>
          </div>
          <div class="text-xl font-normal">
            Register by:<br />18 December 2023
          </div>
        </div>

        <div class="flex justify-between p-4">
          <button
            @click="redirectToAdminCourseView"
            class="w-32 h-12 bg-green-500 rounded-xl hover:bg-green-600 mx-auto text-white text-lg font-normal"
          >
            Manage
          </button>
          <button
            @click="confirmDeleteCourse(course.id)"
            class="w-32 h-12 bg-red-500 rounded-xl hover:bg-red-600 mx-auto text-white text-lg font-normal"
          >
            Delete
          </button>
        </div>
        <br />
      </div>
      <br />
    </div>

    <div class="w-[100%] mx-auto mt-8 item-right">
      <div class="flex flex-col-2 items-center">
        <button
          class="w-[20%] h-10 relative bg-gradient-to-b from-gray-900 to-gray-600 text-center rounded-xl flex items-center hover:bg-green-600 justify-center text-white text-xl font-normal mr-5 p-5"
        >
          Add Course
        </button>
        <div class="flex items-center justify-end">
          <button
            class="w-20 h-20 bg-gradient-to-b from-gray-900 to-gray-600 rounded-full flex items-center hover:bg-green-600 justify-center focus:outline-none"
            onclick="handleButtonClick()"
          >
            <div
              class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-black"
            >
              <span class="text-2xl">+</span>
            </div>
          </button>
        </div>
      </div>
    </div>
    <br /><br /><br />
  </div>
</template>

<script>
import { useCourseStore } from "@/stores/courseStore";

export default {
  data() {
    return {
      courses: [],
    };
  },
  async beforeMount() {
    const isAdmin = await useCourseStore().isAdmin();

    if (!isAdmin) {
      this.$router.push("/dashboard");
    }

    const accessToken = localStorage.getItem("access_token");

    if (!accessToken) {
      this.$router.push("/login");
    }
  },
  async mounted() {
    await this.fetchCourses();
  },
  computed: {
    courses() {
      return useCourseStore().courses;
    },
  },

  methods: {
    async fetchCourses() {
      await useCourseStore().fetchCourses();
    },
    redirectToAdminCourseView() {
      this.$router.push("/admin-course-view");
    },
    confirmDeleteCourse(courseId) {
      const confirmDelete = window.confirm(
        "Are you sure you want to delete this course?"
      );
      if (confirmDelete) {
        this.deleteCourse(courseId);
      }
    },
    async deleteCourse(courseId) {
      const confirmDelete = window.confirm(
        "Are you sure you want to delete this course?"
      );
      if (confirmDelete) {
        await useCourseStore().deleteCourse(courseId);
      }
    },
  },
};
</script>