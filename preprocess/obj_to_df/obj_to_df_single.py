import pandas as pd


def obj_to_df_single(json_file):
    lst_lst = []

    headers = {
        'all_headers': set(),
    }

    current_col = 0
    for obj in json_file:
        for key in obj:
            if key not in headers['all_headers']:
                headers['all_headers'].add(key)
                headers[key] = current_col
                current_col += 1

    for obj in json_file:
        lst = [''] * len(headers['all_headers'])
        for header in headers['all_headers']:
            if header in obj:
                lst[headers[header]] = obj[header]
            else:
                lst[headers[header]] = None
        lst_lst.append(lst)

    heads = [''] * len(headers['all_headers'])
    for header in headers['all_headers']:
        heads[headers[header]] = header

    data = pd.DataFrame(lst_lst, columns=heads)

    return data