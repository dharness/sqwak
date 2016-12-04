from pymongo import MongoClient
from process_audio import get_buffered_amplitudes
import matplotlib.pyplot as plt

# amps = get_buffered_amplitudes("./output.wav")
# plt.figure(1)
# plt.plot(amps[0])
# plt.show()

db = MongoClient()

result = db.sqwaks.sounds.find()
db_amps = result[0]["amplitudes"]
plt.figure(2)
plt.plot(db_amps)
plt.show()