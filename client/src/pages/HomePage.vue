<template>
  <div class="container mx-auto mt-24 text-white w-6/12">
    <div class="flex flex-col text-center">
      <h1 class="text-6xl font-bold">
        Get Personalized Course Recommendations for Students
      </h1>
      <p class="mt-4 text-xl">
        Welcome to our website, where you can discover the perfect courses for
        your educational journey
      </p>

      <div class="mt-12 flex flex-row justify-center">
        <button
          class="mx-1 outline outline-1 p-4 hover:bg-white hover:text-black rounded-md"
        >
          Login
        </button>
        <button
          class="mx-1 outline outline-1 p-4 rounded-md bg-white text-black hover:shadow-lg hover:shadow-yellow-200/90"
        >
          Register
        </button>
      </div>
    </div>

    <div class="flex flex-row mt-24">
      <div class="basis-3/5 flex flex-col">
        <h1 class="text-4xl font-semibold mb-4">
          Find the perfect courses for you
        </h1>
        <p class="mb-2">
          Our intelligent course Recommendation system analyzes your interests
          and academic goals to suggest the best courses for you
        </p>

        <div class="flex flex-row mt-12">
          <div class="flex flex-col">
            <p class="text-lg font-bold mb-1">Personalized</p>
            <p>
              Get personalized course recommendations based on your interests
              and academic goals
            </p>
          </div>
          <div class="flex flex-col">
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
      <div class="basis-2/5 flex flex-col">
        <img
          class="rounded-lg"
          src="@/assets/HomePage/landing-page-image.jpg"
        />
        <small class="mt-1 italic text-center"
          >Photo by
          <a
            class="text-green-400"
            href="https://unsplash.com/@sajadnori?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"
            >Sajad Nori</a
          >
          on
          <a
            class="text-green-400"
            href="https://unsplash.com/photos/person-holding-black-and-white-round-ornament-21mJd5NUGZU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"
            >Unsplash</a
          >
        </small>
      </div>
    </div>

    <div class="flex flex-col mt-24 mb-20">
      <h1 class="text-4xl font-bold w-2/3 mb-4">
        Get Personalized Course Recommendations Just For You
      </h1>

      <div class="flex flex-row mt-12">
        <div class="flex flex-col">
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

        <div class="flex flex-col">
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
  </div>
</template>