import pandas as pd
from collections import defaultdict


def load_table(location, format):
    print(f'Opening file: {location}')

    file_name = location.split('/')[-1]
    data = {}

    with open(location, 'rb') as file:
        if format == 'csv':
            data[file_name] = pd.read_csv(file)
        elif format == 'xlsx':
            temp_data = pd.read_excel(file)
            data[file_name] = temp_data

    print(f'Data extracted successfully')
    return {
        'file_name': file_name,
        'data': data
    }