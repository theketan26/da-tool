import os
import config
import json


from preprocess.obj_to_df.obj_to_df import obj_to_df


def load_object(location):
    can_single = False
    can_multi = False

    print(f'Opening file: {location}')

    file_name = location.split('/')[-1]

    with open(location) as file:
        json_file = json.load(file)

    data = obj_to_df(json_file)

    report = {}

    print(f'Data extracted successfully')

    return {
        'file_name': file_name,
        'data': data
    }