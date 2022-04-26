import json


DIFF_MESSAGES = {
    'added': "Property '{path}' was added with value: {value}",
    'removed': "Property '{path}' was removed",
    'changed': "Property '{path}' was updated. From {old_value} to {new_value}"
}


def get_stringify_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return value


def get_path_string(previous_path, key):
    if previous_path:
        return previous_path + f'.{key}'
    return f'{key}'


def get_message_string(diff, previous_path):
    messages = []
    for key, value_types in diff.items():
        path = get_path_string(previous_path, key)
        type_ = value_types.get('type')
        value = value_types.get('value')
        if type_ == 'nested':
            messages.append(get_message_string(value, path))
        elif type_ == 'changed':
            old_value = get_stringify_value(value.get('old value'))
            new_value = get_stringify_value(value.get('new value'))
            message = DIFF_MESSAGES[type_].format(
                path=path,
                old_value=old_value,
                new_value=new_value
            )
            messages.append(message)
        elif type_ == 'added':
            value = get_stringify_value(value_types.get('value'))
            message = DIFF_MESSAGES[type_].format(path=path, value=value)
            messages.append(message)
        elif type_ == 'removed':
            message = DIFF_MESSAGES[type_].format(path=path)
            messages.append(message)
    return '\n'.join(messages)


def format_plain(diff):
    return get_message_string(diff, previous_path='')
