const Joi = require('joi');

const soundSchema = Joi.object().keys({
    label: Joi.string().required(),
    amplitudes: Joi.array().items(Joi.number()).required(),
    gender: Joi.any().valid('m', 'f', 'o', 'M', 'F', 'O'),
    batch_id: Joi.any()
})

module.exports = {soundSchema};
