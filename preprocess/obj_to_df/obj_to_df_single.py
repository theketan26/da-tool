import pandas as pd


def obj_to_df_single(json_file, can_multi=False):
    lst_lst = []

    to_remove = ''
    if can_multi:
        for obj in json_file:
            temp = {}

            for header in obj:
                if type(obj[header]) == dict:
                    if to_remove == '':
                        to_remove = (header)
                    for header_header in obj[header]:
                        temp_value = obj[header][header_header]
                        temp[str(header) + '|' + str(header_header)] = temp_value

            obj.update(temp)

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

    if can_multi:
        data.drop(to_remove, axis=1, inplace=True)

    return data
