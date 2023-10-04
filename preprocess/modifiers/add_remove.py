import config


def add(key, name, default):
    print('Starting to add new column in', key)

    data = config.curr_data

    data[name] = default

    config.set_data(key, data)

    print('New column addded')

    return {
        'status': True,
        'note': '',
        'data': data
    }


def remove(key, col_id):
    print('Starting to remove the column in', key)

    data = config.curr_data

    data = data.drop(data.columns[col_id], axis = 1)

    config.set_data(key, data)

    print('Dropped a column')

    return {
        'status': True,
        'note': '',
        'data': data
    }