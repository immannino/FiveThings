const pdf = require('pdfjs')
var fs = require('fs');

const doc = new pdf.Document({
  font: new pdf.Font(fs.readFileSync('./pdf/fonts/questa.otf')), 
  padding: 30,
  height: 504,
  width: 360
})
doc.pipe(fs.createWriteStream('month.pdf'))

//dates ordered from oldest to newest
var dates = 
{
    "17/01/01": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/02": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/03": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
    "17/01/04": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea.","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. Eu has eius choro dictas, ex nam cetero iriure invidunt. An ridens pertinacia nam, aliquid omittam ei mea."],
}

doc.text('January 2017', { fontSize: 54, textAlign: 'center' });

doc.pageBreak();
doc.pageBreak();

for (var date in dates) {
    if (dates.hasOwnProperty(date)) {
        var things = dates[date];
        buildPage(date, things);
    }
}

function buildPage(date, things) {

    doc.text(getDayOfWeek(date), {fontSize: 20, font: new pdf.Font(fs.readFileSync('./pdf/fonts/bebasbook.otf'))})
    doc.text(getMonth(date) + " " + getDay(date), {fontSize: 20, font: new pdf.Font(fs.readFileSync('./pdf/fonts/bebasbook.otf'))});
    doc.text(getYear(date), {fontSize: 20, font: new pdf.Font(fs.readFileSync('./pdf/fonts/bebasbook.otf'))});

    var table = doc.table({
        widths: [.75*pdf.cm, null],
        padding: 1
    });

    addRow(1, things[0], table);
    addRow(2, things[1], table);
    addRow(3, things[2], table);
    addRow(4, things[3], table);
    addRow(5, things[4], table);

    doc.pageBreak()
}

function addRow(number, thing, table) {
  var tr = table.row();
  tr.cell().text(number + "." , { fontSize: 10, textAlign: 'left' });
  tr.cell().text(thing, { fontSize: 9, textAlign: 'justified' });
}

//given a date in YY-MM-DD get the day of week
function getDayOfWeek(date) {
  var dayOfWeek = new Date("20" + date).getDay();    
  return isNaN(dayOfWeek) ? null : ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][dayOfWeek];
}

//given a date in YY-MM-DD get the month
function getMonth(date) {
    var month = date.substring(3, 5);
    var monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];
    return monthNames[parseInt(month)-1];
}

//given a date in YY-MM-DD get the year
function getYear(date) {
    var year = date.substring(0, 2);
    return "20" + year;
}

//given a date in YY-MM-DD get the day with ordinal
function getDay(date) {
    var day = date.substring(6, 8);
    day = parseInt(day);
    var j = day % 10,
    k = day % 100;
    if (j == 1 && k != 11) {
        return day + "st";
    }
    if (j == 2 && k != 12) {
        return day + "nd";
    }
    if (j == 3 && k != 13) {
        return day + "rd";
    }
    return day + "th";
}

(async ()=>{
    try{
      var result = await doc.end();
    }catch(e){
      console.log(e)
    }
})();