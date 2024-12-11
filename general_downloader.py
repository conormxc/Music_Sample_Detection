import subprocess
import pandas as pd
import numpy as np
import time
import random

from functs import adjust_time, naive_adjust_time, downloader_drum_break

file_name = 'Songs_general.txt'
time_column = 'timestamp_new'
timestamp_column_format = 'converted_timestamp_new'
link_column_format = 'ytube_link_new'
direc_vid = 'Projects\\Capstone\\Song_files\\Songs_general_3000\\'
direc_file = 'Projects\\Capstone\\Song_files\\Songs_general_info.txt'

df = pd.read_csv('Projects\\Info_folder\\' + file_name)
df[timestamp_column_format] = df[time_column].apply(naive_adjust_time)
df = df[df[link_column_format].notna()].reset_index().iloc[:,1:]


full_df = pd.DataFrame(columns = (list(df.columns) + ['returncode_new','filename_new','message_new']))

for i in range(len(df)):

    if not(df['Amen_relation'][i]):

        output = downloader_drum_break(df,full_df,i,link_column_format,timestamp_column_format,direc_vid,direc_file)
        full_df.loc[i] = output

    if i%50 == 0:
        full_df.to_csv(direc_file, index = False)

full_df.to_csv(direc_file, index = False)