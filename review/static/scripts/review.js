// Start of ReviewPic.html
// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides(n) {
//   var i;
//   var slides = document.getElementsByClassName("mySlides");
//   if (n > slides.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = slides.length}
//   for (i = 0; i < slides.length; i++) {
//       slides[i].style.display = "none";
//   }
//   slides[slideIndex-1].style.display = "block";
// }
// var slideIndex = 1;
// showSlides(slideIndex);
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

//This is the Function for Star of TheUserRate.html
$('.TheUserStars').mouseenter(function(){
  var StarID = parseInt($(this).attr('id'))
  if (StarID <6){
    for(bstar = 1;bstar<=5;bstar++){
      $('#'+bstar).removeClass('GoodStar')
    }
    for(sstar = StarID; sstar>0;sstar--){
      $('#'+sstar).addClass('GoodStar')
    }
  }
  else{
    for(bstar = 6;bstar<=10;bstar++){
      $('#'+bstar).removeClass('GoodStar')
    }
    for(sstar = StarID; sstar>0;sstar--){
      $('#'+sstar).addClass('GoodStar')
    }
  }
})


//This is to send the final rating to other page.
$('#submitbtn').click(function(){
  var score = $('i.TheUserStars[class*="GoodStar"]')
  console.log(score.length);
  $('#hide').val(score.length)
  // document.getElementById("test").submit();
})

// This is the connection between the rating count and the star count on the
// comment page
$('#IcountStars').click(function(){
  var score = $('i.TheUserStars[class*="GoodStar"]')
  for(c=6;c<=score.length+5;c++){
    $("#"+c).toggleClass('GoodStar',1000)
  }
})
$('#FINALSTARCOUNT').click(function(){
  var fscore = $('i.TheLastStar[class*="GoodStar"]')
  // console.log((fscore.length/2))
  $('#HiddenStarCount').val((fscore.length))
  // console.log(new Date($.now()))
  var td = new Date($.now());
  $('#HiddenReviewTime').val(td.getMonth()+1+'/'+td.getDate()+'/'+td.getFullYear())
})
