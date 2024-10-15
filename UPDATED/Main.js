let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("slides");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  // Hide all slides
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;  // Reset to the first slide
    }
    slides[slideIndex - 1].style.display = "block";  // Show the current slide
    setTimeout(showSlides, 5000);  // Change slide every 5 seconds
}
