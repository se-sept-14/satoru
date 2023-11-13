<template>
  <div>
    <NavbarComponent />

    <router-view></router-view>
  </div>
</template>

<script>
import NavbarComponent from '@/components/NavbarComponent.vue';

export default {
  components: {
    NavbarComponent
  }
}
</script>

<style scoped></style>
