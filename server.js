var express = require('express');
var router = require('./src/router')
var path = require('path');
var http = require('http');
var app = express();



app.use('/static', express.static(path.join(__dirname, 'static')));

// Routes
app.use('/', router);

var port = process.env.port || 3000;
app.listen(port);

module.exports = app;
