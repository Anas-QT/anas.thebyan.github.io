// Array of image paths (update these to match your file paths)
const images = [
  "images/personal-photo.jpg",
  "images/fun-photo.jpg",
  "images/waterfall-photo.jpg",
  "images/classy-photo.jpg",
  "images/hat-photo.jpg",
];

let currentIndex = 0;

// Get the image element (update the selector to match your HTML)
const imageElement = document.querySelector(".photo"); // or use querySelector('.your-class')

// Add click event listener
imageElement.addEventListener("click", function () {
  // Move to next image
  currentIndex = (currentIndex + 1) % images.length;

  // Update the image source
  imageElement.src = images[currentIndex];
});

// Optional: Add some visual feedback during transition
imageElement.addEventListener("click", function () {
  imageElement.style.opacity = "0.7";
  setTimeout(() => {
    imageElement.style.opacity = "1";
  }, 150);
});
