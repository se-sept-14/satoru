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

                <button
                  @click="submitForm"
                  class="bg-black hover:bg-teal-700 text-white font-bold py-2 px-4 rounded"
                >
                  Submit
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

              <div v-else-if="step === 4" key="4">
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

                <!-- <h2 class="text-2xl font-bold mb-4">In Which term are you?</h2>
                <input
                  v-model="term"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your current term"
                /> -->
                <button
                  @click="nextStep"
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <!-- <div v-else-if="step === 5" key="5">
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
              </div> -->
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
                  Step 4: Your Favourite 3 Subjects (in order)
                </h2>

                <select v-model="subject1" class="w-full p-2 mb-4 rounded">
                  <option disabled value="">Please choose a course</option>
                  <option
                    v-for="course in availableCourses"
                    :key="course.id"
                    :value="course.name"
                  >
                    {{ course.name }}
                  </option>
                </select>
                <select v-model="subject2" class="w-full p-2 mb-4 rounded">
                  <option disabled value="">Please choose a course</option>
                  <option
                    v-for="course in availableCourses"
                    :key="course.id"
                    :value="course.name"
                  >
                    {{ course.name }}
                  </option>
                </select>
                <select v-model="subject3" class="w-full p-2 mb-4 rounded">
                  <option disabled value="">Please choose a course</option>
                  <option
                    v-for="course in availableCourses"
                    :key="course.id"
                    :value="course.name"
                  >
                    {{ course.name }}
                  </option>
                </select>
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

              <div v-else-if="step === 10" key="10">
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
                  Step 9: Tell us a more about yourself(optional)
                </h2>
                <!-- Add input for completion date -->
                <h3>Your date of birth</h3>
                <input
                  v-model="dob"
                  type="date"
                  class="w-full p-2 mb-4 rounded"
                />
                <!-- <h3>Your Address</h3>
                <input
                  v-model="address"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your address"
                  /> -->
                <h3>Your Category</h3>
                <select v-model="category" class="w-full p-2 mb-4 rounded">
                  <option disabled value="">Please choose an option</option>
                  <option>General</option>
                  <option>OBC</option>
                  <option>SC/ST</option>
                </select>

                <h3>Your Gender</h3>
                <select v-model="gender" class="w-full p-2 mb-4 rounded">
                  <option disabled value="">Please select one</option>
                  <option>Female</option>
                  <option>Male</option>
                  <option>Other</option>
                  <option>Prefer not to say</option>
                </select>

                <h3>Your Profile Picture</h3>
                <input
                  v-model="profile_picture_url"
                  type="text"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your address"
                />
                <!-- <h3>Your phone Number</h3>
                <input
                  v-model="contact_no"
                  type="number"
                  class="w-full p-2 mb-4 rounded"
                  placeholder="Enter your phone number"
                /> -->

                <button
                  @click="nextStep"
                  class="bg-black hover:bg-teal-900 text-white font-bold py-2 px-4 rounded"
                >
                  Next
                </button>
              </div>

              <div v-else key="11">
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
                  class="bg-black hover:bg-teal-700 text-white font-bold py-2 px-4 rounded"
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
import { useCourseStore } from "@/stores/courseStore";
import { toRaw } from "vue";

export default {
  setup() {
    const authStore = useAuthStore();
    const profileStore = useProfileStore();
    const courseStore = useCourseStore();

    return { authStore, profileStore, courseStore };
  },
  data() {
    return {
      step: 1,
      category: "",
      dob: "2000-01-01",
      gender: "",
      name: "nanami",
      profile_picture_url: "ergfc",
      pwd: false,
      roll_no: "534213",

      careerGoals: "chop chop chop",
      completionDate: "2024-01-01",
      numCourses: "3",
      hoursPerWeek: "15",
      preferences: "datasciecne",

      subject1: "a",
      subject2: "b",
      subject3: "c",

      address: "iugskhj",
      contact_no: "685343213",
      level: 1,
      term: "4",
      cgpa: "8.9",
      availableCourses: [],
    };
  },
  methods: {
    nextStep() {
      this.step++;
    },
    prevStep() {
      this.step--;
    },

    submitForm() {},
    async submitForm() {
      const profileData = {
        student_update: {
          category: this.category,
          dob: this.dob,
          gender: this.gender,
          name: this.name,
          profile_picture_url: this.profile_picture_url,
          pwd: this.pwd,
          roll_no: this.roll_no,
        },
        student_profile_update: {
          career_goals: this.career_goals,
          completion_deadline: this.completion_deadline,
          courses_willing_to_take: this.courses_willing_to_take,
          hours_per_week: this.hours_per_week,
          learning_preferences: this.learning_preferences,
        },
        student_about_me_update: {
          address: this.address,
          contact_no: this.contact_no,
          level: this.level,
          term: this.term,
        },
      };

      const response = await this.profileStore.createProfile(profileData);

      if (response) {
        // Handle successful profile creation
        console.log("created profile");
        console.log(this.gender);
      } else {
        // Handle failed profile creation
        console.log("failed to create profile");
      }
    },
  },

  async created() {
    if (!this.authStore.isLoggedIn()) {
      this.$router.push("/login");
      return;
    }

    this.availableCourses = await this.courseStore.fetchCourses();
    console.log(toRaw(this.availableCourses));
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
