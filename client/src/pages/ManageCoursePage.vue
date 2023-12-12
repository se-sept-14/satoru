<template>
  <div class="w-[800px] h-[800px] relative bg-black mx-auto p-8">
    <div class="text-center text-white text-3xl font-bold mb-4">Manage Courses</div>
    
    <div class="mx-auto relative bg-gradient-to-br from-blue-700 to-#CD7672 rounded-xl lg:shadow-lg lg:shadow-slate-500/30 text-white">
    <div class="p-4">
        <div class="text-center text-xl font-semibold mb-2">Programming Concepts using Java <a href="#">(click to view)</a></div>
        <div class="text-center text-lg font-light">by Madhavan Mukund</div>
    </div>
    
    <div class="flex justify-between p-4 text-center">
        <div class="text-xl font-normal">3 credits</div>
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
    </div>
</div>
    <!-- Repeat similar blocks for other courses -->
    
    <div class="w-[100%] mx-auto mt-8">
    <div class="flex items-center">
    <div class="flex items-center justify-end">
        <button class="w-20 h-20 bg-gradient-to-br from-blue-700 to-#CD7672 rounded-full flex items-center hover:bg-green-600 justify-center focus:outline-none" onclick="handleButtonClick()">
            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-black">
                <span class="text-2xl">+</span>
            </div>
        </button>
    </div>
    <button class="w-[50%] h-10 relative bg-gradient-to-br from-blue-700 to-#CD7672 text-center rounded-xl flex items-center hover:bg-green-600 justify-center text-white text-xl font-normal mt-2">
        Add Course
    </button>
    </div>
</div>

  </div>
</template>