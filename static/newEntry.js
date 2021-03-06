var firebase = require("firebase")
var TinyDatePicker = require('tiny-date-picker')

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

var username
var writtenDays = []
var date = new Date()

//set up event listeners
document.getElementById('saveButton').addEventListener("click", formatData);
document.getElementById('logInButton').addEventListener("click", signIn);
document.getElementById('logOutButton').addEventListener("click", signOut);
document.getElementById('one').addEventListener("keyup", stateHasChanged);
document.getElementById('two').addEventListener("keyup", stateHasChanged);
document.getElementById('three').addEventListener("keyup", stateHasChanged);
document.getElementById('four').addEventListener("keyup", stateHasChanged);
document.getElementById('five').addEventListener("keyup", stateHasChanged);
document.onkeydown = function(e) {
    if (!isTyping()) {
      switch (e.keyCode) {
          case 37:
              getPrevDate();
              break;
          case 39:
              getNextDate();
              break;
      }
    }
};


//set up auth state
firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.
    document.getElementById("overlay").style.width = "0%";
    username = user.uid;

    updateDatePicker()
    
    getToday()
  } else {
    // No user is signed in, show overlay and clear fields
    document.getElementById("overlay").style.width = "100%";
    resetFields();
  }
});


function buildDatePicker() {
  const datePicker = TinyDatePicker('#date', {
            mode: 'dp-below',
            format(date) {
              return getPrettyDate(date)
            },
            parse(prettyDate) {
              return getUglyDate(prettyDate)
            },
            max: new Date(),
            dateClass(day) {
              var dayString = getDatabaseStyleDate(day)
              return writtenDays.includes(dayString+"") ? 'dp-written' : ''
              
            }
          })    

  datePicker.on('select', (_, picker) =>  {
    date = picker.state.selectedDate  
    pullInData() 
  })
}

function pullInData() {
  var dateStyled = getDatabaseStyleDate(date)

  var user = firebase.auth().currentUser;
  if (user != null) {
    firebase.database().ref('/users/' + username + "/" + dateStyled).once('value').then(function(snapshot) {
      if (snapshot.val() == null) {
        resetFields(); //no things for this day
      } else {
        var things = snapshot.val()
        document.getElementById('one').value = things[0]
        document.getElementById('two').value = things[1]
        document.getElementById('three').value = things[2]
        document.getElementById('four').value = things[3]
        document.getElementById('five').value = things[4]
      }
    });
    stateHasChanged();
  }
}

function getPrevDate() {
  date.setDate(date.getDate() - 1)
  document.getElementById('date').value = getPrettyDate(date)
  pullInData(); 
}

function getNextDate() {
  date.setDate(date.getDate() + 1)
  document.getElementById('date').value = getPrettyDate(date)
  pullInData(); 
}

function getToday() {
  var today = new Date();
  date = today
  var month = today.getMonth() + 1; // months are zero-indexed for some reason
  var dateStr = today.getFullYear() + "-" + month + "-" + today.getDate();
  document.getElementById("date").value = getPrettyDate(today)
  pullInData(today);
}

//fetches all the dates that a user has data for
function updateDatePicker() {
  var days = []
  var user = firebase.auth().currentUser;

  if (user != null) {
    firebase.database().ref('/users/' + username).once('value').then(function(snapshot) {
      if (snapshot.val() != null) {
        var data = snapshot.val()
        writtenDays = Object.keys(data)
        buildDatePicker()
      }
    })
  }
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

function formatData() {
  var things = {
    0: document.getElementById('one').value,
    1: document.getElementById('two').value,
    2: document.getElementById('three').value,
    3: document.getElementById('four').value,
    4: document.getElementById('five').value
  }

  writeUserData(things);
}

function fieldsAreEmpty(things) {
  if (things[0] == "" &&
      things[1] == "" &&
      things[2] == "" &&
      things[3] == "" &&
      things[4] == "") {
    return true
  }
  return false
}

function writeUserData(things) {

  //save overwrites the current data at the location
  firebase.database().ref('users/' + username + "/" + getDatabaseStyleDate(date)).set(
    (fieldsAreEmpty(things)) ? null : { 0: things[0], 1: things[1], 2: things[2], 3: things[3], 4: things[4]}
  ).then(function () {
      document.getElementById('saveButton').innerHTML = 'Saved';
      updateDatePicker()
    });;
}

//called when five things have been edited before last save
function stateHasChanged() {
  document.getElementById('saveButton').innerHTML = 'Save';
}

function isTyping() {
  return document.getElementById('one') === document.activeElement ||
         document.getElementById('two') === document.activeElement ||
         document.getElementById('three') === document.activeElement ||
         document.getElementById('four') === document.activeElement ||
         document.getElementById('five') === document.activeElement ||
         document.getElementById('date') === document.activeElement;
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

function getPrettyDate(date) {
  var days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  var dayOfWeek = days[date.getDay()]
  var month = getMonth(date.getMonth())
  var day = ordinal_suffix_of(date.getDate())
  var year = date.getFullYear()
  return dayOfWeek + " " + month + " " + day + ", " + year
}

function getUglyDate(prettyDate) {
  var words = prettyDate.split(" ")
  console.log(words)
  var month = words[1]
  var dayStr = words[2]
  dayStr = dayStr.substring(0, dayStr.length-3)
  var year = words[3]
  return new Date(month + " " + dayStr + ", " + year)
}

//takes in a date object and converts to YY-MM-DD
function getDatabaseStyleDate(date)  {
  var month = '' + (date.getMonth() + 1),
      day = '' + date.getDate(),
      year = date.getFullYear().toString().substr(-2)
  if (month.length < 2) month = '0' + month;
  if (day.length < 2) day = '0' + day;

  return [year, month, day].join('-');
}

function getMonth(month) {
  var monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"];
  return monthNames[parseInt(month)];
}

function ordinal_suffix_of(i) {
  var j = i % 10,
      k = i % 100;
  if (j == 1 && k != 11) {
      return i + "st";
  }
  if (j == 2 && k != 12) {
      return i + "nd";
  }
  if (j == 3 && k != 13) {
      return i + "rd";
  }
  return i + "th";
}