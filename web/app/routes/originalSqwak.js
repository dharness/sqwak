var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('original-sqwak', { title: 'Nool Wuz here' });
});

module.exports = router;