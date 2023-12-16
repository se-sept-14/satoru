<template>
  <div>
    <form
      class="flex flex-col items-center justify-center h-screen bg-black text-black"
    >
      <div class="p-8 border rounded-lg shadow-md">
        <div class="text-4xl font-bold mb-8 text-white">Add a new course</div>

        <div class="flex flex-col mb-4">
          <label for="courseName" class="text-xl text-white"
            >Course Name:</label
          >
          <input
            id="courseName"
            type="text"
            class="input-field"
            placeholder="Course Name"
          />
        </div>

        <div class="flex flex-col mb-6">
          <!-- Increase the height of the description input -->
          <label for="description" class="text-xl text-white"
            >Description:</label
          >
          <textarea
            id="description"
            class="textarea-field"
            placeholder="Course description goes here ..."
          ></textarea>
        </div>

        <div class="flex flex-col mb-4">
          <label for="prerequisite" class="text-xl text-white"
            >Prerequisite:</label
          >
          <input
            id="prerequisite"
            type="text"
            class="input-field"
            placeholder="BSCCS2001, BSCCS2003, ..."
          />
        </div>

        <div class="flex flex-col mb-4">
          <label for="taughtBy" class="text-xl text-white">Taught by:</label>
          <input
            id="taughtBy"
            type="text"
            class="input-field"
            placeholder="Professor name here ..."
          />
        </div>

        <div class="flex flex-col mb-4">
          <label for="category" class="text-xl text-white">Category:</label>
          <input
            id="category"
            type="text"
            class="input-field"
            placeholder="Programming"
          />
        </div>

        <div class="flex flex-col mb-4">
          <label for="credits" class="text-xl text-white">Credits:</label>
          <input id="credits" type="text" class="input-field" placeholder="4" />
        </div>

        <center>
          <button
            class="w-32 h-12 bg-green-600 rounded-xl text-xl font-normal text-white"
          >
            Add
          </button>
        </center>
      </div>
    </form>
  </div>
</template>

<style scoped>
.textarea-field {
  width: 100%;
  padding: 1rem; /* Adjusted padding for increased height */
  margin-top: 0.25rem;
  border: 1px solid #ccc;
  border-radius: 0.375rem;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
  resize: vertical; /* Allows vertical resizing of the textarea */
}
.input-field {
  width: 100%;
  padding: 0.75rem; /* Adjust padding for height */
  margin-top: 0.25rem;
  border: 1px solid #ccc;
  border-radius: 0.375rem;
  text: black;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.3); /* Green glow effect, adjust color as needed */
}

.container {
  max-width: 500px;
  width: 100%;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
