import pandas as pd
from collections import defaultdict


def load_table(location, format):
    print(f'Opening file: {location}')
    data = defaultdict(lambda: None)

    with open(location, 'rb') as file:
        if format == 'csv':
            data[location.split('/')[-1]] = pd.read_csv(file)
        # elif format == 'xlsx':
        #     data['data'] = pd.read_excel(file)
            # for sheet in excel.sheet_names:
            #     data[sheet] = excel.parse(sheet)

    print(f'Data extracted successfully')
    return data