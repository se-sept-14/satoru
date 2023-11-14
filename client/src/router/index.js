import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage.vue";

// Vue router docs: https://router.vuejs.org/guide/
export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/login",
      name: "LoginPage",
      component: () => import("@/pages/LoginPage.vue"),
    },
    {
      path: "/register",
      name: "RegisterPage",
      component: () => import("@/pages/RegisterPage.vue")
    }
  ],
});
