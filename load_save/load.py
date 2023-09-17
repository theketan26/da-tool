import os
import config


from load_save.load_table import load_table
from load_save.load_object import load_object


def load(location):
    report = {
        'status': False,
        'note': None,
        'format': None,
        'file_name': None,
        'data': None
    }

    if not os.path.exists(location):
        report['note'] = f'File not exist!\nCheck for the file on location: {location}'
        return report

    report['format'] = location.split('.')[-1]

    if report['format'] in ['csv', 'xlsx']:
        report_load = load_table(location, report['format'])

    elif report['format'] in ['json']:
        report_load = load_object(location)

    else:
        report['note'] = 'File formate not supported!\nSupported formats: CSV, Excel and JSON'
        return report

    config.file_loaded += 1
    config.file_name.append(report_load['file_name'])
    config.file_data[report_load['file_name']] = report_load['data']

    report['status'] = True
    report['file_name'] = report_load['file_name']
    report['data'] = report_load['data']

    return report