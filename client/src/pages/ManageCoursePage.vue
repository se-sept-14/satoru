<template>
  <div class="w-[800px] h-[800px] relative bg-black mx-auto p-8">
    <div class="text-center text-white text-3xl font-bold mb-4">Manage Courses</div>
    <br>
    <div v-for="(course, index) in courses.data" :key="course.id">
    <div  class="mx-auto relative bg-gradient-to-b from-gray-900 to-gray-600 rounded-xl lg:shadow-lg lg:shadow-slate-500/30 text-white">
    
    <div class="p-4">
        <div class="text-center text-xl font-semibold mb-2">{{course.name}}<a href="#">(click to view)</a></div>
        <div class="text-center text-lg font-light">{{course.instructor_name}}</div>
    </div>
    
    <div class="flex justify-between p-4 text-center">
        <div class="text-xl font-normal">{{course.credits}} credits</div>
        <div class="text-xl font-normal">199 students</div>
        <div class="flex">
            <div class="w-5 h-5 bg-yellow-400 clip-star"></div>
            <div class="text-xl font-normal ml-2">4.5</div>
        </div>
        <div class="text-xl font-normal">Register by:<br>18 December 2023</div>
    </div>
    
    <div class="flex justify-between p-4">
        <button class="w-32 h-12 bg-green-500 rounded-xl hover:bg-green-600 mx-auto text-white text-lg font-normal">Manage</button>
        <button class="w-32 h-12 bg-red-500 rounded-xl hover:bg-red-600 mx-auto text-white text-lg font-normal">Delete</button>
    </div><br>
    
</div><br>
</div>
  
    
    <div class="w-[100%] mx-auto mt-8 item-right">
    <div class="flex flex-col-2 items-center">
    <button class="w-[20%] h-10 relative bg-gradient-to-b from-gray-900 to-gray-600 text-center rounded-xl flex items-center hover:bg-green-600 justify-center text-white text-xl font-normal  mr-5 p-5">
        Add Course
    </button>
    <div class="flex items-center justify-end">
        <button class="w-20 h-20 bg-gradient-to-b from-gray-900 to-gray-600 rounded-full flex items-center hover:bg-green-600 justify-center focus:outline-none" onclick="handleButtonClick()">
            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-black">
                <span class="text-2xl">+</span>
            </div>
        </button>
    </div>
    
</div>

</div><br><br><br>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      courses: [],
    };
  },
  async mounted() {
    const response = await axios.get("https://api.pickmycourse.online/api/course/all", {
      headers: {
        Authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZW1haWwiOiJlbmRlcmJvaUBwaWNrbXljb3Vyc2Uub25saW5lIiwiaXNfYWRtaW4iOjAsImV4cCI6MTcwMjM5MTU5OH0.dXgUS4Lz2slUwRwOWbMCzKjp9dKIHlrrUFFl3HasfJ0`,
      },
    });
    this.courses = response.data;
    console.log(response.data);
  },
  // ...other methods and functions
};
</script>