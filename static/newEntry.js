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
var provider = new firebase.auth.GoogleAuthProvider();

var username;

//set up initial state
document.getElementById('date').valueAsDate = new Date();

//set up event listeners
document.getElementById('date').addEventListener("change", pullInData);
document.getElementById('saveButton').addEventListener("click", formatData);
document.getElementById('logInButton').addEventListener("click", signIn);
document.getElementById('logOutButton').addEventListener("click", signOut);


//set up auth state
firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.
    document.getElementById("overlay").style.width = "0%";
    username = user.uid;
    pullInData();
  } else {
    // No user is signed in, show overlay and clear fields
    document.getElementById("overlay").style.width = "100%";
    resetFields();
  }
});

function pullInData() {
  console.log('pulling in data');
  var date = formatDate(document.getElementById('date').value);
  var user = firebase.auth().currentUser;
  if (user == null) {
    console.log("whaaaaa");
  }
  console.log(date);
  firebase.database().ref('/users/' + username + "/" + date).once('value').then(function(snapshot) {
    if (snapshot.val() == null) {
      console.log('reseting fields');
      resetFields();
    } else {
      var things = snapshot.val();
      console.log(things);
      document.getElementById('one').value = things[0];
      document.getElementById('two').value = things[1];
      document.getElementById('three').value = things[2];
      document.getElementById('four').value = things[3];
      document.getElementById('five').value = things[4];
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

//convert date to MM-DD-YY
function formatDate(date) {
    //turn string to date object
    var b = date.split(/\D/);
    var date = new Date(b[0], --b[1], b[2]);

    var dateString = ("0" + (date.getMonth() + 1).toString()).substr(-2) + "-" + ("0" + date.getDate().toString()).substr(-2)  + "-" + (date.getFullYear().toString()).substr(2);

    return dateString;
}


function formatData() {
  var date = formatDate(document.getElementById('date').value);
  var things = {
    0: document.getElementById('one').value,
    1: document.getElementById('two').value,
    2: document.getElementById('three').value,
    3: document.getElementById('four').value,
    4: document.getElementById('five').value
    //TODO make all fields required?
  }
  writeUserData(date, things);
}

function writeUserData(date, things) {
  console.log('writing to db');
	//save overwrites the current data at the location
  firebase.database().ref('users/' + username + "/" + date).set({
    0: things
  });
  //TODO make it so it stays on current date instead of refreshing
}

function signIn() {
  firebase.auth().signInWithRedirect(provider);
}

function signOut() {
  firebase.auth().signOut().then(function() {
  // Sign-out successful.
  }).catch(function(error) {
    // An error happened.
  });
}