document.addEventListener("DOMContentLoaded", function () {
  const containerElement = document.querySelector("#hero");

  // Array of image URLs
  const images = ["../img/hero-img.png", "../img/hero-img-2.png"];
  let currentImageIndex = 0;

  function changeBackground() {
    const imageUrl = url("${images[currentImageIndex]}");
    heroElement.style.backgroundImage = imageUrl;
    currentImageIndex = (currentImageIndex + 1) % images.length;
  }

  // Change background every 2 seconds
  setInterval(changeBackground, 2000);

  // Initial background
  changeBackground();
});


function showFlipCard() {
  document.getElementById("unflipCard").style.display = "none";
  document.getElementById("flipCard").style.display = "block";
}

function showUnflipCard() {
  document.getElementById("flipCard").style.display = "none";
  document.getElementById("unflipCard").style.display = "block";
}


