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
var today = new Date();
document.getElementById("date").value = today.toISOString().substr(0, 10);


//set up event listeners
document.getElementById('date').addEventListener("change", pullInData);
document.getElementById('saveButton').addEventListener("click", formatData);
document.getElementById('logInButton').addEventListener("click", signIn);
document.getElementById('logOutButton').addEventListener("click", signOut);
document.getElementById('one').addEventListener("keyup", stateHasChanged);
document.getElementById('two').addEventListener("keyup", stateHasChanged);
document.getElementById('three').addEventListener("keyup", stateHasChanged);
document.getElementById('four').addEventListener("keyup", stateHasChanged);
document.getElementById('five').addEventListener("keyup", stateHasChanged);


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
  var date = formatDate(document.getElementById('date').value);
  var user = firebase.auth().currentUser;
  if (user == null) {
    console.log("whaaaaa");
    //TODO handle this case where user isn't logged in
  }
  firebase.database().ref('/users/' + username + "/" + date).once('value').then(function(snapshot) {
    if (snapshot.val() == null) {
      resetFields();
    } else {
      var things = snapshot.val();
      document.getElementById('one').value = things[0];
      document.getElementById('two').value = things[1];
      document.getElementById('three').value = things[2];
      document.getElementById('four').value = things[3];
      document.getElementById('five').value = things[4];
    }
  });
  stateHasChanged();
}

function resetFields() {
  document.getElementById('one').value = "";
  document.getElementById('two').value = "";
  document.getElementById('three').value = "";
  document.getElementById('four').value = "";
  document.getElementById('five').value = "";
}

//convert date to YY-MM-DD
function formatDate(date) {  
    var dateString = date + "";
    return  dateString.substring(2);
}


function formatData() {
  var date = formatDate(document.getElementById('date').value);
  var things = {
    0: document.getElementById('one').value,
    1: document.getElementById('two').value,
    2: document.getElementById('three').value,
    3: document.getElementById('four').value,
    4: document.getElementById('five').value
  }
  writeUserData(date, things);
}

function writeUserData(date, things) {

  //save overwrites the current data at the location
  firebase.database().ref('users/' + username + "/" + date).set({
    0: things[0],
    1: things[1],
    2: things[2],
    3: things[3],
    4: things[4]
  }).then(function () {
      document.getElementById('saveButton').innerHTML = 'Saved';
    });;
  //TODO update button to say saved if successful
}

//called when five things have been edited before last save
function stateHasChanged() {
  document.getElementById('saveButton').innerHTML = 'Save';
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