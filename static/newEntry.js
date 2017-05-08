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

//set up auth state
firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.
    document.getElementById('logInOut').innerHTML = 'Sign Out';
    document.getElementById('logInOut').addEventListener("click", signOut);
    username = user.uid;
    pullInData();
  } else {
    // No user is signed in.
    document.getElementById('logInOut').innerHTML = 'Sign In';
    document.getElementById('logInOut').addEventListener("click", signIn);
    username = "NOOOOOO";
    pullInData();
  }
});



//set up event listeners
document.getElementById('date').addEventListener("change", pullInData);
document.getElementById('submitButton').addEventListener("click", formatData);


function pullInData() {
  var date = document.getElementById('date').value;
  var user = firebase.auth().currentUser;
  if (user == null) {
    console.log("whaaaaa");
  }
  firebase.database().ref('/users/' + username + "/" + date).once('value').then(function(snapshot) {
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
  writeUserData(date, things);
}

function writeUserData(date, things) {
	//save overwrites the current data at the location
  firebase.database().ref('users/' + username + "/" + date).set({
    things: things
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