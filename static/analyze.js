var firebase = require("firebase");
var heatMap = require("calendar-heatmap-mini");
var positivity = require('Sentimental').positivity;
var negativity = require('Sentimental').negativity;


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
  if (user != null) {
    firebase.database().ref('/users/' + username).once('value').then(function(snapshot) {
      if (snapshot.val() != null) {
        var days = snapshot.val();
        analyzeDays(days);
      }
    });
  }
}

function analyzeDays(days) {
    var positive = new Array();
    var negative = new Array();
    for (var day in days) {
        var things = days[day];
        var date = new Date("20" + day);
        var dataPositive = {date: date, count: scoreDay(things, true)};
        var dataNegative = {date: date, count: scoreDay(things, false)};
        positive.push(dataPositive);
        negative.push(dataNegative);
    }
    chart(positive, negative);
}

function scoreDay(things, isPositive) {
    var total = 0;
    for (var i = 0; i < things.length; i++) {
        var rating = (isPositive ? positivity(things[i]).score : negativity(things[i]).score);
        total += rating;
    }
    var average = total/things.length;
    return average;
}

function chart(positive, negative) {

    const chart1 = heatMap()
                .data(positive)
                .selector('#positive')
                .colorRange(['#D8E6E7', '#76dd27'])
                .tooltipEnabled(true)
                .onClick(function (data) {
                    console.log('onClick callback. Data:', data);
                });

    // render the chart
    chart1();

    const chart2 = heatMap()
                .data(negative)
                .selector('#negative')
                .colorRange(['#D8E6E7', '#e8482c'])
                .tooltipEnabled(true)
                .onClick(function (data) {
                    console.log('onClick callback. Data:', data);
                });

    // render the chart
    chart2();
}

