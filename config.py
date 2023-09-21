import os
import pandas as pd


base_path = os.path.abspath('')

file_loaded = 0
file_name = []
file_data = {}


def get_data(key):
    location = os.path.join(base_path, 'data', 'pickle', key + '.pkl')
    return pd.read_pickle(location)


def set_data(key, data):
    location = os.path.join(base_path, 'data', 'pickle', key + '.pkl')
    data.to_pickle(location)