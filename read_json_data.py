import pandas as pd
import json

def open_json_data():
    data = []
    relative_path = 'spotify_million_playlist_dataset/data/mpd.slice.'
    
    # Using all the data even makes this extremely slow...
    for i in range(1):
        which_data_file = str(1000 * i) + '-' + str(1000 * (i+1) - 1) + '.json'
        full_path = relative_path + which_data_file
        with open(full_path) as data_file:
            curr_data = json.load(data_file)
            for playlists in curr_data['playlists']:
                data.append(playlists)
    
    print("finished")
    return data

def json_to_dataframe(data):
    result = pd.json_normalize(data, 'tracks', ['name'])
    return result

    