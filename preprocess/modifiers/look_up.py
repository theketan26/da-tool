import pandas as pd
import config


def look_up(key_a, key_b, col_a, col_b):
    print('Starting look up on', key_a, 'and', key_b)

    report = {
        'status': False,
        'note': '',
        'data': ''
    }

    data_a = config.get_data(key_a)
    data_b = config.get_data(key_b)

    try:
        data_m = pd.merge(data_a, data_b, left_on=data_a.columns[col_a], right_on=data_b.columns[col_b])
    except ValueError:
        report['note'] = 'Value not matching'
        return report

    report['status'] = True
    report['data'] = data_m
    config.set_data(key_a, data_m)

    print('Look up complete')

    return report
