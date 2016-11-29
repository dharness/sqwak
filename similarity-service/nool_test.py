from pymongo import MongoClient
from process_audio import get_buffered_amplitudes


amps = get_buffered_amplitudes("./sqwaks/dool_shmaw/*.wav")

db = MongoClient()

for amp in amps:
    db.sqwaks.sounds.insert({
        "name": "dylan",
        "amplitudes": amp,
        "label": "shmaw"
    })