# 1741. Total Time Spent by Each Employee

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)
![Language](https://img.shields.io/badge/Language-Pandas-blue)

## 🔗 Problem
**LeetCode:** https://leetcode.com/problems/total-time-spent-by-each-employee/

### Problem Statement
Write a solution to calculate the **total time in minutes** spent by each employee on each day at the office.  
An employee can enter and leave more than once in a single day.  
The time spent for a single entry is `out_time - in_time`.  

Return the result table in any order.

---

## 💡 Intuition
To compute total time per employee per day:
- Calculate the difference between `out_time` and `in_time` for each entry.  
- Group by both `emp_id` and `event_day`.  
- Sum the total time for each group.  
- Rename `event_day` to `day` to match the expected output format.

---

## 🚀 Approach
1. Compute `total_time = out_time - in_time` for each row.  
2. Use `groupby(["emp_id", "event_day"])` to group by employee and day.  
3. Aggregate with `.sum()` to get total minutes.  
4. Use `as_index=False` to keep group keys as columns.  
5. Rename `event_day → day` for final output.  

---

## ✅ Python (Pandas) Solution
```python
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate time spent for each entry
    employees["total_time"] = employees["out_time"] - employees["in_time"]

    # Group by emp_id and event_day, summing total_time
    df = employees.groupby(["emp_id", "event_day"], as_index=False)["total_time"].sum()

    # Rename event_day → day to match expected output
    df = df.rename(columns={"event_day": "day"})

    return df
```

---

🧪 Example
Input
emp_id	event_day	in_time	out_time
1	2020-11-28	4	32
1	2020-11-28	55	200
1	2020-12-03	4	42
2	2020-11-28	3	33
2	2020-12-09	47	74


After Calculating total_time
emp_id	event_day	total_time
1	2020-11-28	28
1	2020-11-28	145
1	2020-12-03	38
2	2020-11-28	30
2	2020-12-09	27


After GroupBy + Sum
day	emp_id	total_time
2020-11-28	1	173
2020-12-03	1	38
2020-11-28	2	30
2020-12-09	2	27


🔑 Key Takeaways
out_time - in_time computes time per entry.

groupby(["emp_id", "event_day"]) aggregates per employee per day.

as_index=False keeps group keys as columns for clean SQL‑style output.

Renaming event_day → day ensures schema matches expected format.

🏷 Tags
Pandas GroupBy Aggregation LeetCode

## ✅ Python (Pandas) Solution

