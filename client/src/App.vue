<template>
  <div>
    <NavbarComponent v-if="showNavbar" />

    <router-view></router-view>
  </div>
</template>

<script>
import NavbarComponent from "@/components/NavbarComponent.vue";

export default {
  components: {
    NavbarComponent,
  },
  data() {
    return {
      showNavbar: true,
    };
  },
  watch: {
    $route(to, from) {
      // Watch the route for `/login` and `/register`
      this.showNavbar = !["LoginPage", "RegisterPage"].includes(to.name); // Disable the NavbarComponent on those pages
    },
  },
};
</script>

<style scoped></style>
