import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivot_weather = weather.pivot_table(index='month',columns = 'city', values='temperature',aggfunc ='max')
    return pivot_weather
    