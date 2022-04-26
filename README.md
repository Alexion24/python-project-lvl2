## Hexlet tests and linter status:
[![Actions Status](https://github.com/Alexion24/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Alexion24/python-project-lvl2/actions)
[![hexlet-test-and-lint](https://github.com/Alexion24/python-project-lvl2/actions/workflows/test-and-lint.yml/badge.svg)](https://github.com/Alexion24/python-project-lvl2/actions/workflows/test-and-lint.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e6ab91d73f7afd276c68/maintainability)](https://codeclimate.com/github/Alexion24/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e6ab91d73f7afd276c68/test_coverage)](https://codeclimate.com/github/Alexion24/python-project-lvl2/test_coverage)
## Project description:
Проект представляет собой консольную утилиту сравнивающую между собой содерджимое файлов с такими форматами как JSON и YAML с реализованной возможностью использования себя как библиотеки.

Доступные форматы сравнения:
1) stylish
2) plain
3) json

Для работы с проектом как библиотекой, вам понадобится выполнить команду:

`pip install git+https://github.com/Alexion24/python-project-lvl2.git`

Реализация:

`gendiff -h`

`gendiff --format filepath1 filepath2`



## Demonstration:
#### Compare two flat JSON files with stylish format.
[![asciicast](https://asciinema.org/a/VJZ7jGviGmY46OPYMnyhpMBov.svg)](https://asciinema.org/a/VJZ7jGviGmY46OPYMnyhpMBov)

#### Compare two flat YAML files with stylish format.
[![asciicast](https://asciinema.org/a/r311HMrFERp5VxUFgTFTQZ3jg.svg)](https://asciinema.org/a/r311HMrFERp5VxUFgTFTQZ3jg)
#### Compare two nested JSON and YAML files with stylish format.
[![asciicast](https://asciinema.org/a/RKgOL0CALBlaiXRNhsPHQLE7g.svg)](https://asciinema.org/a/RKgOL0CALBlaiXRNhsPHQLE7g)
#### Compare two flat and nested JSON and YAML files with plain format.
[![asciicast](https://asciinema.org/a/cyP78bKIKgfVsTfSqaPpgF0Hg.svg)](https://asciinema.org/a/cyP78bKIKgfVsTfSqaPpgF0Hg)
#### Compare two flat and nested JSON and YAML files with json format.
[![asciicast](https://asciinema.org/a/tA1ti0wsFRPCv3gu5ozmztvBu.svg)](https://asciinema.org/a/tA1ti0wsFRPCv3gu5ozmztvBu)