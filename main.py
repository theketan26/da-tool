import os
import config


from load_save.load import load


def main():
    # location = os.path.join(config.base_path, 'data', 'Bike_Features.csv')
    location = os.path.join(config.base_path, 'data', 'iris.json')
    report = load(location)
    for key in report:
        print(key, ':', report[key])


if __name__ == '__main__':
    print('Starting')
    main()
    print('Exit')