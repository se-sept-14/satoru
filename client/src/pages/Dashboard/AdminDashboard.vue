<template>
  <div>
    <navbar />

    <div class="flex flex-row text-white w-[640px] mx-auto justify-center">
      <!-- Left column -->
      <div class="flex flex-col">
        <div class="border-2 border-teal-500 p-12 rounded-md">
          <p class="font-light text-xl">Students</p>
          <p class="font-extralight text-sm italic mt-2">
            List of all enrolled students
          </p>

          <button
            class="bg-emerald-800 px-4 py-2 rounded-full mt-4"
            @click="allStudents"
          >
            View students
          </button>
        </div>
      </div>

      <!-- Right column -->
      <div class="flex flex-col ml-4">
        <div class="border-2 border-teal-500 p-12 rounded-md">
          <p class="font-light text-xl">Courses</p>
          <p class="font-extralight text-sm italic mt-2">
            List of all available courses
          </p>

          <button
            class="bg-cyan-400 text-black px-4 py-2 rounded-full mt-4"
            @click="manageCourses"
          >
            View courses
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Components
import AuthenticatedNavbarComponent from "@/components/AuthenticatedNavbarComponent.vue";

export default {
  name: "Admin Dashboard",
  components: {
    navbar: AuthenticatedNavbarComponent,
  },
  data() {
    return {};
  },
  methods: {
    manageCourses() {
      this.$router.push("/manage-course");
    },
    allStudents() {
      this.$router.push("/all-students");
    },
  },
  
};
</script>

<style scoped></style>
