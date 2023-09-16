import os
import config


from load_save.load import load


def main():
    location = os.path.join(config.base_path, 'data', 'Bike_Features.csv')
    # location = os.path.join(config.base_path, 'data', 'master_indore.xlsx')
    report = load(location)
    print(report)


if __name__ == '__main__':
    print('Starting')
    main()
    print('Exit')