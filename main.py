import os
import config


from load_save.load import load
from load_save.save import save
from preprocess.modifiers.remove_duplicate import remove_duplicate
from preprocess.modifiers.group_sum import group_sum


def main():
    location = os.path.join(config.base_path, 'data', 'iris.json')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'Bike_Features.csv')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'multi_json.json')
    report = load(location)

    # report_rem_dup = remove_duplicate('iris.json', [1, 4])
    # report_rem_dup = remove_duplicate('iris.json', 4)
    # report_rem_dup = remove_duplicate('Bike_Features.csv')
    report_group_sum = group_sum('iris.json', 4, 1, 'total')
    print(config.file_data['iris.json'])
    print(report_group_sum['sums'])
    # print('duplicates:', report_rem_dup['duplicate'])


if __name__ == '__main__':
    print('Starting')
    main()
    print('Exit')