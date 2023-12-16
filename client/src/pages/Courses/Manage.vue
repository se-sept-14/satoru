<template>
  <div>
    <navbar />

    <div class="w-[800px] h-[800px] relative bg-black mx-auto p-8">
      <div class="flex mb-12 justify-between">
        <p class="text-white text-3xl font-bold font-serif">Manage Courses</p>

        <p
          class="text-lg self-end text-yellow-100 cursor-pointer"
          @click="redirectToAddCourse"
        >
          <i class="fa-solid fa-circle-plus text-md mr-1"></i>
          <span class="hover:underline"> Create a new course </span>
        </p>
      </div>

      <div v-for="(course, index) in courses.data" :key="course.id">
        <div
          class="my-4 mx-auto py-2 bg-gray-950 rounded-lg text-white border border-gray-700 flex justify-between items-center"
        >
          <div class="p-4">
            <p class="text-2xl font-semibold mb-2">
              {{ course.name }}
            </p>
            <p class="text-sm italic font-extralight">
              {{ course.instructor_name }}
            </p>
            <p class="text-md font-semibold">{{ course.credits }} credits</p>
          </div>

          <div class="flex flex-col mx-4">
            <button
              @click="redirectToAdminCourseView(course.id)"
              class="w-24 h-8 rounded hover:bg-slate-600 mx-auto text-white text-md font-normal my-1"
            >
              <i class="fa-solid fa-pen-to-square text-xs"></i>
              Manage
            </button>
            <button
              @click="confirmDeleteCourse(course.id)"
              class="w-24 h-8 bg-red-500 rounded hover:bg-red-600 mx-auto text-white text-md font-normal my-1"
            >
              <i class="fa-solid fa-trash text-xs"></i>
              Delete
            </button>
          </div>
        </div>
      </div>

      <!-- A black dot just to add some margin at the bottom of the page -->
      <p class="text-black my-4 text-center">.</p>
    </div>
  </div>
</template>

<script>
// Components
import AuthenticatedNavbarComponent from "@/components/AuthenticatedNavbarComponent.vue";

// Stores
import { useCourseStore } from "@/stores/courseStore";

export default {
  data() {
    return {
      courses: [],
    };
  },
  components: {
    navbar: AuthenticatedNavbarComponent,
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
    redirectToAdminCourseView(courseId) {
      this.$router.push({
        name: "Admin Course details",
        params: {
          id: courseId,
        },
      });
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
    redirectToAddCourse() {
      this.$router.push("/add-course");
    },
  },
};
</script>
