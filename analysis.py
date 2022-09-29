import pandas as pd

data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

new_data = data[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]
print(new_data.columns)

new_data.plot(
    kind="scatter",
    x="Mortality rate, infant (per 1,000 live births)",
    y="GDP per capita (constant 2010 US$)",
)
