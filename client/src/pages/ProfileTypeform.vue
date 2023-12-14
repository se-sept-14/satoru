<template>
  <div>
    <div class="h-screen w-screen flex">
      <div
        class="h-full w-5/12 flex flex-col justify-center text-center text-white"
      >
        <p class="font-light text-4xl custom-font">Welcome to Pick My Course</p>
        <img
          class="w-[640px] self-center my-12 rounded-lg"
          src="https://images.unsplash.com/photo-1523289333742-be1143f6b766?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        />
      </div>

      <div class="h-full w-7/12 bg-white rounded-l-2xl">
        <div class="flex justify-center items-center min-h-screen">
          <div class="max-w-4xl mx-auto mt-8 p-4">
            <transition name="slide" mode="out-in">
              <div v-if="step === 1" key="1">
                <h2 class="text-2xl font-bold mb-4">
                  Hi! 👋 Please answer as detailed as possible to get the best
                  experience tailored for you! 💪
                </h2>
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                  Let's Get Started
                </button>
              </div>

              <div v-else-if="step === 2" key="2">
                <button @click="prevStep" class="my-2">
                  <svg
                    class="w-6 h-6 inline-block mr-1"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path
                      d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6z"
                    ></path>
                    <path d="M0 0h24v24H0z" fill="none"></path>
                  </svg>
                  Previous
                </button>
                <h2 class="text-2xl font-bold mb-4">
                  Step 2: What is your learning preference?
                </h2>
                <label class="block mb-2">
                  <input
                    type="radio"
                    v-model="preferences"
                    value="programming"
                  />
                  Programming courses
                </label>
                <label class="block mb-2">
                  <input
                    type="radio"
                    v-model="preferences"
                    value="dataScience"
                  />
                  Data Science courses
                </label>
                <label class="block mb-2">
                  <input type="radio" v-model="preferences" value="mix" />
                  Mix of both
                </label>
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
                <button
                  class="text-gray-300 hover:bg-gray-700 px-4 py-2 rounded font-bold"
                ></button>
              </div>

              <!-- Repeat the pattern for other steps -->

              <div v-else-if="step === 3" key="3">
                <button @click="prevStep" class="my-2">
                  <svg
                    class="w-6 h-6 inline-block mr-1"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path
                      d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6z"
                    ></path>
                    <path d="M0 0h24v24H0z" fill="none"></path>
                  </svg>
                  Previous
                </button>
                <h2 class="text-2xl font-bold mb-4">Step 3: Your CGPA</h2>
                <input
                  v-model="cgpa"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your CGPA"
                />
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else-if="step === 4" key="4">
                <button @click="prevStep" class="my-2">
                  <svg
                    class="w-6 h-6 inline-block mr-1"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path
                      d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6z"
                    ></path>
                    <path d="M0 0h24v24H0z" fill="none"></path>
                  </svg>
                  Previous
                </button>
                <h2 class="text-2xl font-bold mb-4">
                  Step 4: Your Favourite 3 Subjects (in order)
                </h2>
                <!-- Add input fields for favorite subjects -->
                <input
                  v-model="subject1"
                  type="text"
                  class="w-full p-2 mb-2 rounded"
                  placeholder="1st Favorite Subject"
                />
                <input
                  v-model="subject2"
                  type="text"
                  class="w-full p-2 mb-2 rounded"
                  placeholder="2nd Favorite Subject"
                />
                <input
                  v-model="subject3"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="3rd Favorite Subject"
                />
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else-if="step === 5" key="5">
                <button @click="prevStep" class="my-2">
                  <svg
                    class="w-6 h-6 inline-block mr-1"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path
                      d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6z"
                    ></path>
                    <path d="M0 0h24v24H0z" fill="none"></path>
                  </svg>
                  Previous
                </button>
                <h2 class="text-2xl font-bold mb-4">
                  Step 5: No. of Hours You Can Devote in a Week
                </h2>
                <!-- Add input for hours per week -->
                <input
                  v-model="hoursPerWeek"
                  type="number"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter hours per week"
                />
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else-if="step === 6" key="6">
                <button @click="prevStep" class="my-2">
                  <svg
                    class="w-6 h-6 inline-block mr-1"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path
                      d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6z"
                    ></path>
                    <path d="M0 0h24v24H0z" fill="none"></path>
                  </svg>
                  Previous
                </button>
                <h2 class="text-2xl font-bold mb-4">
                  Step 6: No. of Courses You're Willing to Take
                </h2>
                <!-- Add input for number of courses -->
                <input
                  v-model="numCourses"
                  type="number"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter number of courses"
                />
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else-if="step === 7" key="7">
                <button @click="prevStep" class="my-2">
                  <svg
                    class="w-6 h-6 inline-block mr-1"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path
                      d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6z"
                    ></path>
                    <path d="M0 0h24v24H0z" fill="none"></path>
                  </svg>
                  Previous
                </button>
                <h2 class="text-2xl font-bold mb-4">
                  Step 7: Your Long-term Career Goals
                </h2>
                <!-- Add input for career goals -->
                <textarea
                  v-model="careerGoals"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your long-term career goals"
                ></textarea>
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else-if="step === 8" key="8">
                <button @click="prevStep" class="my-2">
                  <svg
                    class="w-6 h-6 inline-block mr-1"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path
                      d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6z"
                    ></path>
                    <path d="M0 0h24v24H0z" fill="none"></path>
                  </svg>
                  Previous
                </button>
                <h2 class="text-2xl font-bold mb-4">
                  Step 8: When Do You Intend to Complete Your Degree?
                </h2>
                <!-- Add input for completion date -->
                <input
                  v-model="completionDate"
                  type="date"
                  class="w-full p-2 mb-4 rounded"
                />
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else key="9">
                <h2 class="text-2xl font-bold mb-4">Summary</h2>
                <p>Learning Preferences: {{ preferences }}</p>
                <p>CGPA: {{ cgpa }}</p>
                <p>
                  Favourite Subjects: {{ subject1 }}, {{ subject2 }},
                  {{ subject3 }}
                </p>
                <p>Hours Per Week: {{ hoursPerWeek }}</p>
                <p>Number of Courses: {{ numCourses }}</p>
                <p>Career Goals: {{ careerGoals }}</p>
                <p>Completion Date: {{ completionDate }}</p>
                <button
                  @click="submitForm"
                  class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
                >
                  Submit
                </button>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      step: 1,
      preferences: "",
      cgpa: "",
      subject1: "",
      subject2: "",
      subject3: "",
      hoursPerWeek: "",
      numCourses: "",
      careerGoals: "",
      completionDate: "",
      // Add other form data properties here
    };
  },
  methods: {
    nextStep() {
      this.step++;
    },
    prevStep() {
      this.step--;
    },
    submitForm() {
      // Handle form submission logic here
      // You can access form data from this.dataProperty
      // For example: console.log(this.preferences, this.cgpa, ...);

      // For demonstration purposes, let's just log the form data
      console.log("Form Data:", {
        preferences: this.preferences,
        cgpa: this.cgpa,
        subject1: this.subject1,
        subject2: this.subject2,
        subject3: this.subject3,
        hoursPerWeek: this.hoursPerWeek,
        numCourses: this.numCourses,
        careerGoals: this.careerGoals,
        completionDate: this.completionDate,
      });
    },
  },
};
</script>

<style>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.4s ease;
}
.slide-enter,
.slide-leave-to {
  transform: translateX(100%);
}
/* your-component.css */
@font-face {
  font-family: "ApercuProRegular"; /* Provide a name for your font */
  src: url("@/assets/fonts/ApercuProRegular.otf") format("opentype");
  font-weight: normal;
  font-style: normal;
}

.custom-font {
  font-family: "ApercuProRegular", sans-serif; /* Use the font-family name you specified in @font-face */
}
</style>
