def compare_data(data1, data2):
    diff = {}
    keys1, keys2 = data1.keys(), data2.keys()
    keys_union = sorted(keys1 | keys2)
    for key in keys_union:
        if key not in data1 and key in data2:
            diff.setdefault(f'+ {key}', data2[key])
        elif key in data1 and key not in data2:
            diff.setdefault(f'- {key}', data1[key])
        elif data1[key] == data2[key]:
            diff.setdefault(f'  {key}', data2[key])
        else:
            diff.setdefault(f'- {key}', data1[key])
            diff.setdefault(f'+ {key}', data2[key])
    return diff


def stringify_diff(diff):
    diff_list = ['{']
    for key, value in diff.items():
        if isinstance(value, bool):
            value = f'{value}'.lower()
            diff_list.append(f'  {key}: {value}')
        else:
            diff_list.append(f'  {key}: {value}')
    diff_list.append('}')
    result = '\n'.join(diff_list)
    return result
