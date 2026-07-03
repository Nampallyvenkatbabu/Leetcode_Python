# 1741. Total Time Spent by Each Employee

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)
![Language](https://img.shields.io/badge/Language-Pandas-blue)

## 🔗 Problem

**LeetCode:** https://leetcode.com/problems/find-total-time-spent-by-each-employee/

---

## 📝 Problem Statement

Write a solution to calculate the **total time in minutes** spent by each employee on each day at the office.

An employee can enter and leave the office more than once in a single day. The time spent for each visit is calculated as:

```text
out_time - in_time
```

Return the result table in **any order**.

---

## 💡 Intuition

To determine the total time spent by each employee every day:

- Compute the duration of every office visit using `out_time - in_time`.
- Group records by both `emp_id` and `event_day`.
- Sum all visit durations within each group.
- Rename `event_day` to `day` to match the expected output format.

---

## 🚀 Approach

1. Create a new column `total_time` as `out_time - in_time`.
2. Group the data by `emp_id` and `event_day`.
3. Sum the `total_time` values for each group.
4. Keep grouped columns using `as_index=False`.
5. Rename `event_day` to `day`.
6. Return the final DataFrame.

---

## ✅ Python (Pandas) Solution

```python
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate time spent for each visit
    employees["total_time"] = employees["out_time"] - employees["in_time"]

    # Sum total time for each employee on each day
    result = (
        employees.groupby(["emp_id", "event_day"], as_index=False)["total_time"]
        .sum()
        .rename(columns={"event_day": "day"})
    )

    return result
```

---

## 🧪 Example

### Input

| emp_id | event_day | in_time | out_time |
|:------:|:---------:|:-------:|:--------:|
| 1 | 2020-11-28 | 4 | 32 |
| 1 | 2020-11-28 | 55 | 200 |
| 1 | 2020-12-03 | 4 | 42 |
| 2 | 2020-11-28 | 3 | 33 |
| 2 | 2020-12-09 | 47 | 74 |

### After Calculating `total_time`

| emp_id | event_day | total_time |
|:------:|:---------:|:----------:|
| 1 | 2020-11-28 | 28 |
| 1 | 2020-11-28 | 145 |
| 1 | 2020-12-03 | 38 |
| 2 | 2020-11-28 | 30 |
| 2 | 2020-12-09 | 27 |

### Final Output

| emp_id | day | total_time |
|:------:|:----------:|:----------:|
| 1 | 2020-11-28 | 173 |
| 1 | 2020-12-03 | 38 |
| 2 | 2020-11-28 | 30 |
| 2 | 2020-12-09 | 27 |

---

## 🔑 Key Takeaways

- `out_time - in_time` computes the duration of each office visit.
- `groupby(["emp_id", "event_day"])` groups records by employee and day.
- `.sum()` aggregates the total minutes worked.
- `as_index=False` preserves grouped columns as regular DataFrame columns.
- Renaming `event_day` to `day` ensures the output matches the required schema.

---

## 🏷 Tags

`Pandas` `GroupBy` `Aggregation` `DataFrame` `LeetCode`
