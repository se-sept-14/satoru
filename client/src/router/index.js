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
      path: "/managecourse",
      name: "ManageCoursePage",
      component: () => import("@/pages/ManageCoursePage.vue"),
    },
    {
      path: "/addcourse",
      name: "AddCoursePage",
      component: () => import("@/pages/AddCoursePage.vue"),
    },
    {
      path: "/admincourseview",
      name: "AdminCourseView",
      component: () => import("@/pages/AdminCourseView.vue"),
    },
    {
      path: "/reccomendationpage",
      name: "ReccomendationPage",
      component: () => import("@/pages/ReccomendationPage.vue"),
    },
  ],
});
