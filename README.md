# Text generator
[![codecov](https://codecov.io/gh/HeljaeRaeisaenen/tiralabra23/branch/main/graph/badge.svg?token=FX8PJ7F1KE)](https://codecov.io/gh/HeljaeRaeisaenen/tiralabra23)

A Tiralabra 2023 project (_Mark of processer_)

## Weekly reports
[week 1](documentation/weekly_reports/week_report1.md)

[week 2](documentation/weekly_reports/week_report2.md)

## Requirements specification
[link](documentation/requirements_specification.md)

## How to run the program
1. Copy the repository on your own machine
2. Go to the folder of the repository
3. Run `poetry install`
4. Create a folder named `data` in the repository folder. It should be on the same level as `src`
5. Add a .txt file in the data folder.
6. Run `python3 src/index.py`
7. Give the name of the .txt file (not path!). For example, `example.txt`
8. If this doesn't work then I made a mistake, sorry
9. The sentence is generated randomly, not via a Markov process (yet)
