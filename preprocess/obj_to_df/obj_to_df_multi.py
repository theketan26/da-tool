import pandas as pd


from preprocess.obj_to_df.obj_to_df_single import obj_to_df_single


def obj_to_df_multi(json_file):
    lst_lst = []
    new_json_file = []

    key_dict = ''
    for obj in json_file:
        for key in obj:
            if type(obj[key]) == dict:
                key_dict = key
                break

    curr_id = 0
    for obj in json_file:
        new_json = obj[key_dict]
        new_json['_id_'] = curr_id
        obj[key_dict] = curr_id
        new_json_file.append(new_json)
        curr_id += 1

    data = [
        obj_to_df_single(json_file),
        obj_to_df_single(new_json_file)
    ]

    return data
