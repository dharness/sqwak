const Joi = require('joi');

const soundSchema = Joi.object().keys({
    label: Joi.string().required(),
    amplitudes: Joi.array().items(Joi.number().integer()).length(180224).required(),
    gender: Joi.any().valid('m', 'f', 'o'),
    batch_id: Joi.any()
})

module.exports = {soundSchema};