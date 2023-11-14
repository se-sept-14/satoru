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
        Create a new account
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label
            for="email"
            class="block text-sm font-medium leading-6 text-white"
            >Username</label
          >
          <div class="mt-2">
            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              placeholder="Create a username ..."
              v-model="username"
              required
              class="block w-full rounded-md border-0 py-1.5 px-1.5 bg-transparent text-gray-200 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:rounded-none sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        
        <div>
          <label
            for="email"
            class="block text-sm font-medium leading-6 text-white"
            >Email address</label
          >
          <div class="mt-2">
            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              placeholder="Enter your email ..."
              v-model="email"
              required
              class="block w-full rounded-md border-0 py-1.5 px-1.5 bg-transparent text-gray-200shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:rounded-none sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-white"
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
              v-model="password"
              required
              class="block w-full rounded-md border-0 py-1.5 px-1.5 bg-transparent text-gray-200 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:rounded-none sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        
        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-white"
              >Enter Password Again</label
            >
          </div>
          <div class="mt-2">
            <input
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              placeholder="Enter your password ..."
              v-model="passwordAgain"
              required
              class="block w-full rounded-md border-0 py-1.5 px-1.5 bg-transparent text-gray-200 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:rounded-none sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            @click="register($event)"
            class="flex w-full justify-center rounded-md bg-white px-3 py-1.5 text-sm font-semibold leading-6 text-black shadow-sm hover:shadow-lg hover:shadow-yellow-200/90 hover:rounded-none focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Register
          </button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-slate-100">
        Already registered?
        <router-link
          to="/login"
          class="font-semibold leading-6 text-yellow-300 hover:text-yellow-600"
          >Login here</router-link
        >
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegisterPage",
  data() {
    return {
      email: "",
      username: "",
      password: "",
      passwordAgain: ""
    };
  },
  methods: {
    register(e) {
      e.preventDefault(); // Prevents the default behaviour of submit button (to refresh the page)

      console.log(this.email, this.username, this.password, this.passwordAgain);
    }
  }
};
</script>

<style scoped></style>
