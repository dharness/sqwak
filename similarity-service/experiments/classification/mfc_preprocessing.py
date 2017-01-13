# from essentia.standard import *
from pymongo import MongoClient
# import utils
import numpy as np
import pandas as pd
import librosa
import os
import scipy.io.wavfile
import scipy.stats
from math import floor


def main():
    db = MongoClient()
    classID = 3
    results = db.urban_sound.audio.find({"classID": classID})

    for i, original in enumerate(results):
        slice_file_name = original["slice_file_name"]
        dir = os.path.dirname(__file__)
        wav_path = os.path.join(dir, 'UrbanSound8K', 'formatted_audio', slice_file_name)
        sample_rate, amps = scipy.io.wavfile.read(wav_path)
        if amps.ndim is 2:
            amps = amps[:,0]
        else:
            amps = amps[0:]

        window_size_ms = 23.2
        n_fft = int(floor((sample_rate * window_size_ms)/500.) * 2)
        # 50% frame overlap
        hop_length = n_fft/2
        mfcc_mat = librosa.feature.mfcc(y=amps, sr=sample_rate, n_fft=n_fft, hop_length=hop_length, n_mfcc=40)

        metric_min = np.min( mfcc_mat[0:25,:], axis=1)
        metric_max = np.max( mfcc_mat[0:25,:], axis=1)
        metric_median = np.median( mfcc_mat[0:25,:], axis=1)
        metric_mean = np.mean( mfcc_mat[0:25,:], axis=1)
        metric_variance = np.var( mfcc_mat[0:25,:], axis=1)
        metric_skewness = scipy.stats.skew( mfcc_mat[0:25,:], axis=1)
        metric_kurtosis = scipy.stats.kurtosis( mfcc_mat[0:25,:], axis=1)
        # delta
        mfcc_delta = librosa.feature.delta( mfcc_mat[0:25,:], axis=1)
        metric_mean_delta = np.mean(mfcc_delta[0:25,:], axis=1)
        metric_variance_delta = np.var(mfcc_delta[0:25,:], axis=1)
        # delta-delta
        mfcc_delta_2 = librosa.feature.delta( mfcc_mat[0:25,:], axis=1, order=2)
        metric_mean_delta_2 = np.mean(mfcc_delta_2[0:25,:], axis=1)
        metric_variance_delta_2 = np.var(mfcc_delta_2[0:25,:], axis=1)
        

        feature_vector = np.hstack((
            metric_min,              # 1
            metric_max,              # 2
            metric_median,           # 3
            metric_mean,             # 4
            metric_variance,         # 5
            metric_skewness,         # 6
            metric_kurtosis,         # 7
            metric_mean_delta,       # 8
            metric_variance_delta,   # 9
            metric_mean_delta_2,     # 10
            metric_variance_delta_2  # 11
        ))

        # print(len(feature_vector))

        del original["amplitudes"]
        del original["_id"]
        original["features"] = feature_vector.tolist()
        db.urban_sound.mfc_librosa_2.insert(original)
        print("Inserted " + str(i))

        # w = Windowing(type = 'hann')
        # spectrum = Spectrum()

        # mfcc = MFCC(
        #     numberCoefficients=40, 
        #     lowFrequencyBound=0,
        #     highFrequencyBound=22050,
        #     sampleRate=sample_rate
        # )

        # if amps.ndim is 2:
        #     amps_single = amps[:,0]
        # else:
        #     amps_single = amps[0:]

        # bands, coefs = mfcc(amps_single)
        # del original["amplitudes"]
        # del original["_id"]
        # original["features"] = coefs.tolist()
        # db.urban_sound.mfc_audio_2.insert(original)
        # print "Inserted "

def extract_feature(file_name):
    X, sample_rate = librosa.load(file_name)
    stft = np.abs(librosa.stft(X))
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
    mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
    return mfccs, chroma, mel, contrast, tonnetz

if __name__ == "__main__":
    main()
