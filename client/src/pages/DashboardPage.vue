<template>
  <div>
    <div class="h-screen flex mx-auto px-10">
      <!-- Left sidebar -->
      <div class="w-1/4 flex flex-col" v-if="username">
        <!-- Student's randomly generated profile picture -->
        <div
          id="profilePic"
          class="rounded-full w-32 h-32 my-12 self-center"
          v-html="profilePicture"
        ></div>

        <div class="flex justify-between">
          <div class="flex flex-col">
            <!-- Student's name and username -->
            <h1 class="text-2xl font-bold text-white">{{ name }}</h1>
            <h2 class="text-lg text-gray-400">{{ username }}</h2>
          </div>

          <!-- Logout button -->
          <button
            class="bg-transparent text-gray-200 rounded px-6 py-2 hover:bg-slate-900"
            @click="logout"
          >
            Logout
          </button>
        </div>

        <div class="flex mt-6">
          <div class="flex items-end">
            <h2 class="text-2xl font-semibold text-white">
              {{ courses.length }}
            </h2>
            <h1 class="text-lg text-gray-400 ml-1">courses taken</h1>
          </div>

          <div class="flex items-end ml-6">
            <h2 class="text-2xl font-semibold text-white">84</h2>
            <h1 class="text-lg text-gray-400 ml-1">credits</h1>
          </div>
        </div>
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

          <!-- Search box -->
          <div id="search-box" class="flex">
            <div class="flex items-center justify-center my-8">
              <div class="relative">
                <input
                  type="text"
                  class="bg-black text-white border border-gray-700 rounded-full py-3 px-6 pl-14 placeholder-#000101 focus:outline-none focus:shadow-outline w-96"
                  placeholder="Search ..."
                  v-model="searchQuery"
                  v-on:keyup.enter="callSearch"
                />
                <div class="absolute inset-y-0 left-0 flex items-center pl-5">
                  <svg
                    class="w-3/4 h-4 text-gray-500 dark:text-gray-400"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 20 20"
                  >
                    <path
                      stroke="currentColor"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                    />
                  </svg>
                </div>
              </div>
            </div>
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
          <div
            v-for="(course, i) in courses"
            :key="i"
            class="row-span-1 rounded-xl border-2 border-slate-100/10 bg-[#000101] p-5 dark:bg-[#000101] text-white"
            :class="{ 'col-span-2': i === 3 || i === 6 }"
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
              <p class="text-md font-extralight italic">{{ course.instructor_name }}</p>
              <div class="flex flex-col">
                <p class="text-2xl font-bold self-center">{{ course.credits }}</p>
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
import { useUserProfileStore } from "@/stores/UserProfileStore";
import { useAuthStore } from "@/stores/AuthStore";

export default {
  setup() {
    const authStore = useAuthStore();
    const userProfileStore = useUserProfileStore();

    return { authStore, userProfileStore };
  },
  name: "DashboardPage",
  data() {
    return {
      name: "",
      username: "",
      searchQuery: "",
      profilePicture: null,
      courses: [],
      userData: {},
    };
  },
  methods: {
    callSearch() {
      if (this.searchQuery.length != 0) {
        this.$router.push({
          name: "SearchPage",
          params: {
            query: this.searchQuery,
          },
        });
      } else {
        console.log("empty search query");
      }
    },

    // callProfile() {

    // },
    logout() {
      this.authStore.logout();
      this.$router.push("/login");
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
