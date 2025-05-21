import os
import numpy as np
import pandas as pd


tracks = pd.read_csv('tracks.csv')
tracks = tracks.head(50)

tracks_df = pd.DataFrame(tracks)

tracks_df['duration_ms'] = tracks_df['duration_ms'].apply(lambda duration: duration/1000)

tracks_df = tracks_df.rename(columns = {'duration_ms':'duration_s'})

class getSong(): # cnn to rnn is hooked here.
    def __init__(self):
        super(getSong, self).__init__()
        
    def passs():

        return tracks_df

print(tracks_df.columns)
