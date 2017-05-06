var firebase = require("firebase");

document.getElementById('date').valueAsDate = new Date();

document.getElementById('submitButton').onclick = formatData();

console.log("helloooooo");

  // Initialize Firebase
var config = {
    apiKey: "AIzaSyC7amfR9cLvP0zph_Dghfqt3XUzbZTn9IU",
    authDomain: "fivethings-20a79.firebaseapp.com",
    databaseURL: "https://fivethings-20a79.firebaseio.com",
    projectId: "fivethings-20a79",
    storageBucket: "fivethings-20a79.appspot.com",
    messagingSenderId: "882067772741"
  };
firebase.initializeApp(config);

var database = firebase.database();

function formatData() {
  var date = document.getElementById('date').value;
  var things = {
    one: document.getElementById('one').value,
    two: document.getElementById('two').value,
    three: document.getElementById('three').value,
    four: document.getElementById('four').value,
    five: document.getElementById('five').value
  }

  writeUserData("userID", date, things);
}


function writeUserData(userId, date, things) {
	//save overwrites the current data at the location
  firebase.database().ref('users/' + userId).set({
    date: date,
    things: things
  });
}

