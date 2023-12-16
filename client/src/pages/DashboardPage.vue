<template>
  <div>
    <navbar />

    <div class="h-screen flex mx-24">
      <!-- Left sidebar -->
      <div class="w-1/4 flex flex-col" v-if="username">
        <!-- Student's randomly generated profile picture -->
        <div
          id="profilePic"
          class="rounded-full w-32 h-32 my-12 self-center"
          v-html="profilePicture"
        ></div>

        <div class="flex justify-around">
          <div class="flex flex-col">
            <!-- Student's name and username -->
            <h1 class="text-2xl font-bold text-white">{{ name }}</h1>
            <h2 class="text-center text-lg text-gray-400">{{ username }}</h2>
          </div>
        </div>

        <!-- Number of courses taken and credits -->
        <div class="flex mt-6 self-center">
          <div class="flex items-end">
            <h2 class="text-2xl font-semibold text-white">
              {{ courses.length }}
            </h2>
            <h1 class="text-lg text-gray-400 ml-1">courses taken</h1>
          </div>

          <div class="flex items-end ml-6">
            <h2 class="text-2xl font-semibold text-white">
              {{ courses.reduce((sum, course) => sum + course.credits, 0) }}
            </h2>
            <h1 class="text-lg text-gray-400 ml-1">credits</h1>
          </div>
        </div>

        <button
          class="text-white text-xl font-serif bg-transparent p-4 rounded-md border-2 border-slate-200 mt-20 mx-8 hover:bg-white hover:text-black"
        >
          Get recommendations
        </button>
      </div>

      <!-- Right, main section -->
      <div class="w-3/4 p-4 h-full flex flex-col">
        <div class="flex justify-between">
          <!-- Welcome message -->
          <div id="welcome-message" class="flex pt-6">
            <h1 v-if="username" class="text-3xl font-bold text-white my-2">
              Welcome
              <span class="font-semibold italic">{{ username }}</span> 👋
            </h1>
          </div>
        </div>

        <!-- Courses section -->
        <h2
          v-if="courses.length > 0"
          class="text-2xl text-white my-4 font-semibold"
        >
          Your courses 🔻
        </h2>
        <div class="grid auto-rows-[192px] grid-cols-3 gap-7">
          <!-- Each course box -->
          <div
            v-for="(course, i) in courses"
            :key="i"
            class="row-span-1 rounded-xl border-2 border-slate-100/10 bg-[#000101] p-5 dark:bg-[#000101] text-white cursor-pointer hover:scale-105 transform transition duration-300"
            :class="{ 'col-span-2': i === 3 || i === 6 }"
            @click="viewCourse(course.id)"
          >
            <div class="flex items-end mb-4">
              <h2 class="text-xl font-bold">{{ course.name }}</h2>
              <p class="text-xs ml-2 font-extralight italic">
                {{ course.code }}
              </p>
            </div>

            <div class="flex mb-1">
              <p class="text-xs">
                Corequisite:
                <span class="text-md italic font-bold">{{
                  course.corequisite
                }}</span>
              </p>
              <p class="text-xs ml-2">
                Prerequisite:
                <span class="text-md italic font-bold">{{
                  course.prerequisites
                }}</span>
              </p>
            </div>

            <div class="flex justify-between items-end mt-8">
              <p class="text-md font-extralight italic">
                {{ course.instructor_name }}
              </p>
              <div class="flex flex-col">
                <p class="text-2xl font-bold self-center">
                  {{ course.credits }}
                </p>
                <p class="text-xs font-extralight text-gray-300">Credits</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Stores
import { useAuthStore } from "@/stores/AuthStore";
import { useUserProfileStore } from "@/stores/UserProfileStore";

// Components
import AuthenticatedNavbarComponent from "@/components/AuthenticatedNavbarComponent.vue";

export default {
  setup() {
    const authStore = useAuthStore();
    const userProfileStore = useUserProfileStore();

    return { authStore, userProfileStore };
  },
  name: "DashboardPage",
  components: {
    'navbar': AuthenticatedNavbarComponent
  },
  data() {
    return {
      name: "",
      username: "",
      profilePicture: null,
      courses: [],
      userData: {},
    };
  },
  methods: {
    logout() {
      this.authStore.logout();
      this.$router.push("/login");
    },
    viewCourse(id) {
      this.$router.push({
        name: "Course details",
        params: {
          id: id,
        },
      });
    },
  },
  async mounted() {
    // Check if the user is logged in or not
    if (!this.authStore.isLoggedIn()) {
      this.$router.push("/login");
      return;
    }

    // If they are an admin, redirect them to their dashboard
    if (await this.authStore.isAdmin()) {
      this.$router.push("/manage-course");
      return;
    } else {
      const studentProfile = await this.userProfileStore.fetchProfile();

      if (studentProfile) {
        const { user, name } = studentProfile;
        this.username = `@${user["username"]}`;
        this.name = name;

        this.courses = await this.userProfileStore.fetchStudentCourses();

        const pfpSvg = await this.userProfileStore.fetchProfilePicture(
          this.username
        );

        if (pfpSvg != {} || pfpSvg != 404) {
          this.profilePicture = pfpSvg;
        } else {
          if (pfpSvg == {}) {
            this.$router.push("/profile");
          }
        }
      } else {
        this.$router.push("/profile");
      }
    }
  },
};
</script>

<style scoped>
.course-card {
  border: 1px solid #ccc;
  padding: 20px;
  margin: 10px;
  border-radius: 10px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
}

.course-image {
  width: 100%;
  height: auto;
}
</style>
