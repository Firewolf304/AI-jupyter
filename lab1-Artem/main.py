import pandas as pd

df = pd.read_csv(
    "./datasets/data.csv", 
    sep=';', 
    decimal='.', 
    header=0
)
df[:2]

