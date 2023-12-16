<template>
  <div>
    <div class="flex flex-wrap mx-3 mb-5">
      <div
        class="px-3 mb-6 mx-auto w-11/12 bg-transparent text-white rounded-xl"
      >
        <div
          class="sm:flex items-stretch justify-between grow lg:mb-0 py-5 px-5"
        >
          <div class="flex flex-row flex-wrap justify-center mb-5 mr-3 lg:mb-0">
            <span
              class="my-0 flex text-dark font-semibold text-[1.35rem]/[1.2] flex-col justify-center"
            >
              {{ $route.name }}
            </span>

            <span
              class="my-0 flex font-extralight text-md justify-center items-center ml-8 text-emerald-100 italic cursor-pointer"
              @click="redirectDashboard"
            >
              <span class="hover:underline">go to dashboard</span>
              <i class="fa-solid fa-location-arrow ml-2 text-xs"></i>
            </span>
          </div>

          <div class="flex items-center lg:shrink-0 lg:flex-nowrap">
            <!-- Search bar in the Navbar -->
            <div class="relative flex items-center lg:ml-4 sm:mr-0 mr-2">
              <span class="absolute ml-4 leading-none -translate-y-1/2 top-1/2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                  ></path>
                </svg>
              </span>

              <input
                class="block w-full min-w-[70px] py-3 pl-12 pr-4 text-base font-medium leading-normal bg-transparent border border-solid outline-none appearance-none placeholder:text-secondary-dark peer text-stone-200 border-stone-200 bg-clip-padding rounded-full"
                placeholder="Search..."
                type="text"
                v-model="searchQuery"
                v-on:keyup.enter="callSearch"
              />
            </div>

            <!-- Logout button -->
            <div
              class="relative flex items-center ml-2 lg:ml-4"
              @click="logout"
            >
              <a
                href="javascript:void(0)"
                class="flex items-center justify-center w-12 h-12 text-base font-medium leading-normal text-center align-middle transition-colors duration-150 ease-in-out bg-transparent shadow-none cursor-pointer text-stone-500 border-stone-200 hover:text-primary active:text-primary focus:text-primary"
              >
                <i class="fa-solid fa-right-from-bracket text-white"></i>
              </a>
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

export default {
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  name: "AuthenticatedNavbar",
  data() {
    return {
      searchQuery: "",
      dashboard: "/dashboard",
    };
  },
  methods: {
    logout() {
      this.authStore.logout();
      this.$router.push("/login");
    },
    callSearch() {
      if (this.searchQuery.length != 0) {
        this.$router.push({
          name: "Search Courses",
          params: { query: this.searchQuery },
        });
      }
    },
    redirectDashboard() {
      this.$router.push(this.dashboard);
    },
  },
  async mounted() {
    const isAdmin = await this.authStore.isAdmin();
    this.dashboard = isAdmin ? "/admin-dashboard" : "/dashboard";
  },
};
</script>

<style scoped></style>
