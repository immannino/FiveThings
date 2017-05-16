const pdf = require('pdfjs')
var fs = require('fs');


const doc = new pdf.Document({
  //font: new pdf.Font(require('pdfjs/font/helvetica.json')),
  font: new pdf.Font(fs.readFileSync('./questa.otf')), 
  padding: 54,
  height: 540,
  weight: 540
})
doc.pipe(fs.createWriteStream('output.pdf'))

var dates = {
    "01/01/17": [
        "Danced a bit more with dad and shonagh and niall, slowly destroyed my vocal chords, and sat around a fire singing songs until 4 am (last ones to leave woohoo!)", 
        "Had a lovely lie in and woke up with barely a voice and sat out in the sun with mum and dad for a while before going to circle c park to test out dad's new drone", 
        "Grabbed ellen and the poodles and made our way out to mckinney state park for more sunshine and dog walking in gorgeous weather", 
        "Picked up a quick pterrys and went home to eat that and hang with the family for a while before packing up all my crap", 
        "Played banagrams and chicken foot bingo with the family and then had tearful goodbyes with the family and headed off to bed"
    ], 
    "02/02/17": [
        "Woke up bright and early and got squished my suitcase and headed to the airport for a sad goodbye with dad", 
        "Sat around in the airport feeling pretty rubbish and got on the world hottest plane where i had to rub ice cubes against my body to stop from overheating", 
        "Took a taxi home and then headed out to eltana for a welcome home bagel and then to qfc to restock for a few days", 
        "Unpacked a little and then worked on making a flip clock android app for my new kindle", 
        "Cleaned up nada's mess and then watched the season premiere of the bachelor and also wall-e before going to bed nice and early"
    ], 
    "03/03/17": [
        "Woke up early and decided that i was feeling too crappy to go into work and went back to bed", 
        "Messed around on the internet for a while did research on investing and finance", 
        "Finally felt like eating and had grilled cheese and watched before the flood", 
        "Caught up with nada while she made the biggest mess in the kitchen and i bean-bagged it out", 
        "Got back on the internet and did nothing and eventually went to bed"
    ]
}

for (var date in dates) {
    if (dates.hasOwnProperty(date)) {
        //console.log(date + " -> " + dates[date]);
        var things = dates[date];
        buildPage(date, things);
    }
}

function buildPage(date, things) {

    var formattedDate = formatDate(date);

    doc.cell({ paddingBottom: 0.5*pdf.cm }).text(formattedDate, { 
        fontSize: 60, 
        textAlign: 'center',
        font: new pdf.Font(fs.readFileSync('./questa.otf')), });

    doc.cell({ paddingBottom: 8 }).text(things[0], { fontSize: 14, textAlign: 'justified' });
    doc.cell({ paddingBottom: 8 }).text(things[1], { fontSize: 14, textAlign: 'justified' });
    doc.cell({ paddingBottom: 8 }).text(things[2], { fontSize: 14, textAlign: 'justified' });
    doc.cell({ paddingBottom: 8 }).text(things[3], { fontSize: 14, textAlign: 'justified' });
    doc.cell().text(things[4], { fontSize: 14, textAlign: 'justified' });

    doc.pageBreak()
}

//converts date from MM-DD-YY to month day, year
function formatDate(date) {
    var month = date.substring(0, 2);
    var day = date.substring(3, 5);
    var year = date.substring(6, 8);

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
