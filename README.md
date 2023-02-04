# Text generator
[![codecov](https://codecov.io/gh/HeljaeRaeisaenen/tiralabra23/branch/main/graph/badge.svg?token=FX8PJ7F1KE)](https://codecov.io/gh/HeljaeRaeisaenen/tiralabra23)

A Tiralabra 2023 project (_Mark of processer_)

## Weekly reports
[week 1](documentation/weekly_reports/week_report1.md)

[week 2](documentation/weekly_reports/week_report2.md)

[week 3](documentation/weekly_reports/week_report3.md)


## Requirements specification
[link](documentation/requirements_specification.md)

## Commands
#### First:
1. Copy the repository on your own machine
2. Go to the folder of the repository
3. Run `poetry install`

#### To run pylint: `poetry run invoke lint`

#### To run tests: `poetry run invoke test` 

#### To to run the program:
1. Create a folder named `data` in the repository folder. It should be on the same level as `src`
2. Add a .txt file in the data folder. It should contain text.
3. Run `python3 src/index.py` in the repository's root folder (not in data!)
4. Give the name of the .txt file (not path!). For example, `example.txt`
5. If this doesn't work then I made a mistake, sorry.
