<template>
  <div class="form-container">
    <div class="header"></div>
    <div class="form-wrapper">
      <form @submit.prevent="addCourse" class="form">
        <div v-show="currentStep === 1" class="container bg-black mt-10 mb-10 p-10">
          <div class="title mt-4 text-white">Step 1: Basic Information</div>

          <div class="flex flex-col mb-4">
            <label for="courseName" class="text-xl text-white"
              >Course Name:</label
            >
            <input
              v-model="courseData.name"
              id="courseName"
              type="text"
              class="input-field"
              placeholder="Course Name"
              required/>
          </div>

          <div class="flex flex-col mb-6">
            <!-- Increase the height of the description input -->
            <label for="description" class="text-xl text-white"
              >Description:</label
            >
            <textarea
              v-model="courseData.description"
              id="description"
              class="textarea-field"
              placeholder="Course description goes here ..."
            ></textarea>
          </div>
          <div class="flex flex-col mb-4">
            <label for="prerequisite" class="text-xl text-white"
              >Course price in Rs:</label>
            <input
              v-model="courseData.price"
              id="courseprice"
              type="text"
              class="input-field"
              inputmode="numeric"
              placeholder="10000"
              required/>
          </div>
          <button @click="nextStep1" type="button" class="navigation-button">Next</button>
        </div>

        <div v-show="currentStep === 2" class="container bg-black mt-10 mb-10 p-10">
          <div class="title mt-4 text-white">Step 2: Course Details</div>
          <div class="flex flex-col mb-4">
            <label for="prerequisite" class="text-xl text-white"
              >Course Code:</label
            >
            <input
              v-model="courseData.code"
              id="coursecode"
              type="text"
              class="input-field"
              placeholder="BSCCS2001"
              required
            />
          </div>

          <div class="flex flex-col mb-4">
            <label for="prerequisite" class="text-xl text-white"
              >Prerequisite:</label
            >
            <input
              v-model="courseData.prerequisites"
              id="prerequisite"
              type="text"
              class="input-field"
              placeholder="BSCCS2001, BSCCS2003, ..."
              required
            />
          </div>
          <div class="flex flex-col mb-4">
            <label for="corequisite" class="text-xl text-white"
              >corequisite:</label
            >
            <input
              v-model="courseData.corequisite"
              id="corequisite"
              type="text"
              class="input-field"
              placeholder="BSCCS2001, BSCCS2003, ..."
              required
            />
          </div>
          <button @click="prevStep" type="button" class="navigation-button">Previous</button>
          <button @click="nextStep2" type="button" class="navigation-button">Next</button>
        </div>

        <div v-show="currentStep === 3" class="container bg-black mt-10 mb-10 p-10">
          <div class="title mt-4 text-white">
            Step 3: Instructor Information
          </div>
          <div class="flex flex-col mb-4">
            <label for="taughtBy" class="text-xl text-white">Taught by:</label>
            <input
              v-model="courseData.instructor_name"
              id="taughtBy"
              type="text"
              class="input-field"
              placeholder="Professor name here ..."
              required
            />
          </div>
          <div class="flex flex-col mb-4 text-white">
            <label class="text-xl text-white" for="imageInput">Select an Image:</label>
            <input
              type="file"
              id="imageInput"
              accept="image/*"
              @change="handleImageChange"
            />

            <div v-if="imageBase64">
              <img
                :src="imageBase64"
                alt="Selected Image"
                style="max-width: 100%"
              />
            </div>

            
          </div>

          <button type="button" @click="prevStep" class="navigation-button">Previous</button>
          <button type="button" @click="nextStep3" class="navigation-button">Next</button>
        </div>

        <div v-show="currentStep === 4" class="container bg-black mt-5 mb-10 p-10">
          <div class="title mt-4 text-white">Step 4: Other Details</div>

          <div class="flex flex-col mb-4">
            <label for="taughtBy" class="text-xl text-white"
              >Hrs per week:</label
            >
            <input
              v-model="courseData.hours_per_week"
              id="hours_per_week"
              type="text"
              class="input-field"
              placeholder="10hrs"
              required
            />
          </div>

          <div class="flex flex-col mb-4">
            <label for="tags" class="text-xl text-white">Tags:</label>
            <input
              v-model="newTag"
              type="text"
              class="input-field"
              placeholder="Programming"
              id="tags"
              @keydown.enter.prevent="addTag"
            />
            <br>
            <ul>
              <li class="text-white text-xl mr-3" v-for="(tag, index) in courseData.tags" :key="index">
                {{ tag }}
                <button
                  type="button"
                  class="w-24 h-10 bg-green-600 rounded-xl text-xl font-normal text-white"
                  @click="removeTag(index)"
                >
                  Remove
                </button>
              </li>
            </ul>
          </div>

          <div class="flex flex-col mb-4">
            <label for="credits" class="text-xl text-white">Credits:</label>
            <input
              v-model="courseData.credits"
              id="credits"
              type="text"
              class="input-field"
              placeholder="4"
              required/>
          </div>

          <button type="button" @click="prevStep" class="navigation-button">Previous</button>
          <button type="submit" class="submit-button">Add</button>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
import axios from "axios";

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
        instructor_picture:"https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg",
        tags: [],
      },
      newTag: "",
      imageBase64: null,
      currentStep: 1,
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
  

  this.courseData.credits = parseInt(this.courseData.credits);
  this.courseData.price = parseInt(this.courseData.price);

  const accessToken = localStorage.getItem("access_token");
  const headers = {
    accept: "application/json",
    Authorization: `Bearer ${accessToken}`,
    "Content-Type": "application/json",
  };

  try {
    const response = await axios.post(
      "https://api.pickmycourse.online/api/course/",
      this.courseData,
      {
        headers,
      }
    );

    console.log(response.data);
  } catch (error) {
    alert("Please check if you have entered all the data correctly");
    console.error(error);
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
    nextStep1() {
      if(this.courseData.name=="" || this.courseData.description=="" || this.courseData.price==0){
        console.log("hii");

      }
      else{
        console.log("byee");
        this.currentStep++;

      }
      
      
    },
    nextStep2() {
      if(this.courseData.code=="" || this.courseData.prerequisites=="" || this.courseData.corequisite==""){
        console.log("hii");

      }
      else{
        console.log("byee");
        this.currentStep++;

      }
      
      
    },
    nextStep3() {
      if(this.courseData.instructor_name=="" || this.courseData.instructor_picture==""){
        console.log("hii");

      }
      else{
        console.log("byee");
        this.currentStep++;

      }
      
      
    },
    prevStep() {
  if (this.currentStep > 1) {
    this.currentStep--;
  }
}

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
  text: black;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.3); /* Green glow effect, adjust color as needed */
}

.container {
  max-width: 600px;
  width: 100%;
  background-color: rgb(26, 25, 25);
  box-shadow: 0 0 10px rgba(192, 165, 165, 0.6);
  border:rgb(248, 241, 241);
}

.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  background-color: black;
}

.header {
  flex: 1;
}

.form-wrapper {
  flex: 2;
  display: flex;
  align-items: center;
  justify-content: center;
}

.form {
  display: flex;
  flex-direction: column;
  width: 100%;
}
.navigation-button {
  width: 100%;
  height: 3rem;
  text-align: center;
  background-color: #02c4ff;
  color: white;
  border: none;
  border-radius: 0.375rem;
  font-size: 1.5rem;
  margin-top: 1rem;
  cursor: pointer;
}
.title {
  text-align: center;
  font-size: 2rem;
  font-weight: bold;

  margin-bottom: 1rem;
}

.submit-button {
  width: 100%;
  height: 3rem;
  text-align: center;
  background-color: #49b14c;
  color: white;
  border: none;
  border-radius: 0.375rem;
  font-size: 1.5rem;
  margin-top: 1rem;
  cursor: pointer;
}
</style>
