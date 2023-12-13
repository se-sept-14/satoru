<template>
  <div>
    <div class="flex items-center justify-center my-8">
      <div class="relative">
        <input
          type="text"
          class="bg-black text-white border border-gray-700 rounded-full py-3 px-6 pl-14 placeholder-#000101 focus:outline-none focus:shadow-outline w-96"
          placeholder="Search..."
        />
        <div class="absolute inset-y-0 left-0 flex items-center pl-5">
          <svg
            class="w-3/4 h-4 text-gray-500 dark:text-gray-400"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 20"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
            />
          </svg>
        </div>
      </div>
    </div>'
    
  </div>
</template>

<script>
export default {
  name: "DashboardPage",
};
</script>

<style scoped></style>
