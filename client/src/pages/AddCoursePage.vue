<template>
<br><br><br><br><br>
    <div class="text-4xl font-bold mb-8 bg-black from-black to-black p-4 w-full fixed top-0">
    
    </div><br><br><br><br><br><br><br><br><br><br>
  <form @submit.prevent="addCourse" class="flex flex-col items-center bottom-0 left-0 right-0 justify-center h-screen bg-black text-black ">
    <div class="container bg-gradient-to-b from-gray-900 to-gray-600 p-8 rounded-lg shadow-md">
      <div class="text-4xl font-bold mb-8 text-white text-center">Add a new course</div>

      <div class="flex flex-col mb-4">
        <label for="courseName" class="text-xl text-white">Course Name:</label>
        <input v-model="courseData.name" id="courseName" type="text" class="input-field" placeholder="Course Name" required />
      </div>

      <div class="flex flex-col mb-6"> <!-- Increase the height of the description input -->
        <label for="description" class="text-xl text-white ">Description:</label>
        <textarea v-model="courseData.description" id="description" class="textarea-field" placeholder="Course description goes here ..."></textarea>
      </div>
      <div class="flex flex-col mb-4">
        <label for="prerequisite" class="text-xl text-white">Course price in Rs::</label>
        <input v-model="courseData.price" id="courseprice" type="text" class="input-field" inputmode="numeric" placeholder="10000" required />
      </div>
      <div class="flex flex-col mb-4">
        <label for="prerequisite" class="text-xl text-white">Course Code:</label>
        <input v-model="courseData.code" id="coursecode" type="text" class="input-field" placeholder="BSCCS2001" required />
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
    <label for="imageInput">Select an Image:</label>
    <input
      type="file"
      id="imageInput"
      accept="image/*"
      @change="handleImageChange"
    />
    
    <div v-if="imageBase64">
      <img :src="imageBase64" alt="Selected Image" style="max-width: 100%;" />
    </div>

    <button @click="saveImage">Save Image</button>
  </div>






      <div class="flex flex-col mb-4">
        <label for="taughtBy" class="text-xl text-white">Hrs per week:</label>
        <input v-model="courseData.hours_per_week" id="hours_per_week" type="text" class="input-field" placeholder="10hrs" required />
      </div>

      <div class="flex flex-col mb-4">
        <label for="tags" class="text-xl text-white">Tags:</label>
        <input v-model="newTag" type="text" class="input-field" placeholder="Programming" id="tags" @keydown.enter.prevent="addTag" />
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
      
     <button type="submit" class="w-32 h-12 text-center bg-green-600 rounded-xl text-xl font-normal text-white">Add</button>
    </div>
  </form><br><br><br><br><br>
</template>


<script>
import axios from 'axios';

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
        instructor_picture: null,
        tags: [],
      },
      newTag: "",
      imageBase64: null,
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
      console.log(this.courseData);
      try {
        const accessToken = localStorage.getItem("access_token");
        // Assuming you have an API endpoint for adding courses
            const response = await axios.post(
      "https://api.pickmycourse.online/api/course",
      this.courseData,
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
      
    );

        // Handle the response as needed
        console.log("Course added successfully:", response);

        // You may want to redirect the user or perform other actions after adding the course
      } catch (error) {
        console.error("Error adding course:", error);
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
    handleImageChange(event) {
      const file = event.target.files[0];

      if (file) {
        // Read the file as a data URL (base64)
        const reader = new FileReader();
        reader.onload = () => {
          this.imageBase64 = reader.result;
          this.courseData.instructor_picture = reader.result; // Save base64 in the data property
        };
        reader.readAsDataURL(file);
      }
    },
    saveImage() {
      // Perform actions to save the image, e.g., send it to the server
      console.log("Image saved:", this.courseData.instructor_picture);
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
