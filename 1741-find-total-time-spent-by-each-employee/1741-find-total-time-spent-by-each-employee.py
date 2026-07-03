import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    # Calculate time spent for each entry
    employees["total_time"] = employees["out_time"] - employees["in_time"]

    # Group by emp_id and event_day, summing total_time
    df = employees.groupby(["emp_id", "event_day"], as_index=False)["total_time"].sum()

    # Rename event_day → day to match expected output
    df = df.rename(columns={"event_day": "day"})

    return df




