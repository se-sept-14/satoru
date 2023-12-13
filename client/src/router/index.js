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
      component: () => import("@/pages/RegisterPage.vue"),
    },
    {
      path: "/dashboard",
      name: "DashboardPage",
      component: () => import("@/pages/DashboardPage.vue"),
    },
    {
      path: "/manage-course",
      name: "ManageCoursePage",
      component: () => import("@/pages/ManageCoursePage.vue"),
    },
    {
      path: "/add-course",
      name: "AddCoursePage",
      component: () => import("@/pages/AddCoursePage.vue"),
    },
    {
      path: "/admin-course-view",
      name: "AdminCourseView",
      component: () => import("@/pages/AdminCourseView.vue"),
    },
    {
      path: "/recommend",
      name: "ReccomendationPage",
      component: () => import("@/pages/ReccomendationPage.vue"),
    },
  ],
});
