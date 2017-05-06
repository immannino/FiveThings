var express = require('express');
var router = require('./src/router')
// var firebase = require("firebase");
var path = require('path');
var app = express();

// // Initialize Firebase
// var config = {
//     apiKey: "AIzaSyC7amfR9cLvP0zph_Dghfqt3XUzbZTn9IU",
//     authDomain: "fivethings-20a79.firebaseapp.com",
//     databaseURL: "https://fivethings-20a79.firebaseio.com",
//     projectId: "fivethings-20a79",
//     storageBucket: "fivethings-20a79.appspot.com",
//     messagingSenderId: "882067772741"
//   };
// const db = firebase.initializeApp(config);

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));


app.use('/static', express.static(path.join(__dirname, 'static')));

// Routes
app.use('/', router);

app.listen(8080);

module.exports = app;
