$(function () {
    $('input.dates').daterangepicker({
"autoApply": true,
"maxSpan": {
"days": 7},
"locale": {
"format": "MM/DD/YYYY",
"separator": " - ",
"applyLabel": "Apply",
"cancelLabel": "Cancel",
"fromLabel": "From",
"toLabel": "To",
"customRangeLabel": "Custom",
"weekLabel": "W",
"daysOfWeek": [
    "S",
    "M",
    "T",
    "W",
    "T",
    "F",
    "S"
],
"monthNames": [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
],
"firstDay": 1
},
"startDate": "05/18/2018",
"endDate": "05/24/2018"
},
function(start, end, label) {
console.log('New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')');
})});
