import sklearn
from sklearn.neighbors import KNeighborsClassifier
from python_speech_features import mfcc
import librosa
import pickle

def predict(Knn_classifier, music_address):
    sig, rate = librosa.load(music_address)
    music_mfcc = mfcc(sig, rate, winlen = 0.020, appendEnergy=False)
    #print(music_mfcc)
    results = Knn_classifier.predict(music_mfcc)
    results_dict = dict()
    for single_result in results:
        if single_result not in results_dict:
            results_dict[single_result] = 1
        else:
            results_dict[single_result] += 1
    return results_dict

if __name__ == "__main__":
    with open("mfcc.data", 'rb') as file:
        x, y = pickle.load(file)
    knn = KNeighborsClassifier()
    knn.fit(x, y)
    result = predict(knn, "./music/鄉村/123.mp3")
    print(result)

    
