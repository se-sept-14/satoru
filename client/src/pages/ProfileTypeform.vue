<template>
  <div>
    <div class="h-screen w-screen flex">
      <div
        class="h-full w-5/12 flex flex-col justify-center text-center text-white"
      >
        <p class="font-light text-4xl custom-font w-64 mt-30 self-center">
          Welcome to Pick My Course
        </p>
        <img
          class="w-[400px] self-center mx-4 mt-12 rounded-lg"
          src="@/assets/newtang.png"
        />
      </div>

      <div class="h-full w-7/12 bg-stone-50 rounded-l-2xl">
        <div class="flex justify-center items-center min-h-screen">
          <div class="w-[640px] mx-auto mt-8 p-4">
            <transition name="slide" mode="out-in">
              <div v-if="step === 1" key="1">
                <h2 class="text-3xl font-bold mb-2">Let's get you set up!</h2>
                <p class="text-lg mb-6">
                  It only takes a moment. And it'll make your time with us even
                  better.💪
                </p>
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
                >
                  <span class="mr-1"><i class="fa-solid fa-play"></i></span>
                  Get Started
                </button>
              </div>

              <div v-else-if="step === 2" key="2">
                <button @click="prevStep" class="my-2 hover:text-blue-900">
                  <i class="fa-solid fa-arrow-left mr-1"></i>
                  Go back
                </button>

                <h2 class="text-2xl font-bold mb-4">What is your name?</h2>
                <input
                  v-model="name"
                  type="text"
                  class="w-full p-2 mb-4 border-b border-black border-t-0 border-r-0 border-l-0 rounded-none"
                  placeholder="Enter your name"
                />

                <h2 class="text-2xl font-bold mb-4">
                  What is your learning preference?
                </h2>

                <label class="block mb-2">
                  <input
                    type="radio"
                    v-model="preferences"
                    value="programming"
                    class="mr-1"
                  />
                  Programming courses
                </label>
                <label class="block mb-2">
                  <input
                    type="radio"
                    v-model="preferences"
                    value="dataScience"
                    class="mr-1"
                  />
                  Data Science courses
                </label>
                <label class="block mb-2">
                  <input
                    type="radio"
                    v-model="preferences"
                    value="mix"
                    class="mr-1"
                  />
                  Mix of both
                </label>
                <button
                  @click="nextStep"
                  class="mt-2 bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
                <button
                  class="text-gray-300 hover:bg-gray-700 px-4 py-2 rounded font-bold"
                ></button>
              </div>

              <div v-else-if="step === 3" key="3">
                <button @click="prevStep" class="my-2 hover:text-blue-900">
                  <i class="fa-solid fa-arrow-left mr-1"></i>
                  Go back
                </button>
                <h2 class="text-2xl font-bold mb-4">Step 3: Your CGPA</h2>
                <input
                  v-model="cgpa"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your CGPA"
                />

                <h2 class="text-2xl font-bold mb-4">In Which level are you?</h2>
                <p>(0:foundational, 1:diploma, 2:degree, 3:bs)</p>
                <input
                  v-model="term"
                  type="number"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your current level"
                />

                <h2 class="text-2xl font-bold mb-4">In Which term are you?</h2>
                <input
                  v-model="term"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your current term"
                />
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
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
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
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
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
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
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
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
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
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
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else-if="step === 9" key="9">
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
                  Step 9: Tell us a more about yourself
                </h2>
                <!-- Add input for completion date -->
                <input
                  v-model="dob"
                  type="date"
                  class="w-full p-2 mb-4 rounded"
                />
                <input
                  v-model="address"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your address"
                />
                <input
                  v-model="category"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your address"
                />
                <input
                  v-model="gender"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your address"
                />
                <input
                  v-model="contact_no"
                  type="number"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your phone number"
                />
                <!-- <input
                  v-model="pwd"
                  type="checkbok"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Choose true if pwd"
                /> -->
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else key="10">
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
import { useProfileStore } from "@/stores/ProfileStore";
import { useAuthStore } from "@/stores/AuthStore";

export default {
  setup() {
    const authStore = useAuthStore();
    const profileStore = useProfileStore();

    return { authStore, profileStore };
  },
  data() {
    return {
      step: 1,
      category: "",
      dob: "",
      gender: "",
      name: "",
      profile_picture_url: "",
      pwd: false,
      roll_no: "",

      careerGoals: "",
      completionDate: "",
      numCourses: "",
      hoursPerWeek: "",
      preferences: "",

      subject1: "",
      subject2: "",
      subject3: "",

      address: "",
      contact_no: "",
      level: 1,
      term: "",
      cgpa: "",
    };
  },
  methods: {
    nextStep() {
      this.step++;
    },
    prevStep() {
      this.step--;
    },
    // submitForm() {
    //   console.log("Form Data:", {
    //     preferences: this.preferences,
    //     cgpa: this.cgpa,
    //     subject1: this.subject1,
    //     subject2: this.subject2,
    //     subject3: this.subject3,
    //     hoursPerWeek: this.hoursPerWeek,
    //     numCourses: this.numCourses,
    //     careerGoals: this.careerGoals,
    //     completionDate: this.completionDate,
    //   });
    // },

    submitForm() {},
    async submitForm() {
      const profileData = {
        category: this.category,
        dob: this.dob,
        gender: this.gender,
        name: this.name,
        profile_picture_url: this.profile_picture_url,
        pwd: this.pwd,
        roll_no: this.roll_no,
        career_goals: this.career_goals,
        completion_deadline: this.completion_deadline,
        courses_willing_to_take: this.courses_willing_to_take,
        hours_per_week: this.hours_per_week,
        learning_preferences: this.learning_preferences,
        address: this.address,
        contact_no: this.contact_no,
        level: this.level,
        term: this.term,
      };

      const response = await this.profileStore.createProfile(profileData);

      if (response) {
        // Handle successful profile creation
        console.log("created profile");
      } else {
        // Handle failed profile creation
        log("failed to create profile");
      }
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
  font-family: "ApercuProRegular";
  src: url("@/assets/fonts/ApercuProRegular.otf") format("opentype");
  font-weight: normal;
  font-style: normal;
}

.custom-font {
  font-family: "ApercuProRegular", sans-serif;
}
</style>
