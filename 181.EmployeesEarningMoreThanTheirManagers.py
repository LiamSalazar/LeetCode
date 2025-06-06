import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(employee, how='left', left_on='managerId', right_on='id',suffixes=('', '_manager'))
    result = merged[merged['salary'] > merged['salary_manager']]
    return result[['name']].rename(columns={'name': 'employee'})