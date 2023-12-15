<template>
  <div class="container px-16">
    <div
      :class="{
        // 'mt-24 grid grid-cols-2 gap-4': courses.length > 3,
        'mt-24': courses.length <= 3,
      }"
    >
      <div
        v-for="course in courses"
        :key="course.id"
        class="max-w-2xl mx-auto mt-6 p-6 rounded-xl border-2 border-slate-100/10 bg-[#000101] text-white shadow-lg transition-all duration-200 hover:scale-105"
      >
        <div class="flex justify-between items-start">
          <div class="flex flex-col">
            <div class="mb-4">
              <p class="font-semibold text-2xl mb-1">
                Programming Concepts using Java
              </p>
              <p class="font-light text-lg text-gray-400">by Madhavan Mukund</p>
            </div>
            <p class="text-gray-400 mb-6">
              This course covers the basics of programming in Java. Topics
              include variables, arrays, loops, functions, and object-oriented
              programming.
            </p>
          </div>
          <img
            class="w-20 h-20 object-cover rounded-full ml-6"
            src="https://study.iitm.ac.in/ds/assets/img/academics/instructors/9003_1x.jpg"
          />
        </div>
        <div class="flex justify-between items-center w-full mt-6">
          <div class="text-xl font-light">3 credits</div>
          <div class="text-xl font-light">199 students</div>
          <div class="flex items-center">
            <div class="w-4 h-4 bg-yellow-400 clip-star"></div>
            <div class="text-xl font-light ml-2">4.5</div>
          </div>
          <button
            class="bg-slate-100 text-black rounded px-6 py-2 transition-colors duration-200 hover:bg-slate-200 hover:text-white"
          >
            add to cart
          </button>
        </div>
      </div>

      <!-- ============== -->
      <div
        v-for="course in courses"
        :key="course.id"
        class="max-w-2xl mx-auto mt-6 p-6 rounded-xl border-2 border-slate-100/10 bg-[#000101] text-white shadow-lg transition-all duration-200 hover:scale-105"
      >
        <div class="flex flex-col items-start">
          <div class="mb-4">
            <p class="font-semibold text-2xl mb-1">
              Programming Concepts using Java
            </p>
            <p class="font-light text-lg text-gray-400">by Madhavan Mukund</p>
          </div>
          <p class="text-gray-400 mb-6">
            This course covers the basics of programming in Java. Topics include
            variables, arrays, loops, functions, and object-oriented
            programming.
          </p>
          <div class="flex justify-between items-center w-full mt-6">
            <div class="text-xl font-light">3 credits</div>
            <div class="text-xl font-light">199 students</div>
            <div class="flex items-center">
              <div class="w-4 h-4 bg-yellow-400 clip-star"></div>
              <div class="text-xl font-light ml-2">4.5</div>
            </div>
            <button
              class="bg-slate-100 text-black rounded px-6 py-2 transition-colors duration-200 hover:bg-slate-200 hover:text-white"
            >
              add to cart
            </button>
          </div>
        </div>
      </div>

      <!-- ================================checkpoint -->
      <div
        v-for="course in courses"
        :key="course.id"
        class="max-w-2xl mx-auto mt-6 p-6 rounded-xl border-2 border-slate-100/10 bg-[#000101] text-white shadow-lg"
      >
        <div class="flex flex-col">
          <div class="mb-4">
            <p class="font-semibold text-2xl mb-1">
              Programming Concepts using Java
            </p>
            <p class="font-light text-lg text-gray-400">by Madhavan Mukund</p>
          </div>
          <div class="flex justify-between items-center mt-6">
            <div class="text-xl font-light">3 credits</div>
            <div class="text-xl font-light">199 students</div>
            <div class="flex items-center">
              <div class="w-4 h-4 bg-yellow-400 clip-star"></div>
              <div class="text-xl font-light ml-2">4.5</div>
            </div>
            <button class="bg-slate-100 text-black rounded px-6 py-2">
              add to cart
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchPage",
  data() {
    return {
      userName: "username",
      courses: [
        { id: 1, name: "Course 1", image: "url-to-course-1-image" },
        //   { id: 2, name: "Course 2", image: "url-to-course-2-image" },
        //   { id: 3, name: "Course 3", image: "url-to-course-3-image" },
      ],
    };
  },
};
</script>
<!-- <template>
  <div class="container px-16">
    <div
      :class="{
        'mt-24 grid grid-cols-2 gap-4': courses.length > 3,
        'mt-24': courses.length <= 3,
      }"
    >
      <div
        v-for="course in courses"
        :key="course.id"
        class="max-w-2xl mx-auto mt-4 p-5 rounded-xl border-2 border-slate-100/10 bg-[#000101] text-white"
      >
        <div class="flex flex-col">
          <div class="">
            <p class="font-medium text-xl">Programming Concepts using Java</p>
            <p class="font-thin">by Madhavan Mukund</p>
          </div>
          <div class="">
            <p>122 students</p>
            <p class="text-gray-500 text-base">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. class="
              bg-black text-white rounded overflow-hidden shadow-lg"> bg-black
              text-white rounded overflow-hidden shadow-lg"> bg-black text-white
              rounded overflow-hidden shadow-lg">
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template> -->
