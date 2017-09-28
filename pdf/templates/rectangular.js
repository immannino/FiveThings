const pdf = require('pdfjs')
var fs = require('fs');

const doc = new pdf.Document({
  font: new pdf.Font(fs.readFileSync('./pdf/fonts/questa.otf')), 
  padding: 30,
  height: 504,
  width: 360
})
doc.pipe(fs.createWriteStream('fiveBySeven.pdf'))

//dates ordered from oldest to newest
var dates = 
{
    "17/01/01": ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"],
    "17/01/02": ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"],
}

doc.cell().text('Five Things', { fontSize: 54, textAlign: 'center' });

var keys = Object.keys(dates);
var firstDay = keys[0];
var lastDay = keys[keys.length -1];
var range = formatDate(firstDay) + " - " + formatDate(lastDay);

doc.cell().text(range, { fontSize: 24, textAlign: 'center', font: new pdf.Font(fs.readFileSync('./pdf/fonts/bebasbook.otf')) });

doc.pageBreak();
doc.pageBreak();

for (var date in dates) {
    if (dates.hasOwnProperty(date)) {
        var things = dates[date];
        buildPage(date, things);
    }
}

function buildPage(date, things) {

    var formattedDate = formatDate(date);
    doc.cell().text(formattedDate, { fontSize: 35, textAlign: 'center', font: new pdf.Font(fs.readFileSync('./pdf/fonts/bebasbook.otf')) });

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
  tr.cell().text(thing, { fontSize: 11, textAlign: 'justified' });
}

//converts date from YY-MM-DD to month day, year
function formatDate(date) {
    var year = date.substring(0, 2);
    var month = date.substring(3, 5);
    var day = date.substring(6, 8);

    var monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];

    var monthString = monthNames[parseInt(month)-1];
    var dayString = parseInt(day);
    var yearString = "20" + year;

    return monthString + " " + dayString + ", " + yearString;
}

(async ()=>{
    try{
      var result = await doc.end();
    }catch(e){
      console.log(e)
    }
})();