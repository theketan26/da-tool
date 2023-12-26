import config
from preprocess.modifiers.remove_duplicate import remove_duplicate


def group_sum(key, col_a, col_b):
    print('Starting group sum in', key)

    report = {
        'status': False,
        'note': None,
        'data': None,
        'sums': None
    }
    sums = {}

    # data = config.file_data[key]
    data = config.get_data(key)

    grouped_sum = data.groupby(col_a)[col_b].sum().reset_index()

    report['status'] = True
    report['data'] = grouped_sum

    # config.file_data[key] = data
    config.set_data(key, grouped_sum)

    # data_trimmed = remove_duplicate(key, col_a)
    # config.set_data(key, data_trimmed['data'])

    print('Group summing complete')

    return report
