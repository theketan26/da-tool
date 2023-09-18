import os
import config


from load_save.load import load
from load_save.save import save


def main():
    location = os.path.join(config.base_path, 'data', 'iris.json')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'Bike_Features.csv')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'multi_json.json')
    report = load(location)

    # print('Loaded files:', config.file_name)
    # print('Loaded file data:', config.file_data)

    location = os.path.join(config.base_path, 'data')
    report_save = save(config.file_data['iris.json'], 'iris', location, 'csv')
    for key in report_save:
        print(key, ':', report_save[key])
    report_save = save(config.file_data['Bike_Features.csv'], 'bikes', location, 'json')
    for key in report_save:
        print(key, ':', report_save[key])
    report_save = save(config.file_data['multi_json.json'], 'multi_json', location, 'xlsx')
    for key in report_save:
        print(key, ':', report_save[key])


if __name__ == '__main__':
    print('Starting')
    main()
    print('Exit')