<template>
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

        <button
          class="bg-emerald-600 mt-16 p-4 rounded-md font-serif text-md self-center"
        >
          <i class="fa-solid fa-cart-shopping"></i> <span>Add to cart</span>
        </button>
      </div>
    </div>

    <!-- Lower section, 2 sections -->
    <div class="flex flex-row mt-24 justify-around">
      <!-- Left column -->
      <div class="flex flex-col text-white">
        <p class="font-serif font-bold text-3xl">Reviews</p>
        <p class="font-serif font-extralight italic">
          {{ courseReviews.length }} reviews
        </p>

        <div class="my-4"></div>
        <div
          class="flex flex-row my-2 justify-between"
          v-for="(courseReview, i) in courseReviews"
          :key="courseReview.id"
        >
          <p class="basis-4/5">{{ courseReview.content }}</p>
          <span class="flex flex-row basis-1/5">
            <p class="mr-1">{{ courseReview.ratings }}</p>
            <i class="fa-solid fa-star text-sm mr-4"></i>

            <i class="fa-solid fa-flag" v-if="courseReview.is_flagged"></i>
            <i class="fa-regular fa-flag" v-else></i>
          </span>
        </div>
      </div>

      <!-- Right column -->
      <div class="flex flex-col text-white">
        <p class="text-4xl font-bold font-serif">
          {{
            // Calculate the average ratings
            (
              courseReviews.reduce(
                (sum, courseReview) => sum + courseReview.ratings,
                0
              ) / courseReviews.length
            ).toFixed(2)
          }}
          <i class="fa-solid fa-star text-sm"></i>
        </p>
        <p class="text-lg font-extralight">Average rating</p>
      </div>
    </div>
  </div>
</template>

<script>
import { useCourseStore } from "@/stores/courseStore";
import { useReviewStore } from "@/stores/ReviewStore";

export default {
  setup() {
    const courseStore = useCourseStore();
    const reviewStore = useReviewStore();
    return { courseStore, reviewStore };
  },
  name: "ViewCourse",
  data() {
    return {
      courseId: -1,
      courseData: {},
      courseReviews: [],
    };
  },
  async created() {
    this.courseId = this.$route.params.id;
    this.courseData = await this.courseStore.fetchCourseById(this.courseId);
    this.courseReviews = await this.reviewStore.getReviewsByCourseId(
      this.courseId
    );
  },
};
</script>

<style scoped></style>
