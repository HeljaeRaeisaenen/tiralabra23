# Text generator
[![codecov](https://codecov.io/gh/HeljaeRaeisaenen/tiralabra23/branch/main/graph/badge.svg?token=FX8PJ7F1KE)](https://codecov.io/gh/HeljaeRaeisaenen/tiralabra23)

A Tiralabra 2023 project (_Mark of processer_)

## Weekly reports
[week 1](documentation/weekly_reports/week_report1.md)

[week 2](documentation/weekly_reports/week_report2.md)

[week 3](documentation/weekly_reports/week_report3.md)

[week 4](documentation/weekly_reports/week_report4.md)


## Documentation
[requiremens specification](documentation/requirements_specification.md)

[testing documentation](documentation/testing_document.md)

[executionn documentation](documentation/execution_document.md)


## Commands
#### First:
1. Copy the repository on your own machine
2. Go to the folder of the repository
3. Run `poetry install`

#### To run pylint: `poetry run invoke lint`

#### To run tests: `poetry run invoke test` 
Note: sometimes one test fails randomly. If you see a test fail, try running them again before concluding that the code is broken.

#### To to run the program:
1. Create a folder named `data` in the repository folder. It should be on the same level as `src`
2. Add a .txt file in the data folder. It should contain text. You can find free e-books in plain text from https://www.gutenberg.org and http://www.lonnrot.net (Finnish), for example.
3. Run `python3 src/index.py` in the repository's root folder (not in data!)
4. Give the name of the .txt file (not path!). For example, `example.txt`
