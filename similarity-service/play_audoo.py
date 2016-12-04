import numpy as np
from pymongo import MongoClient
from scipy.io.wavfile import write

db = MongoClient()

result = db.sqwaks.sounds.find()
db_amps = result[0]["amplitudes"]

data = np.random.uniform(-1, 1, 44100) # 44100 random samples between -1 and 1
scaled = np.int16(db_amps/np.max(np.abs(db_amps)) * 32767)
write('test.wav', 44100, scaled)