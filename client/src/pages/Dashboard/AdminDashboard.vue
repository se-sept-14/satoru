<template>
  <div>
    <navbar />
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
};
</script>

<style scoped></style>
