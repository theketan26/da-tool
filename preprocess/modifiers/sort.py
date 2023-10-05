import config


def sort(key, col, asc = True):
    print('Starting the sorting in', key)

    data = config.curr_data
    
    data = data.sort_values(by = data.columns[col],
                            ascending = asc)

    config.set_data(key, data)

    print('Sorting complete')

    return {
        'status': True,
        'note': '',
        'data': data
    }