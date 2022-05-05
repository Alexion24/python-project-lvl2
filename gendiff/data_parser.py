import json
import yaml


def parse(data, format_):
    if format_ == 'json':
        return json.loads(data)
    if format_ == 'yaml':
        return yaml.safe_load(data)
    raise Exception('Wrong file format. Available formats: yaml, yml or json')
