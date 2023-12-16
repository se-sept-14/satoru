import HomePage from "@/pages/HomePage.vue";
import { createRouter, createWebHistory } from "vue-router";

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
      name: "Login",
      component: () => import("@/pages/LoginPage.vue"),
    },
    {
      path: "/register",
      name: "Register",
      component: () => import("@/pages/RegisterPage.vue"),
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("@/pages/ProfileTypeform.vue"),
    },
    {
      path: "/dashboard",
      name: "Dashboard",
      component: () => import("@/pages/DashboardPage.vue"),
    },
    {
      path: "/search/:query",
      name: "Search",
      component: () => import("@/pages/SearchPage.vue"),
    },
    {
      path: "/manage-course",
      name: "AdminManageCourses",
      component: () => import("@/pages/Courses/Manage.vue"),
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
    {
      path: "/course/:id",
      name: "Course details",
      component: () => import("@/pages/Courses/View.vue"),
    },
  ],
});
