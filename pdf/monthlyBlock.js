const pdf = require('pdfjs')
var fs = require('fs');

const doc = new pdf.Document({
  font: new pdf.Font(require('pdfjs/font/helvetica.json')),
  padding: 40,
  height: 504,
  width: 360
})
doc.pipe(fs.createWriteStream('monthBlock.pdf'))

//dates ordered from oldest to newest
var dates = 
{
    "17/01/01": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/02/02": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/03/03": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/04/04": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
}

doc.text('January 2017', { fontSize: 54, textAlign: 'center' });

doc.pageBreak();
doc.pageBreak();

var isRightPage = true;
for (var date in dates) {
    if (dates.hasOwnProperty(date)) {
        var things = dates[date];
        isRightPage ? buildRightPage(date, things) : buildLeftPage(date, things);
        isRightPage = !isRightPage;
    }
}

function buildRightPage(date, things) {

    var table = doc.table({
        widths: [8*pdf.cm, null],
        padding: 1
    });
    var row = table.row();
    row.cell();
    row.cell(getRawDay(date), {fontSize:40, font: new pdf.Font(require('pdfjs/font/helvetica-bold.json')),lineHeight: 1.15});
    var row1 = table.row();
    row1.cell();
    row1.cell(getShortMonth(date), {fontSize: 20, color: 0xa0a0a0, lineHeight: .35});
    var row2 = table.row();
    row2.cell();
    row2.cell(getYear(date), {fontSize: 20, lineHeight: .75});
    
    addRows(things);
    doc.pageBreak()
}

function addRows(things) {
    doc.cell('', {
        fontSize: 10, 
        padding: 5,
        borderLeftColor: 0xFFFFFF
    });
    addRow(things[0]);
    addRow(things[1]);
    addRow(things[2]);
    addRow(things[3]);
    addRow(things[4]);
}

function buildLeftPage(date, things) {

    var table = doc.table({
        widths: [null, 8*pdf.cm],
        padding: 1
    });
    var row = table.row();
    row.cell(getRawDay(date), {fontSize:40, font: new pdf.Font(require('pdfjs/font/helvetica-bold.json')),lineHeight: 1.15});
    row.cell();
    var row1 = table.row();
    row1.cell(getShortMonth(date), {fontSize: 20, color: 0xa0a0a0, lineHeight: .35});
    row1.cell();
    var row2 = table.row();
    row2.cell(getYear(date), {fontSize: 20, lineHeight: .75});
    row2.cell();

    addRows(things);
    doc.pageBreak()
}

function addRow(thing) {
    doc.cell(thing, {
        fontSize: 9.2, 
        padding: 1.25,
        borderLeftWidth: 1, 
        borderLeftColor: 0xa0a0a0
    });
    doc.cell('', {
        fontSize: 10, 
        padding: 3,
        borderLeftColor: 0xFFFFFF
    });
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