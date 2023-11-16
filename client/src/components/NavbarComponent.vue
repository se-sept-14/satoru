<template>
  <nav
    class="lg:sticky top-4 z-10 text-white p-3 lg:mx-80 lg:mt-4 lg:rounded-xl lg:shadow-lg lg:shadow-slate-500/30 flex flex-row justify-center items-center"
    style="background-color: #00050d"
  >
    <router-link
      class="basis-1/2 lg:basis-1/4 font-sans text-lg cursor-pointer font-medium hover:font-bold mx-2"
      to="/"
      >recommender system</router-link
    >
    <div class="collapse lg:visible basis-1/2 flex flex-row">
      <router-link to="/" class="collapse lg:visible mx-3 hover:underline"
        >Discover Courses</router-link
      >
      <router-link to="/" class="mx-3 hover:underline">My Courses</router-link>
      <router-link to="/" class="mx-3 hover:underline"
        >Recommendations</router-link
      >
    </div>
    <button
      @click="goToRegisterPage"
      class="basis-1/6 bg-white text-black p-2 rounded-lg shadow-md hover:shadow-lg hover:shadow-yellow-200/90 hover:text-md"
    >
      Register
    </button>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
  methods: {
    goToRegisterPage() {
      this.$router.push("/register");
    },
  },
};
</script>
