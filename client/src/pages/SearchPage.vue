<template>
  <div class="container px-16">
    <div
      :class="{
        'mt-24 grid grid-cols-2 gap-4': courses.length > 3,
        'mt-24': courses.length <= 3,
      }"
    >
      <div
        v-for="course in courses"
        :key="course.id"
        class="max-w-2xl mx-auto mt-6 p-4 rounded-xl border-2 border-slate-100/10 bg-[#000101] text-white shadow-lg transition-all duration-200 hover:scale-105"
      >
        <div class="flex justify-between items-start">
          <div class="flex flex-col">
            <div class="mb-4">
              <p class="font-semibold text-2xl mb-1">
                {{ course.name }}
              </p>
              <p class="font-light text-lg text-gray-400">by {{ course.instructor_name }}</p>
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
          <div class="text-xl font-light">75 students</div>
          <div class="flex items-center">
            <div class="w-4 h-4 bg-yellow-400 clip-star"></div>
            <div class="text-xl font-light ml-2">4.5</div>
          </div>
          <button
            class="bg-slate-100 text-black rounded px-6 py-2 transition-colors duration-200 hover:bg-slate-200 hover:text-white"
          >
            <i class="fa-solid fa-cart-plus"></i>
            Add to cart!
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from "@/stores/AuthStore";
import { useSearchStore } from "@/stores/SearchStore";

export default {
  setup() {
    const authStore = useAuthStore();
    const searchStore = useSearchStore();

    return { authStore, searchStore };
  },
  name: "SearchPage",
  data() {
    return {
      userName: "username",
      courses: [
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 2, name: "Course 2", image: "url-to-course-2-image" },
        { id: 3, name: "Course 3", image: "url-to-course-3-image" },
        { id: 2, name: "Course 2", image: "url-to-course-2-image" },
        { id: 3, name: "Course 3", image: "url-to-course-3-image" },
        { id: 2, name: "Course 2", image: "url-to-course-2-image" },
        { id: 3, name: "Course 3", image: "url-to-course-3-image" },
      ],
    };
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
    console.log(this.courses);
  },
};
</script>
