import subprocess

def adjust_time(x):

    try:

        sec = int(x.split(':')[1])
        min = int(x.split(':')[0])
    except:
        return x

    sec += 10

    if sec >= 60:

        sec -= 60
        min += 1
        sec = '0' + str(sec)

    val = str(min) + ':' + str(sec)
    val2 = str(min) + ':' + str(sec)

    if min == 0 and sec <= 20 and sec > 10:
        sec2 = 20
        val2 = str(min) + ':' + str(sec2)

    return val + '-' + val2

def naive_adjust_time(x):

    try:

        sec = int(x.split(':')[1])
        min = int(x.split(':')[0])
    except:
        return x
    
    sec2 = sec + 10
    min2 = min

    if sec2 >= 60:

        sec2 -= 60
        min2 = min2 +1
        sec2 = '0' + str(sec2)

    val = str(min) + ':' + str(sec)
    val2 = str(min2) + ':' + str(sec2)

    return val + '-' + val2


def prettify(df):
  
  df_test = df.copy()
  df_test['artist_link'] = df_test['artist_link'].apply(lambda x: 'https://www.whosampled.com' + x)
  df_test['ytube_link'] = df_test['ytube_link'].apply(lambda x: 'https://www.youtube.com/watch?v=' + x)
  return df_test



    #for i in range(len(df)):

        #if df['Success'][i] == 'success' and df['Amen_relation'] == True:

            #rand = random.randint(1, 5)
            #time.sleep(rand)

def downloader_drum_break(df,full_df,i,link_column_format,timestamp_column_format,direc_vid,direc_file):

    # df is original dataframe
    # full df is new dataframe
    # link format is the columns name for ytube_link - 'ytube_link_new'
    # direc_vid is the directory the videos go to - 'Projects\\Capstone\\Positive_songs\\'
    # direc_file is the directory the .txt file goes to (including the file name)

    link = 'https://www.youtube.com/watch?v=' + df[link_column_format][i]
    t = df[timestamp_column_format][i]
    #name = str(i)+ '--' + df['Page'][i].split('/')[-2][:-27]
    name = str(i)+ '--' + df['Page'][i].split('/')[-2]

    path = direc_vid + name

    t = '"*' + t + '"'

    command = 'yt-dlp -o ' + path + ' --download-sections ' + t + ' -x --audio-format wav ' + link

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        message = result.stderr
    else:
        message = 'Success'

    print(i, message)
    return list(df.loc[i]) + [result.returncode,name, message]
    
    
    

    
