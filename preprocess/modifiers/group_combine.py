import config
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


from preprocess.modifiers.remove_duplicate import remove_duplicate


def group_combine(key, col_a, combiner):
    print('Starting group combining in', key)

    data = config.get_data(key)
    cols = list(data.columns)
    col_a = cols[col_a]
    data.sort_values(col_a)

    curr_val = ''
    curr_row = 0
    for i, row in data.iterrows():
        if curr_val == '':
            curr_val = row[col_a]

        elif row[col_a] == curr_val:
            for col in cols:
                if col == col_a:
                    continue

                else:
                    data._set_value(curr_row, col, str(data[col][curr_row]) + combiner + str(row[col]))
                    # try:
                    #     new_row_data[col] += str(new_row_data[col]) + combiner + str(row[col])
                    # except TypeError:
                    #     new_row_data[col] = str(new_row_data[col]) + combiner + str(row[col])

        else:
            curr_val = row[col_a]
            # new_data.loc[len(new_data)] = new_row_data
            curr_row = i

    config.set_data(key, data)
    report = remove_duplicate(key, cols.index(col_a))
    config.set_data(key, report['data'])

    print('Group combining completed')