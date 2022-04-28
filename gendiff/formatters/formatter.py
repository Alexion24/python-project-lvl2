from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.formatters.formats import STYLISH, PLAIN, JSON


def format_diff(diff, formatter):
    if formatter == STYLISH:
        return format_stylish(diff)
    if formatter == PLAIN:
        return format_plain(diff)
    if formatter == JSON:
        return format_json(diff)
    raise Exception(
        'Wrong formatter. Available formatters: stylish, plain or json'
    )
