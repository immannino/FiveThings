var firebase = require("firebase");

document.getElementById('createButton').addEventListener("click", submit);

var email = document.getElementById('email');
var password1 = document.getElementById('password1');
var password2 = document.getElementById('password2');

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


function submit() {
    if (passwordsMatch(password1, password2)) {
        firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
            // TODO Handle Errors here.
                //https://firebase.google.com/docs/reference/js/firebase.auth.Auth#createUserWithEmailAndPassword
            var errorCode = error.code;
            var errorMessage = error.message;
            // ...
        });
    } else {
        //TODO handle non matching passwords
    }
}

//Handle Account Status
firebase.auth().onAuthStateChanged(user => {
  if(user) {
      //a user has logged in
      //window.location = 'index.html'; //After successful login, user will be redirected to index.html
  }
});

//TODO dont let a signed in user go to the create account page