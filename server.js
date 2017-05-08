var express = require('express');
var router = require('./src/router')
var path = require('path');
var app = express();


app.use('/static', express.static(path.join(__dirname, 'static')));

// Routes
app.use('/', router);

app.listen(8080);

module.exports = app;
