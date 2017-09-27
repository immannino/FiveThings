const pdf = require('pdfjs')
var fs = require('fs');

const doc = new pdf.Document({
  font: new pdf.Font(fs.readFileSync('./pdf/Helvetica-Regular.ttf')),
  padding: 40,
  height: 7*72,
  width: 5*72
})
doc.pipe(fs.createWriteStream('NewColumn.pdf'))

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
    var font = new pdf.Font(fs.readFileSync('./pdf/didonesque.otf'))
    var tr = table.row();
    var leftHeader = tr.cell().text({textAlign: 'right', fontSize: 32, lineHeight: .65, font: font})
    leftHeader.add(getRawMonth(leftDay)+"\n"+getRawDay(leftDay)+"\n"+getShortYear(leftDay))
    if (rightDay != null) {
        var rightHeader = tr.cell().text({textAlign: 'right', fontSize: 32, lineHeight: .65, font: font})
        rightHeader.add(getRawMonth(rightDay)+"\n"+getRawDay(rightDay)+"\n"+getShortYear(rightDay))
    
    } else {
         tr.cell().text("  ");
    }
}

function addThings(leftThings, rightThings) {
    var tr = table.row();
    var left = tr.cell({paddingLeft: 25});
    var numbers = buildNumbers()
    addPadding(leftThings)
    left.image(numbers[0],  { height: .6*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[0]+"\n\n", {fontSize: 7.5, padding: 1.25})
    left.image(numbers[1],  { height: .6*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[1]+"\n\n", {fontSize: 7.5, padding: 1.25})
    left.image(numbers[2],  { height: .6*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[2]+"\n\n", {fontSize: 7.5, padding: 1.25})
    left.image(numbers[3],  { height: .6*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[3]+"\n\n", {fontSize: 7.5, padding: 1.25})
    left.image(numbers[4],  { height: .6*pdf.cm, wrap: false, x: 45})
    left.text(leftThings[4], {fontSize: 7.5, padding: 1.25});
    var right = tr.cell({paddingLeft: 25});
    if (rightThings != null) {
        addPadding(rightThings)
        right.image(numbers[0],  { height: .6*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[0]+"\n\n", {fontSize: 7.5, padding: 1.25})
        right.image(numbers[1],  { height: .6*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[1]+"\n\n", {fontSize: 7.5, padding: 1.25})
        right.image(numbers[2],  { height: .6*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[2]+"\n\n", {fontSize: 7.5, padding: 1.25})
        right.image(numbers[3],  { height: .6*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[3]+"\n\n", {fontSize: 7.5, padding: 1.25})
        right.image(numbers[4],  { height: .6*pdf.cm, wrap: false, x: 185})
        right.text(rightThings[4], {fontSize: 7.5, padding: 1.25});
    } else {
        right.text().add("   ");
    }
}

function buildNumbers() {
    var list =  new Array();
    var src = fs.readFileSync('./pdf/one.jpg');
    var imgOne = new pdf.Image(src);
    list.push(imgOne);
    src = fs.readFileSync('./pdf/two.jpg');
    var imgTwo = new pdf.Image(src);
    list.push(imgTwo);
    src = fs.readFileSync('./pdf/three.jpg');
    var imgThree = new pdf.Image(src);
    list.push(imgThree);
    src = fs.readFileSync('./pdf/four.jpg');
    var imgFour = new pdf.Image(src);
    list.push(imgFour);
    src = fs.readFileSync('./pdf/five.jpg');
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

function getRawDay(date) {
    var day = date.substring(6, 8);
    day = parseInt(day);
    return ("0" + day).slice(-2);
}

function getShortYear(date) {
    return date.substring(0, 2);
}

function getYear(date) {
    var year = date.substring(0, 2);
    return "20" + year;
}

function getRawMonth(date) {
    var month = date.substring(3, 5);
    month = parseInt(month);
    return ("0" + month).slice(-2);
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