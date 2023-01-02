from python_speech_features import mfcc
import librosa
import os
import pickle

def load_train_data(folder_address):
    x, y = [], []
    for folder in os.listdir(folder_address):
        print(folder)
        genre_folder = folder_address + '/' + folder
        for music in os.listdir(genre_folder):
            if not music.endswith('.mp3'):
                continue
            print(genre_folder + '/' + music)
            sig, rate = librosa.load(genre_folder + '/' + music)
            music_mfcc = mfcc(sig, rate, winlen = 0.020, appendEnergy=False)
            avg_mfcc = [0 for i in range(13)]
            num = 0
            for single_mfcc in music_mfcc:
                avg_mfcc += single_mfcc
                num += 1
            avg_mfcc /= num
            x.append(avg_mfcc)
            y.append(folder)
    return x, y

if __name__ ==  "__main__":
    folder_address = "./music"
    x, y = load_train_data(folder_address)
    with open("mfcc.data", 'wb') as file:
        pickle.dump((x, y), file)