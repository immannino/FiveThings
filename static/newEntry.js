var firebase = require("firebase");

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

//set up initial state
document.getElementById('date').valueAsDate = new Date();
pullInData();

//set up event listeners
document.getElementById('date').addEventListener("change", pullInData);
document.getElementById('submitButton').addEventListener("click", formatData);


function pullInData() {
  var date = document.getElementById('date').value;
  var userId = "username1"; //firebase.auth().currentUser.uid;
  firebase.database().ref('/users/' + userId + "/" + date).once('value').then(function(snapshot) {
    if (snapshot.val() == null) {
      resetFields();
    } else {
      var things = snapshot.val().things;
      document.getElementById('one').value = things.one;
      document.getElementById('two').value = things.two;
      document.getElementById('three').value = things.three;
      document.getElementById('four').value = things.four;
      document.getElementById('five').value = things.five;
    }
  });
}

function resetFields() {
  document.getElementById('one').value = "";
  document.getElementById('two').value = "";
  document.getElementById('three').value = "";
  document.getElementById('four').value = "";
  document.getElementById('five').value = "";
}


function formatData() {
  var date = document.getElementById('date').value;
  var things = {
    one: document.getElementById('one').value,
    two: document.getElementById('two').value,
    three: document.getElementById('three').value,
    four: document.getElementById('four').value,
    five: document.getElementById('five').value
    //TODO make all fields required?
  }
  writeUserData("username1", date, things);
}

function writeUserData(userId, date, things) {
	//save overwrites the current data at the location
  firebase.database().ref('users/' + userId + "/" + date).set({
    things: things
  });
}

