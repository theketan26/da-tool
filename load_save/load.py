import os


from load_save.load_table import load_table
from load_save.load_object import load_object


def load(location):
    report = {
        'status': False,
        'note': None,
        'format': None,
        'data': None
    }

    if not os.path.exists(location):
        report['note'] = f'File not exist!\nCheck for the file on location: {location}'
        return report

    report['format'] = location.split('.')[-1]

    if report['format'] in ['csv', 'xlsx']:
        report['data'] = load_table(location, report['format'])
    elif report['format'] in ['json']:
        report['data'] = load_object(location)

    return report