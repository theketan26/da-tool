import os
import config


from load_save.load import load
from load_save.save import save
from preprocess.modifiers.remove_duplicate import remove_duplicate
from preprocess.modifiers.group_sum import group_sum
from preprocess.modifiers.group_combine import group_combine
from preprocess.modifiers.seperate import seperate
from preprocess.modifiers.look_up import look_up


def main():
    location = os.path.join(config.base_path, 'data', 'iris.json')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'Bike_Features.csv')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'master_indore_village_code.xlsx')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'master_indore_village_name.xlsx')
    report = load(location)
    # location = os.path.join(config.base_path, 'data', 'iris_combine.json')
    # report = load(location)

    # report_rem_dup = remove_duplicate('iris.json', [1, 4])
    # report_rem_dup = remove_duplicate('iris.json', 4)
    # report_rem_dup = remove_duplicate('Bike_Features.csv')
    # print('duplicates:', report_rem_dup['duplicate'])
    # report_group_sum = group_sum('iris.json', 4, 1, 'total')
    # report_group_combine = group_combine('iris.json', 4, ',')
    # report_group_combine = group_combine('Bike_Features.csv', 21, ',')
    # report_sep = seperate('iris_combine.json', ',')
    # location = os.path.join(config.base_path, 'data')
    # save(report_sep['data'], 'iris_sep.json', location, 'json')
    # print(config.get_data('iris_combine.json'))
    # save(config.get_data('iris.json'), 'iris_combine', location, 'json')
    # print(report_group_sum['sums'])
    look_up('master_indore_village_code.xlsx', 'master_indore_village_name.xlsx', 3, 1)
    print(config.get_data('master_indore_village_code.xlsx'))
    # print(config.get_data('master_indore_village_name.xlsx'))


if __name__ == '__main__':
    print('Starting')
    main()
    print('Exit')