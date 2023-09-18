import os
import json


def save(data, file_name, location, format):
    print('Saving file:', file_name + '.' + format, '\nOn location:', location)
    report = {
        'status': False,
        'note': None
    }

    full_location = os.path.join(location, file_name + '.' + format)

    i = 1
    while os.path.exists(full_location):
        temp_file_name = f'{file_name}({i})'
        full_location = os.path.join(location, temp_file_name + '.' + format)
        i += 1

    try:
        if format == 'csv':
            data.to_csv(full_location)

        elif format == 'xlsx':
            data.to_excel(full_location)

        elif format == 'json':
            json_file = data.to_json(orient='records')
            json_file = json.loads(json_file)
            with open(full_location, 'w') as file:
                json.dump(json_file, file, ensure_ascii=False, indent=4)

    except Exception as err:
        report['note'] = str(err)
        return report

    report['status'] = True
    return report
