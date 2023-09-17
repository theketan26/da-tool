import os
import config


from load_save.load import load


def main():
    location = os.path.join(config.base_path, 'data', 'iris.json')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'Bike_Features.csv')
    report = load(location)
    location = os.path.join(config.base_path, 'data', 'multi_json.json')
    report = load(location)

    # for key in report:
    #     print(key, ':', report[key])

    print('Loaded files:', config.file_name)
    print('Loaded file data:', config.file_data)


if __name__ == '__main__':
    print('Starting')
    main()
    print('Exit')