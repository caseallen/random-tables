import pandas as pd
from pathlib import Path

default_table = "../data/example-table.csv"

def load_table(filepath=default_table):
    example_table = pd.read_csv(filepath)
    example_table.columns = example_table.columns.str.strip()
    return example_table

def categories(filepath=default_table):
    example_table = load_table(filepath)
    return example_table.columns.to_list()
    
