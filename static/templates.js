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

//set up auth state
firebase.auth().onAuthStateChanged(function(user) {
  console.log("bloop")
  if (user) {
    //User is signed in.
    username = user.uid;
    getEntriesInRange("18-01-08", "16-04-28");
  } else {
    console.log("not logged in for realz")
    //No user is signed in, show overlay and clear fields
    //TODO
  }
});


console.log('bleeeep');

function getEntriesInRange(startDate, endDate) {
  //TODO check start date is before endDate

  var user = firebase.auth().currentUser;
    if (user != null) {
      var ref = firebase.database().ref('/users/' + username);
      ref.orderByKey().startAt(startDate).endAt(endDate)
        .on("child_added", function(snapshot){
          var day = snapshot.key
          console.log(day)
          var things = snapshot.val()
        });
    } else {
      console.log("user not logged in!!");
      //TODO get user to log in
    }
}