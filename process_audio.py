import scipy.io.wavfile
import glob
import sys
from tempfile import TemporaryFile

def get_amplitudes(path):
    result = scipy.io.wavfile.read(path)
    amplitudes = result[1]
    norm_amplitudes = []
    for a in amplitudes:
        norm_amplitudes.append(a.tolist()[0])
    return norm_amplitudes

# Reads all the sounds in the provided path, and returns a tuple of aplitudes
# and the longest sound in the batch
def read_sounds(path):
    max_length = 0
    amplitudes = []
    for filename in glob.glob(path):
        sys.stdout.write(filename + '\r')
        sys.stdout.flush()

        current_amplitudes = get_amplitudes(filename)
        amplitudes.append(current_amplitudes)
        if (len(current_amplitudes) > max_length):
            max_length = len(current_amplitudes)
    return (amplitudes, max_length)

# Pad the provided array with 0s until it is the ne size
def add_buffer(amplitudes, new_size):
    new_amplitudes = []
    for a in amplitudes:
        buffer_length = new_size - len(a)
        buffer_array = [0] * buffer_length
        temp_a = a + buffer_array
        new_amplitudes.append(temp_a)
    return new_amplitudes


def get_buffered_amplitudes(path):
  (amplitudes, max_length) = read_sounds(path)
  buffered_amplitudes = add_buffer(amplitudes, max_length)

  return buffered_amplitudes
