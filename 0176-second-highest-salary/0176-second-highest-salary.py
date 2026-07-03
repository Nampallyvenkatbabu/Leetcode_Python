import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee['salary'].sort_values(ascending=False).drop_duplicates()

    if len(sorted_salaries) < 2:
        return pd.DataFrame({f'SecondHighestSalary':[None]})

    return pd.DataFrame({'SecondHighestSalary':[sorted_salaries.iloc[1]]})
    