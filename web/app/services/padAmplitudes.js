module.exports = function padAmplitudes(amplitudes, options) {
    options.frequency = options.frequency || 44100;
    options.sampleLength = options.sampleLength || 3.5;

    const idealLength = options.frequency * options.sampleLength;
    const diff = idealLength - amplitudes.length;
    if (diff < 0) {
        // slice off the extra amplitudes
        amplitudes =  amplitudes.slice(0, idealLength);
    } else if (diff > 0) {
        let padding = new Array(diff);
        padding.fill(0);
        amplitudes = [...amplitudes, ...padding];
    }
    
    return amplitudes
}
