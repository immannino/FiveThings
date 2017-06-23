var firebase = require("firebase");
var sentiment = require('sentiment');

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

//set up auth state
firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.
    //document.getElementById("overlay").style.width = "0%";
    username = user.uid;
    console.log("user has logged in");
    pullInData();
  } else {
    // No user is signed in, show overlay
    console.log("user is not signed in")
    //document.getElementById("overlay").style.width = "100%";
  }
});

console.log("blerg");

function pullInData() {
  var user = firebase.auth().currentUser;
  if (user == null) {
    console.log("whaaaaa");
    //TODO handle this case where user isn't logged in
  }
  firebase.database().ref('/users/' + username).once('value').then(function(snapshot) {
    if (snapshot.val() == null) {
      //user has no data
    } else {
      var days = snapshot.val();
      analyzeDays(days);
    }
  });

}

function analyzeDays(days) {
    for (var day in days) {
        var things = days[day];
        var score = scoreDay(things);
        console.log(day + ": " + score);
    }
}

function scoreDay(things) {
    var total = 0;
    for (var i = 0; i < things.length; i++) {
        var rating = sentiment(things[i]).score;
        //console.log(rating);
        total += rating;
    }
    var average = total/things.length;
    return average;
}