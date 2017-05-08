var express = require('express');
var router = express.Router();
var path = require('path');


router.get('/', function(req, res) {
	res.sendFile(path.join(__dirname + '/index.html'));
});

router.get('/create', function(req, res) {
	res.sendFile(path.join(__dirname + '/createAccount.html'));
});

router.get('/signin', function(req, res) {
	res.sendFile(path.join(__dirname + '/login.html'));
});

module.exports = router;