from preprocess.obj_to_df.obj_to_df_single import obj_to_df_single
from preprocess.obj_to_df.obj_to_df_multi import obj_to_df_multi


def obj_to_df(json_file):
    key_percentage = {
        "total": 0
    }
    for obj in json_file:
        key_percentage['total'] += 1
        for key in obj:
            if key in key_percentage:
                key_percentage[key] += 1
            else:
                key_percentage[key] = 1

    total = key_percentage.pop('total')
    for key in key_percentage:
        key_percentage[key] = key_percentage[key] / total

    can_single = any(map(lambda x: True if x == 1 else False, key_percentage.values()))
    can_multi = False
    for obj in json_file:
        if can_multi:
            break
        for key in obj:
            if type(obj[key]) == dict:
                can_multi = True
                break

    #
    #
    # Prompt for single or multi table option
    #
    #

    single_multi = True  # True if single else False

    if single_multi:
        if not can_multi:
            data = obj_to_df_single(json_file)
        else:
            data = obj_to_df_single(json_file, True)
    else:
        data = obj_to_df_multi(json_file)

    return data