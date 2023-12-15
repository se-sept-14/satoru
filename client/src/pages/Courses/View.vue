<template>
  <!-- Overall page divided into 2 rows -->
  <div class="flex flex-col w-7/12 mx-auto">
    <!-- Upper section, 2 columns -->
    <div class="flex flex-row">
      <!-- Left column -->
      <div class="flex flex-col">
        <p class="text-3xl font-bold font-serif text-white mt-24">{{ courseData.name }}</p>
        <p class="text-lg font-light text-white w-[768px] mt-4">{{ courseData.description }}</p>

        <div class="flex flex-row text-white text-lg justify-around mt-4">
          <div class="flex flex-col">
            <p class="font-semibold">Prerequisites <span class="font-extralight text-2xl">{{ courseData.prerequisites }}</span></p>
            <p class="font-semibold">Corerequisites <span class="font-extralight text-2xl">{{ courseData.corequisite }}</span></p>
            <p class="font-semibold">Credits <span class="font-extralight text-2xl">{{ courseData.credits }}</span></p>
          </div>
          <div class="flex flex-col">
            <p class="font-semibold">Average grade <span class="font-extralight text-2xl">B</span></p>
            <p class="font-semibold">Hours per week <span class="font-extralight text-2xl">{{ courseData.hours_per_week }} hours</span></p>
            <p class="font-semibold">Price <span class="font-extralight text-2xl">₹{{ courseData.price }}/-</span></p>
          </div>
        </div>
      </div>
      
      <!-- Right column -->
      <div></div>
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
      courseData: {}
    };
  },
  async created() {
    this.courseId = this.$route.params.id;
    this.courseData = await this.courseStore.fetchCourseById(this.courseId);
  },
};
</script>

<style scoped></style>
