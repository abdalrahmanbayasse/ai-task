/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/**/*.html"],

  theme: {
    extend: {
      animation: {
        typewriter: "typewriter 2s steps(11) forwards",
      },
      keyframes: {
        typewriter: {
          to: {
            left: "100%",
          },
        },
      },
    },
  },
  plugins: [],
};
