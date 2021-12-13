# BMI Calculator

Quick n Dirty BMI Calculator (Fast 🚀)

## Bootstrap

Initialize Dev Environment

```shell
python -m venv env
python -m pip install -U pip
pip install -r requirements.txt
```

## Command help

How to run?

```text
usage: main.py [-h] [-i INPUT_JSON_PATH] [-c CATEGORY] [-d] [-v]

Patient BMI Info Analyzer

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_JSON_PATH, --input-json-path INPUT_JSON_PATH
                        Path of the patient input data in .json format
  -c CATEGORY, --category CATEGORY
                        Prints the count of category provided. Possible values: "Underweight", "Normal weight", "Overweight", "Moderately
                        obese", "Severely obese", "Very severely obese"
  -d, --disable-time-tracker
                        Disables time tracker if this argument is provided.
  -v, --verbose         Prints data to the console if this argument is provided. Be careful with large datasets ☠

```

simply run `python main.py`

## Time taken with simple data

### Test run 1

```shell
python main.py -c "Overweight" -i data/inp.json -v
```

Output:

```text
   Gender  HeightCm  WeightKg        BMI          BMICategory      HealthRisk
0    Male       171        96  56.140350  Very severely obese  Very high risk
1    Male       161        85  52.795033  Very severely obese  Very high risk
2    Male       180        77  42.777779  Very severely obese  Very high risk
3  Female       166        62  37.349396       Severely obese       High risk
4  Female       150        70  46.666668  Very severely obese  Very high risk
5  Female       167        82  49.101795  Very severely obese  Very high risk
Count by Category Overweight is: 0
Total Time in seconds:  0.07799999999406282
```

### Test run 2

```shell
python main.py -c "Severely obese" -i data/inp.json -v
```

Output:

```text
   Gender  HeightCm  WeightKg        BMI          BMICategory      HealthRisk
0    Male       171        96  56.140350  Very severely obese  Very high risk
1    Male       161        85  52.795033  Very severely obese  Very high risk
2    Male       180        77  42.777779  Very severely obese  Very high risk
3  Female       166        62  37.349396       Severely obese       High risk
4  Female       150        70  46.666668  Very severely obese  Very high risk
5  Female       167        82  49.101795  Very severely obese  Very high risk
Count by Category Severely obese is: 1
Total Time in seconds:  0.06300000000192085
```

### Test run 3

```shell
python main.py -c "Very severely obese" -i data/inp.json -v
```

Output:

```text
   Gender  HeightCm  WeightKg        BMI          BMICategory      HealthRisk
0    Male       171        96  56.140350  Very severely obese  Very high risk
1    Male       161        85  52.795033  Very severely obese  Very high risk
2    Male       180        77  42.777779  Very severely obese  Very high risk
3  Female       166        62  37.349396       Severely obese       High risk
4  Female       150        70  46.666668  Very severely obese  Very high risk
5  Female       167        82  49.101795  Very severely obese  Very high risk
Count by Category Very severely obese is: 5
Total Time in seconds:  0.07899999999790452
```

## Time taken with dataset having 100K+ records

Tests run in non-verbose mode

```shell
python main.py -c "Overweight" -i data/in100k.json
```

Output:

```text
Count by Category Overweight is: 0
Total Time in seconds:  4.936999999998079
```

```shell
python main.py -c "Severely obese" -i data/in100k.json
```

Output:

```text
Count by Category Severely obese is: 16766
Total Time in seconds:  5.51600000000326
```

```shell
python main.py -c "Very severely obese" -i data/in100k.json
```

Output:

```text
Count by Category Very severely obese is: 83830
Total Time in seconds:  5.125
```
