import os
import pandas as pd


base_path = os.path.abspath('')
root = None

file_loaded = 0
file_name = []


def get_data(key):
    location = os.path.join(base_path, 'data', 'pickle', key + '.pkl')
    return pd.read_pickle(location)


def set_data(key, data):
    location = os.path.join(base_path, 'data', 'pickle', key + '.pkl')
    data.to_pickle(location)


processes = ['column', 'combine', 'sum', 'merge', 'remove duplicate']
visuals = ['Line Plot', 'Bar Plot', 'Histogram Plot', 'Scatter Plot']
column_process = ['Add', 'Remove', 'Operate', 'Sort', 'Filter']
operators = ['Add/Concat', 'Compare(=)', 'Compare(>)', 'Compare(<)']

curr_table = None
curr_data = None
table_frame = None
gui_table = None
table_lbl = None
