// Start of ReviewPic.html
function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}
var slideIndex = 1;
showSlides(slideIndex);
// End of ReviewPic.html

//This is the popover function insdie of AvgStarShow.html//
$('#popoverStuff').hover(mouseinside,mouseoutside)

function mouseinside(){
$('[data-toggle="popover"]').popover({
    html: true,
    content: function() {
    return $('#popover-content').html();
  }})
}
function mouseoutside(){
$('[data-toggle="popover"]').popover({
    html: false,
  })
}
