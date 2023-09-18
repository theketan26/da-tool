import config


def group_sum(key, col_a, col_b, col_res_name):
    print('Starting group sum in', key)

    report = {
        'status': False,
        'note': None,
        'data': None,
        'sums': None
    }
    sums = {}

    data = config.file_data[key]
    data.sort_values(data.columns[col_a])
    data[col_res_name] = [''] * len(data.index)

    total = 0
    curr_head = ''
    for i, row in data.iterrows():
        if curr_head == '':
            curr_head = row.iloc[col_a]

        if row.iloc[col_a] == curr_head:
            total += float(row.iloc[col_b])

        else:
            sums[curr_head] = total
            data.iloc[i - 1, -1] = total
            try:
                total = float(row.iloc[col_b])
            except ValueError as err:
                report['note'] = 'All values in columns must be number'
                return report
            curr_head = ''

    data.iloc[-1, -1] = total
    sums[curr_head] = total

    report['status'] = True
    report['data'] = data
    report['sums'] = sums

    config.file_data[key] = data

    print('Group summing complete')

    return report
