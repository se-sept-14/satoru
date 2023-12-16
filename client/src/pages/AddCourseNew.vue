<template>
  <div>
    <div class="mx-auto bg-black text-white p-12 w-[960px]">
      <h1 class="text-3xl font-bold mb-8">Add a new course</h1>
      <form class="flex space-y-6">
        <div class="flex flex-col basis-1/2 mx-4">
          <div class="my-4">
            <label for="courseName" class="block text-lg font-medium mb-2"
              >Course Name:</label
            ><input
              id="courseName"
              placeholder="Course Name"
              class="w-full bg-transparent text-white border border-gray-600 p-3 rounded-md"
              type="text"
              name="courseName"
            />
          </div>
          <div class="my-4">
            <label for="description" class="block text-lg font-medium mb-2"
              >Description:</label
            ><textarea
              id="description"
              name="description"
              placeholder="Course description goes here ..."
              class="w-full bg-transparent text-white border border-gray-600 p-3 rounded-md h-24"
            ></textarea>
          </div>
          <div class="my-4">
            <label for="prerequisite" class="block text-lg font-medium mb-2"
              >Prerequisite:</label
            ><input
              id="prerequisite"
              placeholder="BSCSC2001, BSCSC2003, ..."
              class="w-full bg-transparent text-white border border-gray-600 p-3 rounded-md"
              type="text"
              name="prerequisite"
            />
          </div>
          <div class="flex items-center my-4">
            <div class="flex-grow">
              <label for="taughtBy" class="block text-lg font-medium mb-2"
                >Taught by:</label
              ><input
                id="taughtBy"
                placeholder="Professor name here ..."
                class="w-full bg-transparent text-white border border-gray-600 p-3 rounded-md"
                type="text"
                name="taughtBy"
              />
            </div>
          </div>
        </div>

        <div class="flex flex-col basis-1/2 mx-4">
          <div class="flex items-center">
            <div class="flex-grow my-4">
              <label for="taughtBy" class="block text-lg font-medium mb-2"
                >Instuctor Profile picture :</label
              ><input
                id="taughtBy"
                placeholder="Professor pic here ..."
                class="w-full bg-transparent text-white border border-gray-600 p-3 rounded-md"
                type="text"
                name="taughtBy"
              />
            </div>
          </div>

          <div class="my-4">
            <label for="category" class="block text-lg font-medium mb-2"
              >Category:</label
            ><select
              id="category"
              name="category"
              class="w-full bg-transparent text-white border border-gray-600 p-3 rounded-md appearance-none"
            >
              <option>Programming</option>
            </select>
          </div>
          <div class="my-4">
            <label for="credits" class="block text-lg font-medium mb-2"
              >Credits:</label
            ><input
              id="credits"
              placeholder="4"
              class="w-full bg-transparent text-white border border-gray-600 p-3 rounded-md"
              type="number"
              name="credits"
            />
          </div>
          <button
            class="my-4 inline-flex items-center justify-center text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 h-10 w-full text-black bg-white hover:bg-slate-700 p-3 rounded-md"
          >
            Add
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script></script>
