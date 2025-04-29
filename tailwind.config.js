/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'monopoly-red': '#F11C26',
        'monopoly-green': 'rgb(209 250 229 / 0.9)',
      },
      backgroundImage: {
        'monopoly-board': "url('../images/bg-monopoly.svg')",
        'monopoly-logo': "url('../images/bg-monopoly.svg')",
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('tailwind-scrollbar'),
    require('tailwind-scrollbar-hide'),
  ],
}