import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[
       ~customers["id"].isin(orders["customerId"])
    ][["name"]].rename(columns={"name": "Customers"})

"""
# Below solution is outside leetcode function

result = customers[
    ~customers["id"].isin(orders["customerId"])
][["name"]].rename(columns={"name": "Customers"})

print(result)

"""