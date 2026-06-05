import pandas as pd

data = {
    "employee_id": [101, 102, 103],

    "name": [
        "Rahul",
        "Priya",
        "Amit"
    ],

    "salary": [
        75000,
        85000,
        65000
    ]
}

df = pd.DataFrame(data)

print(df)

import pandas as pd

df = pd.read_csv("employees.csv")

print(df)

print(df.head())

print(df.tail())

print(df.dtypes)

print(df.info())

print(df.describe())   # Statistics

print(df["name"])

print(df[["name", "salary"]])