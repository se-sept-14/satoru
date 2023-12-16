<template>
  <div>
    <navbar />

    <div class="w-[960px] mx-auto flex flex-col text-white">
      <h1 class="text-2xl font-bold font-serif">
        Based on your profile, we recommend the following courses
      </h1>

      <div
        :class="{
          'mt-12 grid grid-cols-2 gap-4': courses.length > 3,
          'mt-12': courses.length <= 3,
        }"
      >
        <div
          v-for="course in courses"
          :key="course.id"
          class="max-w-2xl mx-auto mt-6 p-4 rounded-xl border-2 border-slate-100/10 bg-[#000101] text-white shadow-lg"
        >
          <div class="flex justify-between items-start">
            <div class="flex flex-col">
              <div class="mb-4">
                <span
                  class="font-semibold text-2xl mb-1 cursor-pointer hover:text-yellow-200"
                  @click="viewCoursePage(course.id)"
                >
                  {{ course.name }}
                </span>
                <p class="font-light text-lg text-gray-400">
                  by {{ course.instructor_name }}
                </p>
              </div>
              <p class="text-gray-400 mb-6">
                {{ course.description }}
              </p>
            </div>
            <img
              class="w-20 h-20 object-cover rounded-full ml-6"
              :src="course.instructor_picture"
            />
          </div>
          <div class="flex justify-between items-center w-full mt-6">
            <div class="text-xl font-light">{{ course.credits }} credits</div>
            <button
              @click="chooseCourse(course.id)"
              class="bg-slate-100 text-black rounded px-6 py-2 transition-colors duration-200 hover:bg-slate-500"
            >
              <i class="fa-solid fa-cart-plus"></i>
              Get this course
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Blank space at the bottom -->
    <p class="text-black my-8">.</p>
  </div>
</template>

<script>
// Stores
import { useAuthStore } from "@/stores/AuthStore";
import { useCourseStore } from "@/stores/courseStore";

// Components
import AuthenticatedNavbarComponent from "@/components/AuthenticatedNavbarComponent.vue";

export default {
  setup() {
    const authStore = useAuthStore();
    const courseStore = useCourseStore();

    return { authStore, courseStore };
  },
  name: "Recommend Courses",
  components: {
    navbar: AuthenticatedNavbarComponent,
  },
  data() {
    return {
      numberOfCourses: -1,
      courses: [],
    };
  },
  methods: {
    viewCoursePage(courseId) {
      this.$router.push({
        name: "ViewCourse",
        params: {
          id: courseId,
        },
      });
    },
    async chooseCourse(courseId) {
      const data = await this.courseStore.studentCourseMapById(courseId);

      if(data.message.length != 0) {
        const idx = this.courses.findIndex(course => course.id === courseId);

        if(idx !== -1) {
          this.courses.splice(idx, 1);
        }
      }
    },
  },
  async created() {
    if (!this.authStore.isLoggedIn()) {
      this.$router.push("/login");
      return;
    }

    this.numberOfCourses = this.$route.params["numberOfCourses"];
    this.courses = await this.courseStore.recommendCourses(
      this.numberOfCourses
    );
  },
};
</script>
