import pandas as pd


import config


def seperate_column(data, seperator, col):
    new_data = []

    for row_i, row in data.iterrows():
        new_col_list = row[col].split(seperator)
        new_row_data = list(row)
        for new_col_item in new_col_list:
            new_row_data[col] = new_col_item
            new_data.append(new_row_data)

    return new_data


def seperate(key, seperator, column=-1):
    print('Starting to seperate: ', key)

    data = config.get_data(key)
    new_data = []

    if column == -1:
        for col in range(len(data.columns)):
            if column == col:
                continue
            new_data.append(seperate_column(data, seperator, col))

    new_data = pd.DataFrame(new_data)
    new_data = new_data.T
    new_data.columns = data.columns

    config.set_data(key, new_data)

    print(new_data)

    print('Seperation complete')
    return {
        'status': True,
        'data': new_data
    }