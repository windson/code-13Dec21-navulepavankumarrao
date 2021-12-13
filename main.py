import json
import pandas as pd
import numpy as np
import argparse
from typing import Any



def load_json(path: str)-> Any:
    ref = {}
    with open(path) as f:
        ref = json.load(f)
    return ref

def load_input_data(input_json_path:str) -> dict:
    if input_json_path :
        try:
            data = load_json(input_json_path)
        except:
            print('Unable to find json provided, proceeding with default data')
    else:
        data = load_json('data/inp.json')  
    
    return data

def calculate_bmi(h: np.ndarray, w: np.ndarray) -> float:
    n = len(h)
    bmi = np.empty(n, dtype= np.float32)
    for i in range(n):
        bmi[i] = w[i] / (h[i] / 100)
    return bmi

def build_patient_info(df , df_ref)-> pd.DataFrame:
    types = ['BMICategory', 'HealthRisk']
    for type in types:
        mapper = pd.Series(df_ref[type])
        mapper.index = df_ref['BMIRangeFrom']

        cutoffs = df_ref['BMIRangeFrom'].copy()
        cutoffs[cutoffs.index.max() + 1] = df_ref['BMIRangeTo'].max()

        bins = pd.cut(df['BMI'], bins=cutoffs)
        df[type] = mapper.loc[pd.IntervalIndex(bins).left].values
    return df

def build_patient_info_slow(df, df_ref) -> pd.DataFrame:
    df_ref.index = pd.IntervalIndex.from_arrays(df_ref.BMIRangeFrom, df_ref.BMIRangeTo, closed= 'both')
    df['BMICategory'] = df['BMI'].apply(lambda r: df_ref.iloc[df_ref.index.get_loc(r)].BMICategory)
    df['HealthRisk'] = df['BMI'].apply(lambda r: df_ref.iloc[df_ref.index.get_loc(r)].HealthRisk)
    return df

def get_count_by_category(df, category: str) -> int:
    return df[df.BMICategory == category].shape[0]


def initialize_arg_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description='Patient BMI Info Analyzer')
        parser.add_argument('-i', '--input-json-path',
                            required= False,
                            help = 'Path of the patient input data in .json format')
        parser.add_argument('-c', '--category', default='Overweight',
                            required= False,
                            help = 'Prints the count of category provided. Possible values: "Underweight", "Normal weight", "Overweight", "Moderately obese", "Severely obese", "Very severely obese"')
        parser.add_argument('-d', '--disable-time-tracker', action='store_true',
                            required= False,
                            help = 'Disables time tracker if this argument is provided.')
        parser.add_argument('-v', '--verbose', action='store_true',
                            required= False,
                            help = 'Prints data to the console if this argument is provided. Be careful with large datasets ☠')
        
        return parser

if __name__ == '__main__':
    
    parser = initialize_arg_parser()
    args = parser.parse_args()
    enable_time_tracker = not args.disable_time_tracker
    import time
    if enable_time_tracker:
        start_time = time.monotonic()

    input_json_path = args.input_json_path
    verbose = args.verbose
    data = load_input_data(input_json_path)

    category = args.category
    
    df = pd.DataFrame(data)
    df["BMI"] = calculate_bmi(df.HeightCm, df.WeightKg )
    df_ref = pd.DataFrame(load_json('data/ref.json'))
    #df = build_patient_info_slow(df, df_ref)
    df = build_patient_info(df, df_ref)
    cnt = get_count_by_category(df, category)
    if verbose:
        print(df)
    print(f"Count by Category {category} is: {cnt}")
    if enable_time_tracker:
        print('Total Time in seconds: ', time.monotonic() - start_time)
