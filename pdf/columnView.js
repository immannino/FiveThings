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
    "17/01/01": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/02": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/03": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/04": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/05": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/06": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/07": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
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
    rightThings,
    table;
while (i < keys.length) {
    table = doc.table({
        widths: [doc.width/2, doc.width/2],
        borderHorizontalWidths: function(i) { return i < 2 ? 1 : 0.1 },
        padding: 5
    })
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
    doc.pageBreak();
}


function addDateHeaders(leftDate, rightDate) {
    var tr = table.row();
    var left = tr.cell().text(getRawDay(leftDate), {textAlign: 'center', fontSize: 35, font: new pdf.Font(require('pdfjs/font/helvetica-bold.json'))});
    if (rightDate != null) {
        tr.cell().text(getRawDay(rightDate), {textAlign: 'center', fontSize: 35, font: new pdf.Font(require('pdfjs/font/helvetica-bold.json'))})
    } else {
         tr.cell().text("  ");
    }
}

function addThings(leftDate, rightDate) {
    var tr = table.row();
    var left = tr.cell().text();
    left.add(leftDate[0], {
                fontSize: 7, 
                padding: 1.25})
        .br()
        .br()
        .add(leftDate[1], {
                fontSize: 7, 
                padding: 1.25})
        .br()
        .br()
        .add(leftDate[2], {
                fontSize: 7, 
                padding: 1.25})
        .br()
        .br()
        .add(leftDate[3], {
                fontSize: 7, 
                padding: 1.25})
        .br()
        .br()
        .add(leftDate[4], {
                fontSize: 7, 
                padding: 1.25});
    var right = tr.cell().text();
    if (rightDate != null) {
        right.add(rightDate[0], {
                    fontSize: 7, 
                    padding: 1.25})
            .br()
            .br()
            .add(rightDate[1], {
                    fontSize: 7, 
                    padding: 1.25})
            .br()
            .br()
            .add(rightDate[2], {
                    fontSize: 7, 
                    padding: 1.25})
            .br()
            .br()
            .add(rightDate[3], {
                    fontSize: 7, 
                    padding: 1.25})
            .br()
            .br()
            .add(rightDate[4], {
                    fontSize: 7, 
                    padding: 1.25});
    } else {
        right.add("   ");
    }
}

function addOddPage(day, things) {
    doc.cell().text(getRawDay(day), {textAlign: 'center', fontSize: 35, font: new pdf.Font(require('pdfjs/font/helvetica-bold.json'))});
    var left = doc.cell({ paddingRight: 143}).text();
    left.add(things[0], {
                fontSize: 7, 
                padding: 1.25})
        .br()
        .br()
        .add(things[1], {
                fontSize: 7, 
                padding: 1.25})
        .br()
        .br()
        .add(things[2], {
                fontSize: 7, 
                padding: 1.25})
        .br()
        .br()
        .add(things[3], {
                fontSize: 7, 
                padding: 1.25})
        .br()
        .br()
        .add(things[4], {
                fontSize: 7, 
                padding: 1.25});
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