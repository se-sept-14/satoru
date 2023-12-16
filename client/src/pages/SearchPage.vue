<template>
  <div>
    <navbar />
    
    <div class="container px-16">
      <div
        :class="{
          'mt-24 grid grid-cols-2 gap-4': courses.length > 3,
          'mt-24': courses.length <= 3,
        }"
      >
        <h1 v-if="courses.length == 0" class="text-4xl font-bold text-white">
          No results found
        </h1>
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
            <div class="flex items-center">
              <div class="w-4 h-4 bg-yellow-400 clip-star"></div>
              <div class="text-xl font-light ml-2">4.5</div>
            </div>
            <button
              class="bg-slate-100 text-black rounded px-6 py-2 transition-colors duration-200 hover:bg-slate-200 hover:text-white"
            >
              <i class="fa-solid fa-cart-plus"></i>
              Get this course
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Stores
import { useAuthStore } from "@/stores/AuthStore";
import { useSearchStore } from "@/stores/SearchStore";
import { useCourseStore } from "@/stores/courseStore";

// Components
import AuthenticatedNavbarComponent from "@/components/AuthenticatedNavbarComponent.vue";

export default {
  setup() {
    const authStore = useAuthStore();
    const searchStore = useSearchStore();
    const courseStore = useCourseStore();

    return { authStore, searchStore };
  },
  name: "SearchPage",
  components: {
    navbar: AuthenticatedNavbarComponent,
  },
  data() {
    return {
      userName: "username",
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
  },
  async created() {
    if (this.$route.params.query.toString().length == 0) {
      console.log("Empty query");
      return;
    }

    if (!this.authStore.isLoggedIn()) {
      this.$router.push("/login");
      return;
    }

    this.courses = await this.searchStore.searchCourse(
      this.$route.params.query
    );

    if (this.courses.length == 0) {
      console.log("No courses found");
    }
  },
};
</script>
