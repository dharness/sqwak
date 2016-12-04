var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.redirect('/labs/play');
});

router.get('/play', function(req, res, next) {
  res.render('labs/play');
});

router.get('/record', function(req, res, next) {
  res.render('labs/record');
});

module.exports = router;
