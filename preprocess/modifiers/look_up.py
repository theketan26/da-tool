import pandas as pd
import config


def look_up(key_a, key_b, col_a, col_b, a_cols=[], b_cols=[]):
    print('Starting look up on', key_a, 'and', key_b)

    report = {
        'status': False,
        'note': '',
        'data': ''
    }

    data_a = config.get_data(key_a)
    col_a = data_a.columns[col_a]
    if a_cols != []:
        data_a = data_a.iloc[:, a_cols]
    data_b = config.get_data(key_b)
    col_b = data_b.columns[col_b]
    if b_cols != []:
        data_b = data_b.iloc[:, b_cols]

    try:
        data_m = pd.merge(data_a, data_b, left_on=col_a, right_on=col_b)
    except ValueError:
        report['note'] = 'Value not matching'
        return report

    report['status'] = True
    report['data'] = data_m
    config.set_data(key_a, data_m)

    print('Look up complete')

    return report
