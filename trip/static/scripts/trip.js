// for the left
function openDay(evt, trvlDate) {
  // Declare all variables
  var i, daytab, tablinks;

  // Get all elements with class="daytab" and hide them
  daytab = document.getElementsByClassName("daytab");
  for (i = 0; i < daytab.length; i++) {
    daytab[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(trvlDate).style.display = "block";
  evt.currentTarget.className += " active";
};
// accordion
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display == "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

// end of accordion


// $( function() {

// } );
// end of sortable

// delete list
$(document).ready(function () {
  $(".delli").on("click", function () {
    $(this).closest("li").remove();
  });

  // $("#sortable").sortable({
  //   placeholder: "ui-state-highlight"
  // });
  // $("#sortable").disableSelection();

  $(".sortable").sortable({
    placeholder: "ui-state-highlight"
  });
  $(".sortable").disableSelection();

  BTNclick('Shopping');

});

// end of the left
// now explore

filterSelection("all") // Execute the function and show all columns

function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("column");
  if (c == "all") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
};

// Show filtered elements
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
};

// Hide elements that are not selected
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
};

// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

//selector
  // $(".selector").change(function () {
  //   console.log('hi')
  //   console.log($(this))
  //   // $("ul#sortable").append("li.ui-state-default")
  //   // var sorttitle=("content-title").text(data[i]['RestName']);
  // });
  $('#WeStartHere').on('change','.selector',function(){
    if ($('#lalala').text() == "A"){
      var Hi = '#sp'+$(this).val()
      var Hi2 = '#daysp'+$(this).val()
    }
    else if ($('#lalala').text() == "H"){
      var Hi = "#sh"+$(this).val()
      var Hi2 = "#daysh"+$(this).val()
    }
    else if ($('#lalala').text() == "R"){
      var Hi = "#sr"+$(this).val()
      var Hi2 = "#daysr"+$(this).val()
    }
    console.log($(this).closest('select').attr('id'))
    // $(Hi).append($(this).attr('name'))
    $(Hi).append($(document.createElement('li')).addClass('ui-state-default').text($(this).attr('name')).attr('id',$(this).closest('select').attr('id')).append($(document.createElement('div')).addClass('delli').text("x")));
    $(".delli").on("click", function () {
      console.log($(this).closest("li").attr("id"))
      console.log($(Hi2).text())
      console.log($(Hi2).text().replace($(this).closest('li').attr('id')+'/',''))
      $(Hi2).text($(Hi2).text().replace($(this).closest('li').attr('id')+'/',''))
      $(this).closest("li").remove();
      // console
      // $(Hi2).replace($(this).closest('select').attr('id')+"/","")
    });
    $(Hi2).append($(this).closest('select').attr('id')+"/")

  })

//Willy try Code

$('.WFilterbyName').click(function(){
  var CurrentState = $(this).text();
  console.log(CurrentState)
  if ($('#lalala').text() == "A"){
    var AppendIDCheck = '#sp'
    var AppendID = 'idAttraction'
    var AppendSelect = 'Attraction'
  }
  else if ($('#lalala').text() == "H"){
    var AppendIDCheck = "#sh"
    var AppendID = 'id_hotel'
    var AppendSelect = 'Hotel'
  }
  else if ($('#lalala').text() == "R"){
    var AppendIDCheck = "#sr"
    var AppendID = 'Resid'
    var AppendSelect = 'Restaurant'
  }

  $.ajax({
  url: 'ajax/Wchange/',
  data: {
    'CurrentFilter': CurrentState,
    'CheckForSelect' : AppendSelect
  },
  dataType: 'json',
  success: function (data) {
    $('#WeStartHere').empty();
    console.log("hi")
    for(i = 0; i <= data.length;i++){

    var FinalR = $(document.createElement('div')).addClass('column show')
    console.log(FinalR)
    var PicContent = $(document.createElement('div')).addClass('content')

    if (data[i]['Img'] != ""){
      var smallPic = data[i]['Img']
    }
    else{
      // var smallPic = '../static/images/null.jpg'
      var smallPic = 'xxx'
    }
//add null pic

    PicContent.css('background-image',"url("+smallPic+")")
    var linktor = '/review/' + data[i]['ID']
    console.log(data[i]['ID'])
    var LinktoR = $(document.createElement('a')).attr('href',linktor).text(data[i]['Name'])
    var div1 = $(document.createElement('div')).addClass('content-overlay')
    var div2 = $(document.createElement('div')).addClass("content-details fadeIn-bottom")
    var PiCTitle = $(document.createElement('h3')).addClass("content-title")
    var PiCRate = $(document.createElement('p')).addClass('content-text').text('★★★★☆')
    //adding selector
    var PickADate= $(document.createElement('select')).addClass('selector').attr('name',data[i]['Name'])
    // var PickDate = $(document.createElement('option')).text('Hi')
    // PickADate.append(PickDate)
    var DfOption=$(document.createElement('option'));
      DfOption.text("Pick A Date")
      PickADate.append(DfOption)

    for (n = 1; n <= 5;n++){
      var DateOption=$(document.createElement('option')).attr("value",n);
      DateOption.text("Day"+n)
      // console.log(typeof DateOption)
      PickADate.append(DateOption)
      }

    // div2.append(PiCTitle,PiCRate,PickADate)
    // LinktoR.append(div1,div2)
    LinktoR.append(PiCTitle) // link pictitle to review?
    div2.append(LinktoR,PiCRate,PickADate)
    PicContent.append(div1,div2)
    FinalR.append(PicContent)
    $('#WeStartHere').append(FinalR)
  }
  }
});

})

function BTNclick(style_t){
  // var CurrentState = $(this).text();
  var CurrentState = style_t;
  console.log(typeof(style_t))
  if ($('#lalala').text() == "A"){
    // var AppendIDCheck = '#sp'
    var AppendID = 'idAttraction'
    var AppendSelect = 'Attraction'
  }
  else if ($('#lalala').text() == "H"){
    // var AppendIDCheck = "#sh"
    var AppendID = 'id_hotel'
    var AppendSelect = 'Hotel'
  }
  else if ($('#lalala').text() == "R"){
    // var AppendIDCheck = "#sr"
    var AppendID = 'Resid'
    var AppendSelect = 'Restaurant'
  }

  $.ajax({
  url: 'ajax/Wchange/',
  data: {
    'CurrentFilter': CurrentState,
    'CheckForSelect' : AppendSelect
  },
  dataType: 'json',
  success: function (data) {
    $('#WeStartHere').empty();
    console.log("hi")
    for(i = 0; i <= data.length;i++){

    var FinalR = $(document.createElement('div')).addClass('column show')
    console.log(FinalR)
    var PicContent = $(document.createElement('div')).addClass('content')

    if (data[i]['Img'] != ""){
      var smallPic = data[i]['Img']
      console.log(smallPic)
    }

    else{
      var smallPic = '../static/images/null.jpg'
      console.log('NULL IMG'+smallPic)
    }
//add null pic

    PicContent.css('background-image',"url("+smallPic+")")
    var linktor = '/review/?placeide=' + data[i]['Id']
    var LinktoR = $(document.createElement('a')).attr('href',linktor).text(data[i]['Name'])
    var div1 = $(document.createElement('div')).addClass('content-overlay')
    var div2 = $(document.createElement('div')).addClass("content-details fadeIn-bottom")
    var PiCTitle = $(document.createElement('h3')).addClass("content-title").html(LinktoR)
    var StarsNum = ['☆☆☆☆☆','★☆☆☆☆','★★☆☆☆','★★★☆☆','★★★★☆','★★★★★']
    var GetRating = data[i]['GetRating']
    var PiCRate = $(document.createElement('p')).addClass('content-text').text(StarsNum[GetRating])
    //adding selector
    var PickADate= $(document.createElement('select')).addClass('selector').attr('name',data[i]['Name']).attr('id',data[i]['Id'])
    // var PickDate = $(document.createElement('option')).text('Hi')
    // PickADate.append(PickDate)
    var DfOption=$(document.createElement('option'));
      DfOption.text("Pick A Date")
      PickADate.append(DfOption)
    console.log(data[i]['GetTpday'])
    for (n = 1; n <= data[i]['GetTpday'];n++){
      var DateOption=$(document.createElement('option')).attr("value",n);
      DateOption.text("Day"+n)
      // console.log(typeof DateOption)
      PickADate.append(DateOption)
      }

      PiCTitle.append(LinktoR) // link pictitle to review?
      div2.append(PiCTitle,PiCRate,PickADate)
      PicContent.append(div1,div2)
      FinalR.append(PicContent)
      $('#WeStartHere').append(FinalR)
  }
  }
});

}

// end of explore
