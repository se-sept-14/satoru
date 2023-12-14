<!-- ProfileForm.vue -->
<template>
  <div class="flex justify-center items-center min-h-screen">
    <div
      class="max-w-4xl mx-auto mt-8 p-4 bg-black text-white border border-gray-700 rounded-lg"
    >
      <div v-if="step === 1">
        <h2 class="text-2xl font-bold mb-4">
          Hi! 👋 Please answer as detailed as possible to get the best
          experience tailored for you! 💪
        </h2>
        <button
          @click="nextStep"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Let's Get Started
        </button>
      </div>

      <div v-else-if="step === 2">
        <h2 class="text-2xl font-bold mb-4">
          Step 2: What is your learning preference?
        </h2>
        <label class="block mb-2">
          <input type="radio" v-model="preferences" value="programming" />
          Programming courses
        </label>
        <label class="block mb-2">
          <input type="radio" v-model="preferences" value="dataScience" />
          Data Science courses
        </label>
        <label class="block mb-2">
          <input type="radio" v-model="preferences" value="mix" />
          Mix of both
        </label>
        <button
          @click="nextStep"
          class="bg-teal-600 hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
        >
          Next
        </button>
        <button
          class="text-gray-300 hover:bg-gray-700 px-4 py-2 rounded font-bold"
        ></button>
      </div>

      <!-- Repeat the pattern for other steps -->

      <div v-else-if="step === 3">
        <h2 class="text-2xl font-bold mb-4">Step 3: Your CGPA</h2>
        <input
          v-model="cgpa"
          type="text"
          class="w-full p-2 mb-4 rounded"
          placeholder="Enter your CGPA"
        />
        <button
          @click="nextStep"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Next
        </button>
      </div>

      <div v-else-if="step === 4">
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
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Next
        </button>
      </div>

      <div v-else-if="step === 5">
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
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Next
        </button>
      </div>

      <div v-else-if="step === 6">
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
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Next
        </button>
      </div>

      <div v-else-if="step === 7">
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
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Next
        </button>
      </div>

      <div v-else-if="step === 8">
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
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Next
        </button>
      </div>

      <div v-else>
        <h2 class="text-2xl font-bold mb-4">Summary</h2>
        <p>Learning Preferences: {{ preferences }}</p>
        <p>CGPA: {{ cgpa }}</p>
        <p>
          Favourite Subjects: {{ subject1 }}, {{ subject2 }}, {{ subject3 }}
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

<style scoped>
/* Add your Tailwind CSS styles here */
</style>
