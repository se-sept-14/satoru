<template>
  <div>
    <navbar />

    <div class="flex flex-col w-[720px] mx-auto text-white">
      <h1 class="font-serif text-3xl font-semibold mb-6">All students</h1>

      <div class="flex my-4 items-center border-2 border-slate-700 px-4 py-3 rounded-md" v-for="(student, index) in students" :key="student.id">
        <i class="fa-solid fa-graduation-cap mr-4 text-2xl self-end"></i>
        
        <div class="flex flex-col">
          <p class="text-sm italic font-extralight">Name</p>
          <span class="text-2xl not-italic font-semibold">{{ student.name }}</span>
        </div>

        
      </div>
    </div>
  </div>
</template>

<script>
// Stores
import { useAuthStore } from "@/stores/AuthStore";
import { useAdminStore } from "@/stores/AdminStore";
import { useUserProfileStore } from "@/stores/UserProfileStore";

// Components
import AuthenticatedNavbarComponent from "@/components/AuthenticatedNavbarComponent.vue";

export default {
  setup() {
    const authStore = useAuthStore();
    const adminStore = useAdminStore();
    const userProfileStore = useUserProfileStore();

    return { adminStore, authStore, userProfileStore };
  },
  name: "ViewAllStudents",
  data() {
    return {
      students: [],
      studentProfiles: []
    };
  },
  components: {
    navbar: AuthenticatedNavbarComponent,
  },
  async mounted() {
    const isAdmin = await this.authStore.isAdmin();
    if(!isAdmin) this.$router.push("/login");

    const data = await this.adminStore.fetchAllStudents();
    for(let i = 0; i < data.length; ++i) {
      if(Object.keys(data[i]).length == 0 && !data[i].user) continue;

      this.students.push(data[i]);
      const studentData = await this.userProfileStore.fetchProfileById();
      console.log(studentData);
    }
  },
};
</script>

<style scoped></style>
