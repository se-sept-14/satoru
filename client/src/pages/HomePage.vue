<template>
  <div class="container mx-auto mt-24 text-white w-3/5">
    <div class="flex flex-col text-center">
      <h1
        class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-bold"
      >
        <span class="gradient-text-1">Get Personalized Course</span><br />
        <span class="gradient-text-2">Recommendations for Students</span>
      </h1>
      <p class="mt-4 text-md sm:text-md md:text-lg lg:text-xl xl:text-2xl">
        Welcome to our website, where you can discover the perfect courses for
        your educational journey
      </p>

      <div class="mt-12 flex flex-col justify-center md:flex md:flex-row">
        <router-link
          to="/login"
          class="mx-2 outline outline-1 px-6 py-4 my-2 md:my-0 text-lg md:text-md sm:text-sm hover:bg-white hover:text-black rounded-md"
        >
          Already a user? Login
        </router-link>
        <button
          class="mx-2 outline outline-1 px-6 py-4 my-2 md:my-0 text-lg md:text-md sm:text-sm rounded-md bg-white text-black hover:shadow-lg hover:shadow-yellow-200/90"
        >
          Get Started
        </button>
      </div>
    </div>

    <div class="flex flex-row mt-24">
      <div class="lg:basis-3/5 flex flex-col">
        <h1 class="text-3xl lg:text-4xl font-semibold mb-4">
          Find the perfect courses for you
        </h1>
        <p class="mb-2">
          Our intelligent course Recommendation system analyzes your interests
          and academic goals to suggest the best courses for you
        </p>

        <div class="flex flex-col lg:flex-row mt-12">
          <div class="flex flex-col my-2 lg:my-0">
            <p class="text-lg font-bold mb-1">Personalized</p>
            <p>
              Get personalized course recommendations based on your interests
              and academic goals
            </p>
          </div>
          <div class="flex flex-col my-2 lg:my-0">
            <p class="text-lg font-bold mb-1">Efficient</p>
            <p>
              Save time and effort by letting our intelligent systems find the
              best courses for you
            </p>
          </div>
        </div>

        <button
          class="outline outline-1 w-36 p-2 mt-8 rounded-md hover:rounded-none hover:bg-white hover:text-black"
        >
          Get started
        </button>
      </div>
      <div class="invisible lg:visible basis-2/5 flex flex-col">
        <img
          class="rounded-lg"
          src="@/assets/HomePage/landing-page-image.jpg"
        />
        <small class="mt-1 italic text-center"
          >Photo by
          <a
            class="text-green-400"
            v-bind:href="unsplash.user"
            target="_blank"
            rel="noopener noreferrer"
            >Sajad Nori</a
          >
          on
          <a
            class="text-green-400"
            v-bind:href="unsplash.image"
            target="_blank"
            rel="noopener noreferrer"
            >Unsplash</a
          >
        </small>
      </div>
    </div>

    <div class="flex flex-col mt-24 mb-20">
      <h1 class="text-3xl font-bold lg:w-2/3 lg:text-5xl mb-4">
        Get Personalized Course Recommendations Just For You
      </h1>

      <div class="flex flex-col lg:flex-row mt-12">
        <div class="flex flex-col my-4 lg:my-0">
          <i class="fa-solid fa-cube text-3xl"></i>
          <p class="text-xl font-semibold mt-6">
            Explore a Diverse Selection of Courses
          </p>
          <p class="mt-8 w-4/5">
            Our platform offers a wide range of courses to suit your interests
            and goals
          </p>
          <div
            class="flex flex-row items-center mt-6 cursor-pointer text-blue-200"
          >
            <p class="hover:mr-2 underline underline-offset-2">Enroll</p>
            <i class="fa-solid fa-chevron-right ml-2 hover:ml-4"></i>
          </div>
        </div>

        <div class="flex flex-col my-4 lg:my-0">
          <i class="fa-solid fa-earth-asia text-3xl"></i>
          <p class="text-xl font-semibold mt-6">
            Discover new opportunities with easy enrollment
          </p>
          <p class="mt-8 w-4/5">
            Our enrollment process is simple and hassle-free, allowing you to
            start learning right away
          </p>
          <div
            class="flex flex-row items-center mt-6 cursor-pointer text-blue-200"
          >
            <p class="hover:mr-2 underline underline-offset-2">Join</p>
            <i class="fa-solid fa-chevron-right ml-2 hover:ml-4"></i>
          </div>
        </div>
      </div>
    </div>

    <div class="flex flex-col mt-28 mb-8 text-center">
      <h1 class="text-4xl font-bold">FAQs</h1>
      <p class="mt-4">
        Find answers to commonly asked questions about our service and how to
        get started
      </p>

      <hr class="my-8 border-t-2 border-gradient" />
      <p class="text-lg font-semibold">How does it work?</p>
      <p class="mt-2">
        Our website uses advanced algorithms to analyze your interests, academic
        background and career goals to provide personalized course
        recommendations. Simply create an account, answer a few questions and
        let our system do the magic
      </p>

      <hr class="my-8 border-t-2 border-gradient" />
      <p class="text-lg font-semibold">Is it free?</p>
      <p class="mt-2">
        Yes, our service is completely free to use. We believe that access to
        quality education should be available to everyone, regardless of their
        financial situation
      </p>

      <hr class="my-8 border-t-2 border-gradient" />
      <p class="text-lg font-semibold">How accurate are the recommendations?</p>
      <p class="mt-2">
        Our recommendations are based on a combination of Machine Learning
        algorithms and user feedback. While we strive to provide the most
        accurate suggestions, it's important to note that individual preferences
        and goals may vary
      </p>

      <hr class="my-8 border-t-2 border-gradient" />
      <p class="text-lg font-semibold">How can I contact support?</p>
      <p class="mt-2">
        If you have any other questions or need further assistance, our support
        team is available 24/7. Simple reach out to us via email or through the
        contact form and we'll be glad to help
      </p>

      <h1 class="mt-16 text-3xl font-semibold">Still have questions?</h1>
      <p>Get in touch with us today</p>

      <button
        class="border border-1 w-32 p-3 mt-4 rounded-md hover:bg-white hover:text-black hover:rounded-none self-center"
      >
        Contact Us
      </button>
    </div>

    <div class="flex flex-col mt-28 mb-24">
      <h1 class="text-center text-4xl font-bold">Meet Our Team 14</h1>
      <p class="text-center mt-2">Get to know the minds behind this platform</p>

      <div class="flex flex-col lg:flex-row my-6">
        <div class="basis-1/3 flex flex-col items-center my-4 lg:my-0">
          <div
            class="relative inline-flex items-center justify-center w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600 mr-2"
          >
            <img
              src="https://ifkash.vercel.app/assets/images/gojo.webp"
              alt="Kashiful Haque"
            />
          </div>
          <p class="font-semibold mt-2">Kashiful Haque</p>
          <p class="text-sm font-light">Developer</p>
          <p class="text-center text-sm mt-3 w-56">
            Passionate about helping students achieve their full potential
          </p>
        </div>

        <div class="basis-1/3 flex flex-col items-center my-4 lg:my-0">
          <div
            class="relative inline-flex items-center justify-center w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600 mr-2"
          >
            <img
              src="https://avatars.githubusercontent.com/u/99545773?v=4"
              alt="Tejas Gajra"
            />
          </div>
          <p class="font-semibold mt-2">Tejas Gajra</p>
          <p class="text-sm font-light">Developer</p>
          <p class="text-center text-sm mt-3 w-56">
            Bringing innovative ideas to create a seamless user experience
          </p>
        </div>

        <div class="basis-1/3 flex flex-col items-center my-4 lg:my-0">
          <div
            class="relative inline-flex items-center justify-center w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600 mr-2"
          >
            <img
              src="https://avatars.githubusercontent.com/u/91440435?v=4"
              alt="Ananya Modugula"
            />
          </div>
          <p class="font-semibold mt-2">Ananya Modugula</p>
          <p class="text-sm font-light">Data Scientist</p>
          <p class="text-center text-sm mt-3 w-56">
            Transforming ideas into innovative features for an enhanced learning
            experience
          </p>
        </div>
      </div>

      <div class="flex flex-col lg:flex-row justify-center">
        <div class="basis-1/3 flex flex-col items-center my-4 lg:my-0">
          <div
            class="relative inline-flex items-center justify-center w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600 mr-2"
          >
            <img
              src="https://avatars.githubusercontent.com/u/126502243?v=4"
              alt="Aarya Motiwala"
            />
          </div>
          <p class="font-semibold mt-2">Aarya Motiwala</p>
          <p class="text-sm font-light">Developer</p>
          <p class="text-center text-sm mt-3 w-56">
            Committed to creating a supportive and inclusive learning
            environment
          </p>
        </div>

        <div class="basis-1/3 flex flex-col items-center my-4 lg:my-0">
          <div
            class="relative inline-flex items-center justify-center w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600 mr-2"
          >
            <img
              src="https://avatars.githubusercontent.com/u/146165366?v=4"
              alt="Md Farhan Reza"
            />
          </div>
          <p class="font-semibold mt-2">Md Farhan Reza</p>
          <p class="text-sm font-light">Developer</p>
          <p class="text-center text-sm mt-3 w-56">
            Passionate about inspiring students to pursue their educational
            goals
          </p>
        </div>
      </div>
    </div>

    <div class="flex flex-col lg:flex-row mt-32 mb-24">
      <div class="basis-8/12 flex flex-col">
        <h1 class="text-2xl font-semibold">Recommender System</h1>
        <p class="text-md font-semibold mt-4">Address</p>
        <p class="text-sm font-light">646 Hammes Wells, New Ty, NC 24138</p>
        <p class="text-md font-semibold mt-8">Contact</p>
        <p class="text-sm font-light">contact@recsys.ai</p>
        <div class="flex flex-row mt-6">
          <i
            class="mx-1 cursor-pointer text-xl fa-brands fa-square-x-twitter"
          ></i>
          <i class="mx-1 cursor-pointer text-xl fa-brands fa-instagram"></i>
          <i class="mx-1 cursor-pointer text-xl fa-brands fa-youtube"></i>
          <i class="mx-1 cursor-pointer text-xl fa-brands fa-threads"></i>
          <i class="mx-1 cursor-pointer text-xl fa-brands fa-linkedin"></i>
        </div>
      </div>

      <div class="basis-4/12 flex flex-col">
        <router-link to="/" class="my-2 cursor-pointer text-sm text-yellow-100"
          >Discover courses</router-link
        >
        <router-link to="/" class="my-2 cursor-pointer text-sm text-yellow-100"
          >My courses</router-link
        >
        <router-link to="/" class="my-2 cursor-pointer text-sm text-yellow-100"
          >Recommendations</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      unsplash: {
        user: "https://unsplash.com/@sajadnori",
        image:
          "https://unsplash.com/photos/person-holding-black-and-white-round-ornament-21mJd5NUGZU",
      },
    };
  },
};
</script>

<style scoped>
.border-gradient {
  background: linear-gradient(to right, #ff00a9, #ff7e5f);
}

/* Vercel like Gradient text CSS stolen from https://dev.to/mohsenkamrani/create-a-gradient-text-effect-like-vercel-with-css-38g5 */
.gradient-text-1 {
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(90deg, #007cf0, #00dfd8);
}

.gradient-text-2 {
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(to right, #f7797d, #fbd786, #c6ffdd);
}
</style>
