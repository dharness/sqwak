def calculate_accuracy(actual_ratings, predicted_ratings, threshold=0.1):
    correct_predictions = []
    for i, predicted in enumerate(predicted_ratings):
        actual = actual_ratings[i]
        if (predicted <= (actual + threshold) and predicted >= (actual - threshold)):
            correct_predictions.append(True)
    accuracy = 100. * (len(correct_predictions))/len(predicted_ratings)
    return accuracy 