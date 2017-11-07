const pdf = require('pdfjs')
var fs = require('fs');

const doc = new pdf.Document({
  font: new pdf.Font(fs.readFileSync('./pdf/fonts/Helvetica-Regular.ttf')),
  padding: 40,
  height: 7*72,
  width: 5*72
})
doc.pipe(fs.createWriteStream('./pdf/samples/simpleColumn.pdf'))

const img = new pdf.Image(fs.readFileSync('./pdf/assets/neutralCover.jpg'))
doc.image(img, {
  height: 424, align: 'center'
})
doc.pageBreak();
doc.pageBreak();

//dates ordered from oldest to newest
var dates = 
{
    "17/01/01": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior. ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  "],
    "17/01/02": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  "],
    "17/01/03": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  "],
    "17/01/04": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  "],
    "17/01/05": ["Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  ","Lorem ipsum dolor sit amet, vis paulo postulant definitiones ad. Ei meis brute imperdiet sed, eos eu aperiri abhorreant instructior.  "],
}

var keys = Object.keys(dates);
var i = 0;

while (i < keys.length) {
    var table = doc.table({
        widths: [doc.width/2, doc.width/2],
        padding: 3
    })
    leftDay = keys[i];
    rightDay = keys[i+1];
    leftThings = dates[leftDay];
    rightThings = dates[rightDay];
    addHeaders(leftDay, rightDay)
    leftThings = dates[leftDay];
    rightThings = dates[rightDay];
    addThings(leftThings, rightThings);
    i += 2;
    doc.pageBreak();
}

function addHeaders(leftDay, rightDay) {
    var font = new pdf.Font(fs.readFileSync('./pdf/fonts/didonesque.otf'))
    var tr = table.row({paddingBottom: 10});
    var leftHeader = tr.cell().text({fontSize: 21, lineHeight: .65, font: font})
    leftHeader.add(getDayOfWeek(leftDay)+"\n\n", {fontSize: 16, lineHeight: .65, font: font})
            .append(getMonth(leftDay)+" "+getDay(leftDay));
    if (rightDay != null) {
        var rightHeader = tr.cell().text({fontSize: 21, lineHeight: .65, font: font})
        rightHeader.add(getDayOfWeek(rightDay)+"\n\n", {fontSize: 16, lineHeight: .65, font: font})
            .append(getMonth(rightDay)+" "+getDay(rightDay));
    } else {
         tr.cell().text("  ");
    }
}

function addThings(leftThings, rightThings) {
    var tr = table.row();
    var left = tr.cell({paddingLeft: 20});
    var numbers = buildNumbers()
    addPadding(leftThings)
    left.image(numbers[0],  { height: .4*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[0]+"\n\n", {fontSize: 7.5, padding: 1.25})
    left.image(numbers[1],  { height: .4*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[1]+"\n\n", {fontSize: 7.5, padding: 1.25})
    left.image(numbers[2],  { height: .4*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[2]+"\n\n", {fontSize: 7.5, padding: 1.25})
    left.image(numbers[3],  { height: .4*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[3]+"\n\n", {fontSize: 7.5, padding: 1.25})
    left.image(numbers[4],  { height: .4*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[4], {fontSize: 7.5, padding: 1.25});
    var right = tr.cell({paddingLeft: 20});
    if (rightThings != null) {
        addPadding(rightThings)
        right.image(numbers[0],  { height: .4*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[0]+"\n\n", {fontSize: 7.5, padding: 1.25})
        right.image(numbers[1],  { height: .4*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[1]+"\n\n", {fontSize: 7.5, padding: 1.25})
        right.image(numbers[2],  { height: .4*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[2]+"\n\n", {fontSize: 7.5, padding: 1.25})
        right.image(numbers[3],  { height: .4*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[3]+"\n\n", {fontSize: 7.5, padding: 1.25})
        right.image(numbers[4],  { height: .4*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[4], {fontSize: 7.5, padding: 1.25});
    } else {
        right.text().add("   ");
    }
}

function buildNumbers() {
    var list =  new Array();
    var src = fs.readFileSync('./pdf/assets/one.jpg');
    var imgOne = new pdf.Image(src);
    list.push(imgOne);
    src = fs.readFileSync('./pdf/assets/two.jpg');
    var imgTwo = new pdf.Image(src);
    list.push(imgTwo);
    src = fs.readFileSync('./pdf/assets/three.jpg');
    var imgThree = new pdf.Image(src);
    list.push(imgThree);
    src = fs.readFileSync('./pdf/assets/four.jpg');
    var imgFour = new pdf.Image(src);
    list.push(imgFour);
    src = fs.readFileSync('./pdf/assets/five.jpg');
    var imgFive = new pdf.Image(src);
    list.push(imgFive)
    return list;
}

function addPadding(things) {
    for (var i=0; i<things.length; i++) {
        if (things[i].length<30) { //one line
            things[i] = things[i] + "\n\n"
        } else if (things[i].length<59) { //two lines
            things[i] = things[i] + "\n"
        }
    }
}

//takes in YY/MM/DD and gets day of week
function getDayOfWeek(date) {
    var year = parseInt("20" + date.substring(0, 2));
    var month = parseInt(date.substring(3, 5))-1;
    var day = parseInt(date.substring(6, 8));
    var theDate = new Date(year, month, day);
    console.log(theDate)
    var days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    return days[theDate.getDay()];
}

//takes in YY/MM/DD and gets date with ordinal
function getDay(date) {
    var day = date.substring(6, 8);
    var dayNum = parseInt(day);
    return ordinal_suffix_of(dayNum);
}

function ordinal_suffix_of(i) {
    var j = i % 10,
        k = i % 100;
    if (j == 1 && k != 11) {
        return i + "st";
    }
    if (j == 2 && k != 12) {
        return i + "nd";
    }
    if (j == 3 && k != 13) {
        return i + "rd";
    }
    return i + "th";
}

function getMonth(date) {
    var month = date.substring(3, 5);
    var monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];
    return monthNames[parseInt(month)-1];
}

(async ()=>{
    try{
      var result = await doc.end();
    }catch(e){
      console.log(e)
    }
})();