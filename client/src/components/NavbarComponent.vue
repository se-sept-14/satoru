<template>
  <nav
    class="navbar-black sticky top-0 z-5 text-white p-4 lg:mx-40 lg:my-4 flex flex-row justify-center items-center"
  >
    <router-link
      class="basis-1/4 font-serif font-bold text-xl cursor-pointer hover:font-bold"
      to="/"
    >
      <span>{{ title }}</span>
      <span class="font-redacted ml-2">{{ title }}</span>
    </router-link>

    <div class="collapse md:visible md:basis-1/2 flex flex-row"></div>
    <button
      @click="goToRegisterPage"
      class="collapse md:visible basis-1/4 lg:basis-1/6 bg-white text-black p-2 rounded-lg shadow-md hover:shadow-lg hover:shadow-yellow-200/90 hover:text-md"
    >
      Get Started
    </button>
    <button
      @click="goToRegisterPage"
      class="collapse md:visible basis-1/4 lg:basis-1/6 bg-white text-black p-2 rounded-lg shadow-md hover:shadow-lg hover:shadow-yellow-200/90 hover:text-md"
    >
      Snow
    </button>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
  data() {
    return {
      title: "pickmycourse",
    };
  },
  methods: {
    goToRegisterPage() {
      this.$router.push("/register");
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Redacted+Script&display=swap");

.font-redacted {
  font-family: "Redacted Script", cursive;
}
</style>
