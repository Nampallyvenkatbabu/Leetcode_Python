# 177. Nth Highest Salary

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Python-blue)

## 🔗 Problem
**LeetCode:** https://leetcode.com/problems/nth-highest-salary/

### Problem Statement
Find the **Nth highest distinct salary** from the Employee table.  
If it doesn’t exist, return `None`.

---

## 💡 Intuition
- Sort salaries descending.  
- Remove duplicates.  
- Return the Nth salary if available.  

---

## 🚀 Approach
1. Sort salaries.  
2. Drop duplicates.  
3. Use index `iloc[n-1]` if valid.  

---

## ✅ Python Solution
```python
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee["salary"].sort_values(ascending=False).drop_duplicates()
    if len(sorted_salaries) < N:
        return pd.DataFrame({"NthHighestSalary": [None]})
    return pd.DataFrame({"NthHighestSalary": [sorted_salaries.iloc[N-1]]})
