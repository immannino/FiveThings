var express = require('express');
var router = express.Router();
var path = require('path');


router.get('/', function(req, res) {
	res.sendFile(path.join(__dirname + '/index.html'));
});

router.get('/analyze', function(req, res) {
	res.sendFile(path.join(__dirname + '/analyze.html'));
});

router.get('/templates', function(req, res) {
	res.sendFile(path.join(__dirname + '/templates.html'));
});

module.exports = router;