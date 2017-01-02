from python_speech_features import mfcc

def calculate_accuracy(actual_ratings, predicted_ratings, threshold=0.1):
    correct_predictions = 0
    for i, predicted in enumerate(predicted_ratings):
        actual = actual_ratings[i]
        if (predicted <= (actual + threshold) and predicted >= (actual - threshold)):
            correct_predictions += 1
    accuracy = 100. * (correct_predictions)/len(predicted_ratings)
    return accuracy 
    
def mfc(amplitudes, sample_rate):
    mfcc_feat = mfcc(amplitudes, sample_rate)
    return mfcc_feat[0]