<template>
<br><br><br><br><br>
    <div class="text-4xl font-bold mb-8 bg-black from-black to-black p-4 w-full fixed top-0">
    
    </div><br><br><br>
  <form class="flex flex-col items-center justify-center h-screen bg-black text-black">
    <div class="container bg-gradient-to-b from-gray-900 to-gray-600 p-8 rounded-lg shadow-md">
      <center><div class="text-4xl font-bold mb-8 text-white">Add a new course</div></center>

      <div class="flex flex-col mb-4">
        <label for="courseName" class="text-xl text-white">Course Name:</label>
        <input v-model="courseData.name" id="courseName" type="text" class="input-field" placeholder="Course Name" required />
      </div>

      <div class="flex flex-col mb-6"> <!-- Increase the height of the description input -->
        <label for="description" class="text-xl text-white ">Description:</label>
        <textarea v-model="courseData.description" id="description" class="textarea-field" placeholder="Course description goes here ..."></textarea>
      </div>

      <div class="flex flex-col mb-4">
        <label for="prerequisite" class="text-xl text-white">Prerequisite:</label>
        <input v-model="courseData.prerequisites" id="prerequisite" type="text" class="input-field" placeholder="BSCCS2001, BSCCS2003, ..." required />
      </div>
      <div class="flex flex-col mb-4">
        <label for="corequisite" class="text-xl text-white">corequisite:</label>
        <input v-model="courseData.corequisite" id="corequisite" type="text" class="input-field" placeholder="BSCCS2001, BSCCS2003, ..." required />
      </div>

      <div class="flex flex-col mb-4">
        <label for="taughtBy" class="text-xl text-white">Taught by:</label>
        <input v-model="courseData.instructor_name" id="taughtBy" type="text" class="input-field" placeholder="Professor name here ..." required />
      </div>

      <div class="flex flex-col mb-4">
        <label for="category" class="text-xl text-white">Category:</label>
        <input v-model="courseData.code" id="category" type="text" class="input-field" placeholder="Programming" required />
      </div>
      <div class="flex flex-col mb-4">
        <label for="tags" class="text-xl text-white">Tags:</label>
        <input v-model="newTag" type="text" class="input-field" placeholder="Programming" id="tags" @keyup.enter="addTag" />
        <ul>
          <li v-for="(tag, index) in courseData.tags" :key="index">
            {{ tag }} 
            <button type="button" class="w-32 h-12 bg-green-600 rounded-xl text-xl font-normal text-white" @click="removeTag(index)">Remove</button>
          </li>
        </ul>
      </div>




      <div class="flex flex-col mb-4">
        <label for="credits" class="text-xl text-white">Credits:</label>
        <input v-model="courseData.credits" id="credits" type="text" class="input-field" placeholder="4" required />
      </div>

      <center><button type="submit" class="w-32 h-12 bg-green-600 rounded-xl text-xl font-normal text-white">Add</button></center>
    </div>
  </form><br><br><br><br><br>
</template>


<script>
export default {
  data() {
    return {
      courseData: {
        name: "",
        code: "",
        price: 0,
        credits: 0,
        description: "",
        corequisite: "",
        prerequisites: "",
        hours_per_week: "",
        instructor_name: "",
        instructor_picture: "",
        tags: [],
      },
      newTag: "",
    };
  },
    beforeMount() {
    // Check for the existence of the access token in local storage
    const accessToken = localStorage.getItem("access_token");

    // If access token is not present, redirect to the login component
    if (!accessToken) {
      this.$router.push("/login"); // Adjust the route based on your setup
    }
  },

  // Other component options and methods can be added here
    methods: {
    async addCourse() {
      try {
        // Assuming you have an API endpoint for adding courses
        const response = await this.$axios.post("https://api.pickmycourse.online/api/course", this.courseData);

        // Handle the response as needed
        console.log("Course added successfully:", response.data);

        // You may want to redirect the user or perform other actions after adding the course
      } catch (error) {
        console.error("Error adding course:", error.response.data);
        // Handle errors, show a message, etc.
      }
    },
        addTag() {
      if (this.newTag.trim() !== "") {
        this.courseData.tags.push(this.newTag.trim());
        this.newTag = ""; // Clear the input after adding a tag
      }
    },
    removeTag(index) {
      this.courseData.tags.splice(index, 1);
    },
  },





};
</script>

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
    text:black;
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
