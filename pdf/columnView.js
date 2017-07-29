const pdf = require('pdfjs')
var fs = require('fs');

const doc = new pdf.Document({
  font: new pdf.Font(require('pdfjs/font/helvetica.json')),
  padding: 40,
  height: 504,
  width: 360
})
doc.pipe(fs.createWriteStream('columnView.pdf'))

//dates ordered from oldest to newest
var dates = 
{
    "17/01/01": ["LEFT Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/02": ["RIGHT Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/03": ["LEFT Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/04": ["RIGHT Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/05": ["LEFT Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."]
}


var table = doc.table({
  widths: [doc.width/2, doc.width/2],
  borderHorizontalWidths: function(i) { return i < 2 ? 1 : 0.1 },
  padding: 5
})

var keys = Object.keys(dates);
var i = 0;
var leftDay,
    rightDay,
    leftThings,
    rightThings;
while (i < keys.length-1) {
    console.log(i);
    leftDay = keys[i];
    rightDay = keys[i+1];
    console.log("L: " + leftDay);
    console.log("R: " + rightDay);
    leftThings = dates[leftDay];
    rightThings = dates[rightDay];
    addDateHeaders(leftDay, rightDay);
    addThings(leftThings, rightThings);
    i += 2;
}
if (keys.length%2 != 0) {
    leftDay = keys[i];
    leftThings = dates[leftDay]
    addOddPage(leftDay, leftThings);
}
//TODO account for odd num of pages


function addDateHeaders(leftDate, rightDate) {
    var tr = table.row();
    var left = tr.cell().text();
    left.add(getRawDay(leftDate), {fontSize:40, font: new pdf.Font(require('pdfjs/font/helvetica-bold.json')),lineHeight: 1.15})
        .br()
        .add(getShortMonth(leftDate), {fontSize: 20, color: 0xa0a0a0, lineHeight: .35})
        .br()
        .add(getYear(leftDate), {fontSize: 20, lineHeight: .75});
    if (rightDate != null) {
        var right = tr.cell().text();
        right.add(getRawDay(rightDate), {fontSize:40, font: new pdf.Font(require('pdfjs/font/helvetica-bold.json')),lineHeight: 1.15})
            .br()
            .add(getShortMonth(rightDate), {fontSize: 20, color: 0xa0a0a0, lineHeight: .35})
            .br()
            .add(getYear(rightDate), {fontSize: 20, lineHeight: .75});
    }
}

function addThings(leftDate, rightDate) {
    var tr = table.row();
    var left = tr.cell().text();
    left.add(leftDate[0], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(leftDate[1], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(leftDate[2], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(leftDate[3], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(leftDate[4], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0});
    var right = tr.cell().text();
    right.add(rightDate[0], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(rightDate[1], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(rightDate[2], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(rightDate[3], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(rightDate[4], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0});
}

function addOddPage(day, things) {
    var leftDate = doc.cell().text();
    leftDate.add(getRawDay(day), {fontSize:40, font: new pdf.Font(require('pdfjs/font/helvetica-bold.json')),lineHeight: 1.15})
        .br()
        .add(getShortMonth(day), {fontSize: 20, color: 0xa0a0a0, lineHeight: .35})
        .br()
        .add(getYear(day), {fontSize: 20, lineHeight: .75});
    var left = doc.cell({ paddingRight: 143}).text();
    left.add(things[0], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(things[1], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(things[2], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(things[3], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0})
        .br()
        .add(things[4], {
                fontSize: 8, 
                padding: 1.25,
                borderLeftWidth: 1, 
                borderLeftColor: 0xa0a0a0});
}


//given a date in YY-MM-DD get the month
function getShortMonth(date) {
    var month = date.substring(3, 5);
    var monthNames = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
    "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"];
    return monthNames[parseInt(month)-1];
}

//given a date in YY-MM-DD get the year
function getYear(date) {
    var year = date.substring(0, 2);
    return "20" + year;
}

//returns the date in DD format
function getRawDay(date) {
    var day = date.substring(6, 8);
    day = parseInt(day);
    return ("0" + day).slice(-2);
}



(async ()=>{
    try{
      var result = await doc.end();
    }catch(e){
      console.log(e)
    }
})();