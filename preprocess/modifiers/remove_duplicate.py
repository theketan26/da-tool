import config


def remove_duplicate_table(data, column):
    rows = set()
    to_remove = []

    for i, row in data.iterrows():
        s = ''
        if type(column) == list:
            for col in column:
                s += str(row.iloc[col]).strip(' ').lower()

        elif column == -1:
            for tup in row:
                s += str(tup).strip(' ').lower()

        else:
            s = str(row.iloc[column]).strip(' ').lower()

        if s in rows:
            to_remove.append(i)
        else:
            rows.add(s)

    data.drop(to_remove, inplace=True)

    return {
        'data': data,
        'duplicate': len(to_remove)
    }


def remove_duplicate(key, column=-1):
    print('Starting to remove duplicates from', key)

    data = config.file_data[key]
    report_rem_dup = remove_duplicate_table(data, column)

    if report_rem_dup['duplicate'] > 0:
        config.file_data[key] = report_rem_dup['data']

    print('Duplicates removed! Found', report_rem_dup['duplicate'])

    return report_rem_dup