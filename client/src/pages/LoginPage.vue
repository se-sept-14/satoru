<template>
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img
        class="mx-auto h-10 w-auto"
        src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
        alt="Your Company"
      />
      <h2
        class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white"
      >
        Sign in to your account
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label
            for="username"
            class="block text-md font-medium leading-6 text-white"
            >Username</label
          >
          <div class="mt-2">
            <input
              id="username"
              name="username"
              type="username"
              autocomplete="username"
              placeholder="Enter your username ..."
              v-model="userData.username"
              v-on:keydown="clearUsernameError"
              required
              class="block w-full rounded-md border-0 py-1.5 px-1.5 bg-transparent text-gray-200 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:rounded-none sm:text-sm sm:leading-6"
            />
            <small
              class="text-sm font-light italic text-yellow-600"
              v-if="userDataError.username"
              >Invalid username</small
            >
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-md font-medium leading-6 text-white"
              >Password</label
            >
          </div>
          <div class="mt-2">
            <input
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              placeholder="Enter your password ..."
              v-model="userData.password"
              v-on:keydown="clearPasswordError"
              required
              class="block w-full rounded-md border-0 py-1.5 px-1.5 bg-transparent text-gray-200 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:rounded-none sm:text-sm sm:leading-6"
            />
            <small
              class="text-sm font-light italic text-yellow-600"
              v-if="userDataError.password"
              >Invalid password</small
            >
          </div>
        </div>

        <div>
          <button
            type="submit"
            @click="login($event)"
            class="flex w-full justify-center rounded-md bg-white px-3 py-1.5 text-md font-semibold leading-6 text-black shadow-sm hover:shadow-md hover:shadow-yellow-400/90 hover:rounded-none focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Login
          </button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-slate-100">
        Not a member?
        <router-link
          to="/register"
          class="font-semibold leading-6 text-yellow-300 hover:text-yellow-600"
          >Register now</router-link
        >
      </p>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from "@/stores/AuthStore";

export default {
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  name: "LoginPage",
  data() {
    return {
      userData: {
        username: "",
        password: "",
      },
      userDataError: {
        username: false,
        password: false,
      },
    };
  },
  methods: {
    async login(e) {
      e.preventDefault(); // Prevents the default behaviour of submit button (to refresh the page)

      if (this.userData.username.length == 0) this.userDataError.username = true;
      if (this.userData.password.length == 0) this.userDataError.password = true;

      if (!this.userDataError.username && !this.userDataError.password) {
        const user = await this.authStore.login(this.userData);

        if (user) {
          if (typeof user == "string") {
            console.log(user);
          } else if (typeof user == "number") {
            if (parseInt(user) == 401) this.userDataError.password = true;

            if (parseInt(user) == 404) {
              this.userDataError.username = true;
              this.userDataError.password = true;
            }
          } else {
            localStorage.setItem("token_type", user.token_type);
            localStorage.setItem("access_token", user.access_token);

            this.$router.push("/dashboard");
          }
        } else {
          this.userDataError.username = true;
          this.userDataError.password = true;
        }
      }
    },
    clearUsernameError() {
      this.userDataError.username = false;
    },
    clearPasswordError() {
      this.userDataError.password = false;
    },
  },
  mounted() {
    if(this.authStore.isLoggedIn()) {
      this.$router.push("/dashboard");
      return;
    }
  },
};
</script>

<style scoped></style>
