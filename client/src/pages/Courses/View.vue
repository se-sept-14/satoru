<template>
  <!-- Overall page divided into 2 rows -->
  <div class="flex flex-col w-8/12 mx-auto">
    <!-- Upper section, 2 columns -->
    <div class="flex flex-row mt-24 justify-around">
      <!-- Left column -->
      <div class="flex flex-col px-4">
        <p class="text-3xl font-bold font-serif text-white">
          {{ courseData.name }}
        </p>
        <p class="text-lg font-light text-white w-[768px] mt-6">
          {{ courseData.description }}
        </p>

        <div class="flex flex-row text-white text-lg justify-between mt-12">
          <div class="flex flex-col">
            <p class="font-semibold">
              Prerequisites
              <span class="font-extralight text-2xl">{{
                courseData.prerequisites
              }}</span>
            </p>
            <p class="font-semibold">
              Corerequisites
              <span class="font-extralight text-2xl">{{
                courseData.corequisite
              }}</span>
            </p>
            <p class="font-semibold">
              Credits
              <span class="font-extralight text-2xl">{{
                courseData.credits
              }}</span>
            </p>
          </div>
          <div class="flex flex-col">
            <p class="font-semibold">
              Average grade <span class="font-extralight text-2xl">B</span>
            </p>
            <p class="font-semibold">
              Hours per week
              <span class="font-extralight text-2xl"
                >{{ courseData.hours_per_week }} hours</span
              >
            </p>
            <p class="font-semibold">
              Price
              <span class="font-extralight text-2xl"
                >₹{{ courseData.price }}/-</span
              >
            </p>
          </div>
        </div>
      </div>

      <!-- Right column -->
      <div class="flex flex-col">
        <img
          :src="courseData.instructor_picture"
          :alt="courseData.instructor_name"
          class="rounded-full w-32 self-center"
        />

        <p
          class="font-extralight text-xl text-center text-gray-400 mt-2 font-serif"
        >
          {{ courseData.instructor_name }}
        </p>

        <button class="bg-emerald-600 mt-16 p-4 rounded-md font-serif text-md self-center">
          <i class="fa-solid fa-cart-shopping"></i> <span>Add to cart</span>
        </button>
      </div>
    </div>

    <!-- Lower section, 2 sections -->
    <div class="flex flex-row"></div>
  </div>
</template>

<script>
import { useCourseStore } from "@/stores/courseStore";

export default {
  setup() {
    const courseStore = useCourseStore();
    return { courseStore };
  },
  name: "ViewCourse",
  data() {
    return {
      courseId: -1,
      courseData: {},
    };
  },
  async created() {
    this.courseId = this.$route.params.id;
    this.courseData = await this.courseStore.fetchCourseById(this.courseId);
  },
};
</script>

<style scoped></style>
