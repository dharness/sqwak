const express = require('express');
const Joi = require('joi');
const soundSchema = require('../services/validations').soundSchema;
const padAmplitudes = require('../services/padAmplitudes');
const router = express.Router();
const conn = require('../dbConnection');

/* GET users listing. */
router.get('/', function(req, res, next) {
  conn.db.collection('sounds').find({}, {amplitudes:0}).toArray((err, sounds) => {
    if (err) return res.send(err);
    res.send(sounds);
  });
});

router.post('/', function(req, res, next) {
  const data = req.body ? req.body.data : {}
  const sampleLength = 3.5;
  const frequency = 44100;
  
  data.amplitudes = padAmplitudes(data.amplitudes, { frequency, sampleLength });

  Joi.validate(data, soundSchema, (err, sound) => {
    console.log(err);
    if (err != null) return res.status(400).send(err);
    
    conn.db.collection('sounds').insertOne(sound, (err, ok) => {
      if (err != null) return res.send(err);
      res.status(200).send(ok);
    })
  });
});

module.exports = router;
