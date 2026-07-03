# 176. Second Highest Salary

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Pandas-blue)

## 🔗 Problem

**LeetCode:** https://leetcode.com/problems/second-highest-salary/

### Problem Statement

Given the `Employee` table, find the **second highest distinct salary**.

If there is no second highest salary, return **None**.

---

## 💡 Intuition

To find the second highest salary:

- Sort the salaries in descending order.
- Remove duplicate salaries.
- Return the second salary if it exists.
- Otherwise, return `None`.

---

## 🚀 Approach

1. Select the `salary` column.
2. Sort salaries in descending order.
3. Remove duplicate salaries using `drop_duplicates()`.
4. Check whether at least two distinct salaries exist.
5. Return the second highest salary.
6. Otherwise return `None`.

---

## ✅ Python (Pandas) Solution

```python
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee["salary"].sort_values(
        ascending=False
    ).drop_duplicates()

    if len(sorted_salaries) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})

    return pd.DataFrame(
        {"SecondHighestSalary": [sorted_salaries.iloc[1]]}
    )
```

---

## ⏱ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(n log n)** |
| Space | **O(n)** |

### Why?

- Sorting takes **O(n log n)**.
- Removing duplicates takes **O(n)**.
- Accessing the second element takes **O(1)**.

Overall complexity:

**Time:** `O(n log n)`

**Space:** `O(n)`

---

## 🧪 Example

### Input

| id | salary |
|----|--------|
|1|100|
|2|200|
|3|300|

### After Sorting

```text
300
200
100
```

### After Removing Duplicates

```text
300
200
100
```

Second Highest Salary:

```text
200
```

Output

| SecondHighestSalary |
|---------------------|
| 200 |

---

## 🔑 Key Takeaways

- `sort_values()` sorts salaries in descending order.
- `drop_duplicates()` ensures only distinct salaries are considered.
- `iloc[1]` returns the second highest salary.
- Return `None` if fewer than two distinct salaries exist.

---

## 🏷 Tags

`Pandas` `Sorting` `DataFrame` `LeetCode`
