var express = require('express');
var router = require('./src/router')
var app = express();

app.use('/static', express.static('static'));
app.use('/src', express.static('src'));
app.use('/', router);

app.listen(8080);

module.exports = app;
