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

getToday();

//set up event listeners
document.getElementById('date').addEventListener("change", pullInData);
document.getElementById('logo').addEventListener("click", getToday);
document.getElementById('saveButton').addEventListener("click", formatData);
document.getElementById('logInButton').addEventListener("click", signIn);
document.getElementById('logOutButton').addEventListener("click", signOut);
document.getElementById('left').addEventListener("click", getPrevDate);
document.getElementById('right').addEventListener("click", getNextDate);
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

  if (date == "") {
    disableFields();
  } else {
    enableFields();
    var user = firebase.auth().currentUser;
    if (user != null) {
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
  }
}

function getPrevDate() {
  document.getElementById('date').stepDown(1);
  pullInData();
}

function getNextDate() {
  document.getElementById('date').stepUp(1);
  pullInData();
}

function getToday() {
  var today = new Date();
  // need to construct our own datestr because today.toISOString() returns date in UTC timezone.
  var month = today.getMonth() + 1; // months are zero-indexed for some reason
  var dateStr = today.getFullYear() + "-" + month + "-" + today.getDate();
  document.getElementById("date").value = new Date(dateStr).toISOString().substr(0, 10);
  pullInData();
}

function disableFields() {
  resetFields();
  document.getElementById('one').value = "Impossible date!";
  document.getElementById('one').disabled = true;
  document.getElementById('two').disabled = true;
  document.getElementById('three').disabled = true;
  document.getElementById('four').disabled = true;
  document.getElementById('five').disabled = true;
  document.getElementById('saveButton').disabled = true;
}

function enableFields() {
  document.getElementById('one').disabled = false;
  document.getElementById('two').disabled = false;
  document.getElementById('three').disabled = false;
  document.getElementById('four').disabled = false;
  document.getElementById('five').disabled = false;
  document.getElementById('saveButton').disabled = false;
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