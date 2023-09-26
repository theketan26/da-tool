import os
import config


from load_save.load import load
from load_save.save import save
from preprocess.modifiers.remove_duplicate import remove_duplicate
from preprocess.modifiers.group_sum import group_sum
from preprocess.modifiers.group_combine import group_combine
from preprocess.modifiers.seperate import seperate
from preprocess.modifiers.look_up import look_up


from gui.gui import show_gui


def main():
    # location = os.path.join(config.base_path, 'data', 'iris.json')
    # report = load(location)
    # location = os.path.join(config.base_path, 'data', 'Bike_Features.csv')
    # report = load(location)

    show_gui()


if __name__ == '__main__':
    print('Starting')
    main()
    print('Exit')