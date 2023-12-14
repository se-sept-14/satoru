<template>
  <div>
    <div class="h-screen flex mx-auto px-10">
      <div class="w-1/4">
        <div class="flex flex-col items-center justify-center">
          <img
            src="https://avatars.githubusercontent.com/u/73879363?v=4"
            alt="avatar"
            class="rounded-full w-32 h-32"
          />
          <h1 class="text-2xl font-bold text-white my-2">User Name</h1>
          <h2 class="text-xl text-white my-2">enderboi</h2>
        </div>
        <div class="flex flex-col items-center justify-center mt-10">
          <h1 class="text-2xl font-bold text-white my-2">Total courses:</h1>
          <h2 class="text-xl text-white my-2">26</h2>
        </div>
        <div class="flex flex-col items-center justify-center mt-10">
          <h1 class="text-2xl font-bold text-white my-2">Total credits:</h1>
          <h2 class="text-xl text-white my-2">84</h2>
        </div>
      </div>
      <div class="w-3/4 p-4 h-full flex flex-col">
        <div class="flex justify-between">
          <div id="welcome-message" class="flex pt-6">
            <h1 class="text-3xl font-bold text-white my-2">
              Welcome, {{ userName }}
            </h1>
          </div>

          <div id="search-box" class="flex">
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
            </div>
          </div>
        </div>

        <h2 class="text-2xl text-white my-4">Your courses</h2>
        <div class="grid auto-rows-[192px] grid-cols-3 gap-7">
          <div
            v-for="(course, i) in courses"
            :key="i"
            class="row-span-1 rounded-xl border-2 border-slate-100/10 bg-[#000101] p-5 dark:bg-[#000101] text-white"
            :class="{ 'col-span-2': i === 3 || i === 6 }"
          >
            <h2 class="text-xl font-bold">{{ course.name }}</h2>
            <p class="text-sm">{{ course.code }}</p>
            <p class="text-sm">Credits: {{ course.credits }}</p>
            <p class="text-sm">{{ course.description }}</p>
            <p class="text-sm">Corequisite: {{ course.corequisite }}</p>
            <p class="text-sm">Prerequisite: {{ course.prerequisite }}</p>
            <p class="text-sm">Instructor: {{ course.instructor }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<!-- ... rest of your component ... -->

<script>
export default {
  name: "DashboardPage",
  data() {
    return {
      userName: "username",
      courses: [
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        { id: 2, name: "Course 2", image: "url-to-course-2-image" },
        // add more courses as needed
      ],
    };
  },
};
</script>

<style scoped>
.course-card {
  border: 1px solid #ccc;
  padding: 20px;
  margin: 10px;
  border-radius: 10px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
}

.course-image {
  width: 100%;
  height: auto;
}
</style>
