import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage.vue";
import { useAuthStore } from "@/stores/AuthStore"; // adjust the path as needed

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
    // {
    //   path: "/login",
    //   name: "LoginPage",
    //   component: () => import("@/pages/LoginPage.vue"),
    //   beforeEnter: (to, from, next) => {
    //     // Check if the user is already logged in
    //     if (store.getters["auth/isLoggedIn"]) {
    //       // If they are, redirect to the dashboard
    //       next("/dashboard");
    //     } else {
    //       // If not, continue to the login page
    //       next();
    //     }
    //   },
    // },
    // {
    //   path: "/login",
    //   name: "LoginPage",
    //   component: () => import("@/pages/LoginPage.vue"),
    //   beforeEnter: (to, from, next) => {
    //     const authStore = useAuthStore();
    //     // Check if the user is already logged in
    //     if (authStore.currentUser && authStore.currentUser.access_token) {
    //       // If they are, redirect to the dashboard
    //       next("/dashboard");
    //     } else {
    //       // If not, continue to the login page
    //       next();
    //     }
    //   },
    // },
    {
      path: "/register",
      name: "RegisterPage",
      component: () => import("@/pages/RegisterPage.vue"),
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("@/pages/ProfileTypeform.vue"),
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
