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

//This is the Hover Function for Star of TheUserRate.html
$('.TheUserStars').mouseenter(function(){
  var StarID = parseInt($(this).attr('id'))
  if (!($('#1').hasClass('GoodStar'))){
    for(i = StarID; i>0;i--){
      $("#"+i).toggleClass('GoodStar',1000)
    }

  }
  else{
    for(j = StarID; j<6;j++){
      $("#"+j).removeClass('GoodStar',1000)
    }
    $(this).toggleClass('GoodStar',1000)
    console.log("Star from beginning")
  }
})

$('#submitbtn').click(function(){
  var score = $('i.TheUserStars[class*="GoodStar"]')
  console.log(score.length);
  $('#hide').val(score.length)
  // document.getElementById("test").submit();
})
