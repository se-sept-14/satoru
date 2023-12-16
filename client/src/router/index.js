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
      component: () => import("@/pages/Auth/LoginPage.vue"),
    },
    {
      path: "/register",
      name: "Register",
      component: () => import("@/pages/Auth/RegisterPage.vue"),
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("@/pages/ProfileTypeform.vue"),
    },
    {
      path: "/dashboard",
      name: "Dashboard",
      component: () => import("@/pages/Dashboard/DashboardPage.vue"),
    },
    {
      path: "/admin-dashboard",
      name: "Admin Dashboard",
      component: () => import("@/pages/Dashboard/AdminDashboard.vue"),
    },
    {
      path: "/search/:query",
      name: "Search Courses",
      component: () => import("@/pages/Courses/Search.vue"),
    },
    {
      path: "/manage-course",
      name: "Admin Manage Courses",
      component: () => import("@/pages/Courses/Manage.vue"),
    },
    {
      path: "/add-course",
      name: "Admin Add Course",
      component: () => import("@/pages/Courses/AddCourse.vue"),
    },
    {
      path: "/admin-course-view",
      name: "Admin Course details",
      component: () => import("@/pages/AdminCourseView.vue"),
    },
    {
      path: "/recommend/:numberOfCourses",
      name: "Recommended Courses",
      component: () => import("@/pages/Courses/Recommend.vue"),
    },
    {
      path: "/course/:id",
      name: "Course details",
      component: () => import("@/pages/Courses/View.vue"),
    },
  ],
});
