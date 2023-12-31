<template>
  <div>
    <navbar />

    <div class="flex flex-col w-8/12 mx-auto">
      <!-- Upper section, 2 columns -->
      <div class="flex flex-row mt-4 justify-around">
        <!-- Left column -->
        <div class="flex flex-col px-4">
          <p class="text-3xl font-bold font-serif text-emerald-300">
            {{ courseData.name }} <i class="fa-solid fa-pen-to-square"></i>
          </p>
          <p class="text-lg font-light text-white w-[768px] mt-6">
            {{ courseData.description }} <i class="fa-solid fa-pen-to-square"></i>
          </p>

          <div class="flex flex-row text-white text-lg justify-between mt-12">
            <div class="flex flex-col">
              <p class="font-semibold">
                Prerequisites
                <span class="font-extralight text-2xl">{{
                  courseData.prerequisites
                }} <i class="fa-solid fa-pen-to-square"></i></span>
              </p>
              <p class="font-semibold">
                Corerequisites
                <span class="font-extralight text-2xl">{{
                  courseData.corequisite
                }} <i class="fa-solid fa-pen-to-square"></i></span>
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
                  >{{ courseData.hours_per_week }} hours <i class="fa-solid fa-pen-to-square"></i></span
                >
              </p>
              <p class="font-semibold">
                Price
                <span class="font-extralight text-2xl"
                  >₹{{ courseData.price }}/- <i class="fa-solid fa-pen-to-square"></i></span
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
          /> <i class="fa-solid fa-pen-to-square text-white"></i>

          <p
            class="font-extralight text-xl text-center text-gray-400 mt-2 font-serif"
          >
            {{ courseData.instructor_name }} <i class="fa-solid fa-pen-to-square"></i>
          </p>
        </div>
      </div>

      <!-- Lower section, 2 sections -->
      <div class="flex flex-row mt-24 justify-around basis-8/12">
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
            <p class="w-[500px]">{{ courseReview.content }}</p>
            <span class="flex flex-row basis-1/5">
              <p class="mr-1">{{ courseReview.ratings }}</p>
              <i class="fa-solid fa-star text-sm mr-4"></i>

              <!-- Flagged review -->
              <i class="fa-solid fa-flag" v-if="courseReview.is_flagged"></i>
              <!-- Not flagged review -->
              <i
                class="fa-regular fa-flag cursor-pointer hover:text-yellow-300"
                v-else
                @click="flagReview(courseReview.id, i)"
              ></i>

              <!-- Delete icon -->
              <i v-if="courseReview.is_flagged" class="fa-solid fa-trash ml-4 text-red-500 cursor-pointer" @click="deleteReview(courseReview.id)"></i>
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

      <!-- Empty div to add margin at the bottom -->
      <div class="my-8"></div>
    </div>
  </div>
</template>

<script>
// Stores
import { useCourseStore } from "@/stores/courseStore";
import { useReviewStore } from "@/stores/ReviewStore";

// Components
import AuthenticatedNavbarComponent from "@/components/AuthenticatedNavbarComponent.vue";

export default {
  setup() {
    const courseStore = useCourseStore();
    const reviewStore = useReviewStore();
    return { courseStore, reviewStore };
  },
  name: "EditCourse",
  components: {
    navbar: AuthenticatedNavbarComponent,
  },
  data() {
    return {
      courseId: -1,
      courseData: {},
      courseReviews: [],
      disableRegistration: false,
    };
  },
  methods: {
    async flagReview(id, idx) {
      const data = await this.reviewStore.flagReviewById(id);

      if (data.message.length != 0) {
        this.courseReviews[idx].is_flagged = true;
      }
    },
    async mapStudentCourse() {
      const data = await this.courseStore.studentCourseMapById(this.courseId);
      if (data.message.length != 0) {
        this.disableRegistration = true;
        this.$router.push("/dashboard");
      }
    },
    async deleteReview(reviewId) {
      const data = await this.reviewStore.deleteReviewById(reviewId);

      if(data.message.length != 0) {
        const idx = this.courseReviews.findIndex(review => review.id === reviewId);

        if(idx !== -1) {
          this.courseReviews.splice(idx, 1);
        }
      }
    }
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
