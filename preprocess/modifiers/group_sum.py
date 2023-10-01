import config
from preprocess.modifiers.remove_duplicate import remove_duplicate


def group_sum(key, col_a, col_b, col_res_name):
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
    data = data.sort_values(by = str(data.columns[col_a]))
    data[col_res_name] = [''] * len(data.index)

    total = 0
    curr_head = ''
    for i, row in data.iterrows():
        if curr_head == '':
            curr_head = row.iloc[col_a]

        if row.iloc[col_a] == curr_head:
            try:
                total += float(row.iloc[col_b])
            except ValueError as err:
                report['note'] = 'All values in columns must be number'
                return report

        else:
            print()
            print()
            print(i, row.iloc[col_a], curr_head, row.iloc[col_a] == curr_head)
            print()
            print()

            sums[curr_head] = total
            data.iloc[i - 1, -1] = total
            total = 0
            curr_head = row.iloc[col_a]
            try:
                total = float(row.iloc[col_b])
            except ValueError as err:
                report['note'] = 'All values in columns must be number'
                return report

    data.iloc[-1, -1] = total
    sums[curr_head] = total

    report['status'] = True
    report['data'] = data
    report['sums'] = sums

    # config.file_data[key] = data
    config.set_data(key, data)
    print()
    print()
    print(sums)
    print()
    print()

    # data_trimmed = remove_duplicate(key, col_a)
    # config.set_data(key, data_trimmed['data'])

    print('Group summing complete')

    return report
