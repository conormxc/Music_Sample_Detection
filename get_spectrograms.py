
import librosa
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import pickle

from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('Projects\Capstone\Song_files\Complete_df.txt')

def create_spectrogram(filename,n_fft,window_length, hop_length):
  
  y,sr = librosa.load(filename)
  if sr != 22050:
     y = librosa.resample(y, orig_sr=sr, target_sr=22050)
  #D = librosa.amplitude_to_db(abs(librosa.stft(y,hop_length = int(hop_length),win_length = window_length, n_fft=n_fft)))
  M = librosa.feature.melspectrogram(y=y,hop_length = int(hop_length), win_length = window_length,n_fft=n_fft)
  M_db = librosa.power_to_db(M)
  if M_db.shape[1] < 861:
    return 0
  M_db = minmax_scale(M_db[:,-861:])
  return M_db

def minmax_scale(input_array):
   
    scaler = MinMaxScaler()

    # Flatten the input array and then reshape it back to its original shape after scaling
    flattened_array = input_array.reshape(-1, 1)
    scaled_array = scaler.fit_transform(flattened_array).reshape(input_array.shape)

    return scaled_array

n_fft=1024
window_length = n_fft
hop_length = n_fft/4

s = len(df)
lst = [0]*s

for i in range(s):
    filename = df['Directory'][i] + '\\' + df['filename'][i].split('/')[-1]
    spec = create_spectrogram(filename,n_fft,window_length, hop_length)
    lst[i] = spec
    if i%100 == 0:
       print(i)
    if not isinstance(spec,np.ndarray):
       print(i,'fail',filename,spec)

with open('Spectrograms_low.pickle', 'wb') as handle:
    pickle.dump(lst, handle)

