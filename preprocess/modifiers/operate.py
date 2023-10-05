import config


def add(data, a, b, b_col):
    for i, row in data.iterrows():
        if b_col:
            b = int(b)
            try:
                a_ = float(row[a])
                b_ = float(row[b])
                data.iloc[i, a] = a_ + b_

            except:
                data.iloc[i, a] = str(row[a]) + str(row[b])

        else:
            try:
                a_ = float(row[a])
                b_ = float(b)
                data.iloc[i, a] = a_ + b_

            except:
                data.iloc[i, a] = str(row[a]) + str(b)


def compare(data, a, b, b_col, op):
    if b_col:
        b = int(b)
    data['Compare'] = None
    for i, row in data.iterrows():
        if b_col:
            if op == '=':
                data['Compare'] = row[a] == row[b]
            elif op == '<':
                data['Compare'] = row[a] < row[b]
            elif op == '>':
                data['Compare'] = row[a] > row[b]
        else:
            if op == '=':
                data['Compare'] = row[a] == b
            elif op == '<':
                data['Compare'] = row[a] < b
            elif op == '>':
                data['Compare'] = row[a] > b


def operate(key, a, b, b_col, op):
    print('Starting operation on ', key)

    data = config.curr_data

    if op == 'Add/Concat':
        add(data, a, b, b_col)

    elif op == 'Compare(=)':
        compare(data, a, b, b_col, '=')

    elif op == 'Compare(<)':
        compare(data, a, b, b_col, '<')

    elif op == 'Compare(>)':
        compare(data, a, b, b_col, '>')

    config.set_data(key, data)

    print('Operation completed')

    return {
        'status': True,
        'note': '',
        'data': data
    }
